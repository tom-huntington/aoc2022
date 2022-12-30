#!/bin/sh
cat "p${1}.in" | python3.11 "${1}.py"
