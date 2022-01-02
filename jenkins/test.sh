#!/bin/bash

echo "Test stage"

# venv created, source
python3 -m venv venv
source venv/bin/activate

# install pip dependencies
pip3 install pytest pytest-cov flask_testing
pip3 install -r requirements.txt

mkdir test-reports

# run pytest
python3 -m pytest \
    --cov=application \
    --cov-report term missing \
    --cov-report xml:test_reports/coverage.xml \
    --junitxml=test_reports/junit_report.xml


# remove venv
deactivate
rm -rf venv