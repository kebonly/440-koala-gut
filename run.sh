#! /bin/bash

echo "Running Kevin Ly's PSET 4 script..."

# Check we have the correct version of Python running
python_version=$(python)
python3 -c 'import sys; print(sys.version_info[:])'

# Create virtual environment with venv and install libraries
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt

# Run the main.py file
python3 ./src/main.py