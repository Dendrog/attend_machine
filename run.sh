#!/bin/bash

while true; do
    python3 requ.py &
    wait $!
    sleep 180  # 3분 동안 대기
done