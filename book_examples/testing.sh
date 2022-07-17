#!/bin/bash

DIR=$1
PROG=$2
CNT=$3


if [[ $CNT -ge 2 ]]
then
    for ((i=1;i<$CNT+1;i++))
    do
        cat ${DIR}/test/${PROG}_${i} | python ${DIR}/${PROG}.py
    done
else
    cat ${DIR}/test/${PROG} | python ${DIR}/${PROG}.py
fi
