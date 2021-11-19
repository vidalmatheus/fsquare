#!/bin/bash
RESTORE='\033[0m'
RED='\033[00;31m'
GREEN='\033[00;32m'
YELLOW='\e[0;33m'
BLUE='\033[0;34m'
LBLU='\033[1;34m'

HOST={{name}}.example.com

{{name}}

export PROJ_BASE="$(dirname ${BASH_SOURCE[0]})"
CD=$(pwd)
cd $PROJ_BASE
export PROJ_BASE=$(pwd)
cd $CD


function devhelp {
    echo -e "${LBLU}devhelp${RESTORE}           Print this ${GREEN}help${RESTORE}"
    echo -e ""
    echo -e "${LBLU}dkdev${RESTORE}             Runs a dockerized ${GREEN}postgresql${RESTORE}, ${GREEN}nginx${RESTORE} and ${GREEN}metabase${RESTORE}"
    echo -e ""
    echo -e "${LBLU}dkdb${RESTORE}              Runs a dockerized ${GREEN}postgresql${RESTORE} database on port ${GREEN}5432${RESTORE}"
    echo -e ""
    echo -e "${LBLU}dknginx${RESTORE}           Runs a dockerized ${GREEN}nginx${RESTORE} on port 80 to 8000(back) and 3000(front)"
    echo -e ""
    echo -e "${LBLU}pytest${RESTORE}            Runs python ${GREEN}test${RESTORE}"
    echo -e ""
    echo -e "${LBLU}pycoverage${RESTORE}        Runs python ${GREEN}tests${RESTORE} with flake8 and coverage report"
    echo -e ""
    echo -e "${LBLU}dkbuild${RESTORE}           Builds a ${GREEN}docker image${RESTORE} for this project"
    echo -e ""
    echo -e "${LBLU}dkfulldev${RESTORE}         Runs dockerized ${GREEN}postgresql${RESTORE}, ${GREEN}nginx${RESTORE}, ${GREEN}metabase${RESTORE} and ${GREEN}project image${RESTORE}"
    echo -e ""
}

function echo_blue {
    echo -e "${LBLU}$1${RESTORE}";
}

function echo_green {
    echo -e "${GREEN}$1${RESTORE}";
}

function dkdev {
    invoke dkdev
}

function dkdb {
    invoke dkdb
}

function dknginx {
    invoke dknginx
}

function pycoverage {
    invoke pycoverage
}

function dkbuild {
    invoke dkbuild
}

function dkfulldev {
    invoke dkfulldev
}

echo_green "Welcome to the {{name}}'s development environment:"
echo_green "Tip: autocomplete works for the commands below \o/"
echo_green "-------------------------------------------------------------"
devhelp
