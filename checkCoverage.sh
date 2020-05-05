#!/bin/bash

coverage run --source=source_files/ --omit=source_files/ui.py -m pytest
coverage report
