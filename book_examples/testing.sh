#!/bin/bash

DIR=$1
PROG=$2

cat ${DIR}/test/${PROG} | python ${DIR}/${PROG}.py