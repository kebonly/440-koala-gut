# 20.440 Problem Set 4 Tutorial
This respository was created as an educational exercise for the MIT class [20.440 Analysis of Biological Networks](http://be.mit.edu/academic-programs/courses/20440) (Spring 2023).

---

## Overview & Data
The figure generated comes from data reported by *[Alphano (2015)](https://www.nature.com/articles/srep10189)* in the supplementary section (relevant Excel file linked in ```./raw_data```). The figure shows a pie chart of various families of microbes found in the gastrointestinal tract of two koalas in captivity.

---
## Folder Structure
This root directory of this repository contains three main folders:
- ```src```: Contains all needed code to process and visualize and save data and/or figures.
- ```raw_data```: Contains the original, raw data that will be run by code in ```src```.
- ```fig```: Output figure visualizations.

---
## Installation
To see if everything works, navigate to the projects root directory and type in the command:
```bash
source ./run.sh
```
You can expect for all the figures to populate the ```fig``` folder.

> **Note:** Running this shell script will check that you have at least Python 3.7.9 and create a virtual environment via ```venv``` to download dependencies.

---
