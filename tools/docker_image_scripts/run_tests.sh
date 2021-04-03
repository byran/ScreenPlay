#!/usr/bin/env bash

set -e

readonly SCRIPT_PATH=$(realpath $(dirname $0))

cd "${SCRIPT_PATH}"
cd ../../

source .venv/bin/activate

cd src

set +e
behave
readonly EXIT_CODE=$?
set -e

exit ${EXIT_CODE}
