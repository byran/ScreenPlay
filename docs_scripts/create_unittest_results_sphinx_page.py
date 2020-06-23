#!/usr/bin/env python3
import sys
from screenplay.behave_extensions.sphinx_file_writer import SphinxFileWriter


def is_failing_test(test_element):
    for element in test_element:
        if element.tag == 'failure':
            return True
    return False


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Invalid arguments:\n{cmd} <results file> <output file>\n'.format(cmd=sys.argv[0]))
        exit(1)

    import xml.etree.ElementTree as ET
    tree = ET.parse(sys.argv[1])
    root = tree.getroot()

    with open(sys.argv[2], 'wt') as file:
        fileWriter = SphinxFileWriter(file)
        pass_text = fileWriter.text_with_style('pass', 'passed')
        fail_text = fileWriter.text_with_style('fail', 'failed')

        fileWriter.write_heading_1('Unit test results')

        last_file = None
        for testsuite in root:
            fileWriter.begin_table('Test attribute', 'value')
            fileWriter.add_table_row('Number of tests', testsuite.attrib['tests'])
            fileWriter.add_table_row('Failing tests', testsuite.attrib['failures'])
            fileWriter.add_table_row('Errors', testsuite.attrib['errors'])
            fileWriter.add_table_row('Skipped tests', testsuite.attrib['skipped'])
            fileWriter.end_table()

            for testcase in testsuite:
                test_file_name = testcase.attrib['classname']

                if test_file_name != last_file:
                    if last_file is not None:
                        fileWriter.end_table()
                    last_file = test_file_name
                    fileWriter.write_heading_2(test_file_name)
                    fileWriter.begin_table('Test', 'result')

                if is_failing_test(testcase):
                    fileWriter.add_table_row(testcase.attrib['name'], fail_text)
                else:
                    fileWriter.add_table_row(testcase.attrib['name'], pass_text)
            fileWriter.end_table()
