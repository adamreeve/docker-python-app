#!/bin/bash

WAIT_TIME=0
MAX_WAIT=60
SLEEP=5

until psql -c "SELECT 1;" > /dev/null; do
    echo "postgresql not yet available, waiting"
    sleep $SLEEP
    WAIT_TIME=$(($WAIT_TIME + $SLEEP))
    if [ $WAIT_TIME -eq $MAX_WAIT ]; then
        echo "error: timeout waiting for postgresql"
        exit -1
    fi
done

psql -v ON_ERROR_STOP=1 < create.sql
psql -v ON_ERROR_STOP=1 < data.sql
