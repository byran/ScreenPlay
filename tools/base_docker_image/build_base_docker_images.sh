#!/usr/bin/env bash

readonly SCRIPT_PATH=$(realpath $(dirname $0))

cd "${SCRIPT_PATH}"

docker rmi byran/python-screenplay
docker build -t byran/python-screenplay .
