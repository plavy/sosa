#!/bin/bash

if [[ ${PERFORM_TEST} == "unittest"]]; then python -m unittest > /logs/\$(date '+%F-%T')-unittest
elif [[ ${PERFORM_TEST} == "bandit"]]; then bandit -r . > /logs/\$(date '+%F-%T')-bandit
else python app.py
fi