#!/usr/bin/env python3
import sys
import json
from os import path
from screenplay.behave_extensions.collecting_formatter import CollectedFeature
from screenplay.behave_extensions.sphinx_file_writer import SphinxFileWriter
from screenplay.behave_extensions.markup_feature_file_writer import write_markup_feature_file


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Invalid command format, format is:\n {a[0]} <json feature file>\n'.format(a=sys.argv))
        exit(1)

    with open(sys.argv[1], 'rt') as file:
        feature = CollectedFeature.from_json(json.load(file))

    (file_name, _) = path.splitext(sys.argv[1])
    file_name += '.rst'

    with open(file_name, 'wt') as file:
        sphinx_writer = SphinxFileWriter(file)
        write_markup_feature_file(feature, sphinx_writer)
