#!/usr/bin/env bash

tmp_stderr=stderr.tmp
tmp_stdout=stdout.tmp
rm -f $tmp_stderr
rm -f $tmp_stdout

while :
do
    bash random.sh 2>> $tmp_stderr >> $tmp_stdout
    if $(grep -q "error" $tmp_stderr); then
        echo "$(cat $tmp_stdout | wc -l)"
        break
    fi
done