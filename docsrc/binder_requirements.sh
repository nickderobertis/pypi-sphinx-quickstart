#!/bin/bash
cd ..
echo "$(python binder_requirements.py)" > docsrc/source/binder/requirements.txt
cd docsrc
