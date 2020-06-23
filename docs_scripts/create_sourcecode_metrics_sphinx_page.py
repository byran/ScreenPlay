#!/usr/bin/env python3
import sys, json
from screenplay.behave_extensions.sphinx_file_writer import SphinxFileWriter


class FunctionMetrics:
    def __init__(self):
        self.complexity = 0


class FileMetrics:
    def __init__(self):
        self.functions = {}
        self.maintainability = 0
        self.lines_of_code = 0


def process_maintainability(maintainability, files):
    for file in maintainability:
        file_metrics = FileMetrics()
        file_metrics.maintainability = maintainability[file]['mi']

        files[file] = file_metrics


def process_complexity(complexity, files):
    for file in complexity:
        file_metrics = files[file]

        for item in complexity[file]:
            function_metrics = FunctionMetrics()
            function_metrics.complexity = item['complexity']

            if item['type'] == 'function':
                file_metrics.functions[item['name']] = function_metrics

            if item['type'] == 'method':
                file_metrics.functions[item['classname'] + '.' + item['name']] = function_metrics


def process_common(common, files):
    for file in common:
        file_metrics = files[file]
        file_metrics.lines_of_code = common[file]['loc']


def calculate_average_and_max_complexity(files):
    max_complexity = 0
    total = 0
    count = 0
    for file in files:
        functions = files[file].functions
        for function in functions:
            f = functions[function]
            total += f.complexity
            max_complexity = max(max_complexity, f.complexity)
            count += 1

    if count == 0:
        return (0, 0)
    return (total / count, max_complexity)



def calculate_summary_file_metrics(files):
    max_loc = 0
    total_loc = 0
    min_maintainability = 100
    total_maintainability = 0
    count = 0
    for file in files:
        f = files[file]
        max_loc = max(max_loc, f.lines_of_code)
        total_loc += f.lines_of_code
        min_maintainability = min(min_maintainability, f.maintainability)
        total_maintainability += f.maintainability
        count += 1
    
    if count == 0:
        return (0, 0, 0, 0)
    return (total_loc / count, max_loc, total_maintainability / count, min_maintainability)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Invalid arguments:\n{cmd} <output file>\n'.format(cmd=sys.argv[0]))
        exit(1)

    files = {}

    with open('mi.json') as mi:
        maintainability = json.load(mi)
    process_maintainability(maintainability, files)

    with open('cc.json') as cc:
        complexity = json.load(cc)
    process_complexity(complexity, files)

    with open('raw.json') as raw:
        common = json.load(raw)
    process_common(common, files)

    with open(sys.argv[1], 'wt') as file:
        fileWriter = SphinxFileWriter(file)

        fileWriter.write_heading_1('Code metrics')

        fileWriter.write_heading_2('Summary')

        fileWriter.begin_table('metric', 'value')
        (average_complexity, max_complexity) = calculate_average_and_max_complexity(files)
        fileWriter.add_table_row('average complexity', str(average_complexity))
        fileWriter.add_table_row('max complexity', str(max_complexity))
        (average_loc, max_loc, average_maintainability, min_maintainability) = calculate_summary_file_metrics(files)
        fileWriter.add_table_row('average lines of code', str(average_loc))
        fileWriter.add_table_row('max lines of code', str(max_loc))
        fileWriter.add_table_row('average maintainability', str(average_maintainability))
        fileWriter.add_table_row('min maintainability', str(min_maintainability))
        fileWriter.end_table()

        fileWriter.write_heading_2('Individual file code metrics')

        for file in files:
            fileWriter.write_heading_3(file)
            file_metrics = files[file]

            fileWriter.write_lines(
                'Maintainability: {v}'.format(v=file_metrics.maintainability),
                'Lines of code: {v}'.format(v=file_metrics.lines_of_code)
            )

            functions = file_metrics.functions
            if len(functions) > 0:
                fileWriter.begin_table('function/method', 'complexity')
                for function in functions:
                    fileWriter.add_table_row(function, str(functions[function].complexity))
                fileWriter.end_table()
