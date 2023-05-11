# Exellys-BatchCsvProcessor
A "small" python project to process multiple csv files in one go

**Table of Content**  
*To-be filled in*

## Features

- Processing all csv files that are in the same directory as .py file.
- Being able to exclude/discard csv files from batch processing

### Planned To-Do Items (in order of importance)

- [X] Creating a release
- [ ] Modularising the process
- [ ] Adding checks for setup scripts (python there or not, print meaningful errors during setup etc.)
- [ ] Creating a flowchart
- [ ] Writing a small manual
- New Features
    - [ ] Date range selection
    - [ ] Add Excel Support
      - [ ] Highlight any cells lower than INPUT
    - [ ] Figure out why .csv is always messed up with Excel
      - [ ] Is it regional .csv problem? , vs ;
      - [ ] Maybe tab delimited?
      - [ ] Maybe add metadata indicating , is a delimiter!
    - [ ] Add Additional Stats
      - [ ] Total Average
      - [ ] Highest Rated
      - [ ] Lowest Rated
    - [ ] Second run generates another file, instead of overwriting.
    - [X] Column type inference
    - [ ] Column selector
    - [ ] Unique column identifier
    - [ ] Passing a config

## Installation
Installation of this app is simple.

1. Download the latest release from here (*release TBD, link to be placed*)
2. Install [Python](https://www.python.org/)
   - If using Windows, before hitting next on install  
     **TICK THE BOX** of _Add Python #.## to PATH_.  
   - If forgotten, you can repair the install or add python to system path manually.
3. Install dependencies
    1. Method #1: Install via scripts
        - Open the setup folder
        - Run the flavor of script for your OS.
            - pre-req.sh for Linux
            - pre-req.bat for Windows
    2. Method #2: Install manually through terminal
        - Open the terminal of your OS  
        (Powershell, cmdline for Windows; bash for Linux)
        - Install the dependencies through pip (e.g. pip install pandas)

### Dependency List

Currently, we only need **pandas**.

## How to Run

This is a very simple application, thus running is not that complicated.
But please read all the way through.

1. Place the .csv files that are to be processed in the same directory as
csv-loader.py
2. Rename .csv files into something that represents their data.  
   (Don't name them output.csv but Quarterly Performance Assesment.csv)
3. Run the csv-loader.py by double-clicking.
4. Follow the prompts on the screen.
5. Output file is _processed_output.csv_

:warning: The output file will overwrite itself, if code is ran a second time.
In other words, make sure to change output name. (For the time being)

## Workflow
