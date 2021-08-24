# Advent of Code Solutions

This is a collection of my solutions for [Advent of Code](https://adventofcode.com) puzzles in Python.
___

### Directory Structure

All directories in the repo correspond to each year's solutions. Within each year's directory there are two subdirectories:  
- `scripts`: solutions for each day's puzzles represented as executable Python scripts;
- `data`: .txt files containing data for each day's puzzle

### Setting Up

To install dependencies for running solution scripts for a particular year please run
```
cd [year]
poetry install
```
### Running the Scripts

In order to generate a solution for a particular day, you need to run the .py file for the corresponding day passing the path to the datafile as an argument.

```
python ./scripts/day_1.py ./data/day_1.txt
```
