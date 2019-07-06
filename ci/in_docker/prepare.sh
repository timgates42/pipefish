#!/bin/bash

set -euxo pipefail

THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASEDIR="$( dirname "$( dirname "${THISDIR}" )" )"

cp "${BASEDIR}/README.rst" "${BASEDIR}/app/README.rst"

MAIN_MODULE="pymodulenamegoeshere"
MODULES=( "${MAIN_MODULE}" "tests" )
