#!/bin/sh

export pycmd=/usr/bin/python3

export FLASK_ENV=development
export FLASK_APP=main.py

echo "Flask Environment: $FLASK_ENV"
echo "Flask Application: $FLASK_APP"

flask run main.py
