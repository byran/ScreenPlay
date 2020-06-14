#!/usr/bin/env bash

coverage run --branch --module pytest
readonly EXIT_CODE=$?

coverage report --omit=".venv/*" --show-missing > coverage/report.txt
cat coverage/report.txt

coverage html --omit=".venv/*" -d coverage/html

exit ${EXIT_CODE}
