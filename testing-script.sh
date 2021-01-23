#!/bin/bash
rm -r htmlcov/*
patterns='*/*__init__*,*/migrations/*'
coverage run --source=. --omit=$patterns manage.py test -v 2
coverage html