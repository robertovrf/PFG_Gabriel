#!/bin/bash

for i in {1..36}; do sleep 5 && top -b -n 1 -p $(pidof dana) | tail -1 ; done >> monitor.txt
