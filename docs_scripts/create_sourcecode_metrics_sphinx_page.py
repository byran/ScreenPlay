#!/usr/bin/env python3
import sys
import json
from jinja2 import Template


def non_class_complexity(file):
    count = 0
    for item in file:
        if item['type'] != "class":
            count = count + 1
    return count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Invalid arguments:\n{cmd} <output file>\n'.format(cmd=sys.argv[0]))
        exit(1)

    with open('mi.json') as mi:
        maintainability = json.load(mi)

    with open('cc.json') as cc:
        complexity = json.load(cc)

    with open('raw.json') as raw:
        common = json.load(raw)

    context = {
        "mi": maintainability,
        "cc": complexity,
        "raw": common,
        "non_class_complexity": non_class_complexity
    }

    with open('metrics.template') as file:
        template = file.read()

    with open(sys.argv[1], 'wt') as file:
        file.write(Template(template).render(**context))
