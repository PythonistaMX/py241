#! /usr/bin/bash
cd src/abc_alumnos/
export FLASK_APP=$PWD/main.py
flask run --host=0.0.0.0