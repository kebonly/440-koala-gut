#! /bin/bash
RED="\033[0;31m"
ORANGE="\033[0;33m"
GREEN="\033[0;32m"
NC="\033[0m"

echo -e "${ORANGE}Running Kevin Ly's PSET 4 script..."
# Check we have the correct version of Python running
python_version=$(echo $(python3 -V) | grep -po "\d\.\d.")
echo -e "You are running Python Version $python_version"
echo -e "${RED}NOTE: Must have Python >= 3.8 in order to run this script${NC}"

# Create virtual environment with venv and install libraries
echo -e "${ORANGE}Creating and activating virtual environment..."
python3 -m venv ./venv
source ./venv/bin/activate

echo -e "Checking if pip needs upgrading...${NC}"
pip3 install -q --upgrade pip

echo -e "${ORANGE}Installing Python dependencies...${NC}"
pip3 install -q -r requirements.txt

# Run the main.py file
echo -e "${ORANGE}Running source files to produce figures...${NC}"
python3 ./src/main.py

deactivate

echo -e "${GREEN}Done! (enjoy this cute dog)${NC}"
echo "
   __
o-''|\_____/)
 \_/|_)     )
    \  __  /
    (_/ (_/   

Art by Hayley Jane Wakenshaw"