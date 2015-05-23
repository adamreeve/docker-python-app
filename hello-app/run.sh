#!/bin/bash

if [ "$DEBUG" == "true" ]; then
    python run.py
else
    /usr/local/bin/gunicorn --error-logfile=- -w 2 -b 0.0.0.0:8080 run:wsgi_app
fi
