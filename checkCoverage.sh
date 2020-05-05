#!/bin/bash

coverage run --source=source_files/ -m pytest
coverage report
