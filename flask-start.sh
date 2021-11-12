#!/bin/sh
cd "${0%/*}"
export FLASK_APP=./api_reviews.py
export FLASK_ENV=development
flask run -h 0.0.0.0