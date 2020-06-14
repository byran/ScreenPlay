#!/usr/bin/env bash

coverage run --module pytest
readonly EXIT_CODE=$?

coverage report --omit=".venv/*" --show-missing > coverage.txt

cat coverage.txt

exit ${EXIT_CODE}
