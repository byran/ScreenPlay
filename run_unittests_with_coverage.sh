#!/usr/bin/env bash

coverage run --branch --module pytest --junit-xml=unittest_results.xml
readonly EXIT_CODE=$?

coverage report --omit=".venv/*" --show-missing > coverage/report.txt
cat coverage/report.txt

coverage html --omit=".venv/*" -d coverage/html

./create_unittest_results_sphinx_page.py unittest_results.xml docs/unittest_results/unittest_results.rst

exit ${EXIT_CODE}
