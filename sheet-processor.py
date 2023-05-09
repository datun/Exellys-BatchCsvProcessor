#!/usr/bin/env python

import numpy as np
import pandas as pd
import os
import re
from util/sheet_loader.py import * as sheetIO
from util/sheet_operations.py import * as sheetOps
from util/common_utils import * as util


class Worksheet:
    def __init__(self, option, highlight=False, hvalue=None, hdirection=False)
    self.extension = None
    self.separator = None
    self.reader = None
    self.option = option
    self.format_choice(option)
    self.highlight = self.highlight
    self.hvalue = hvalue
    self.hdirection = hdirection

    def format_choice(self, choice):
        match choice:
            case 0:
                self.extension = ".xls"
                self.separator = ","
                self.reader = pd.read_excel
            case 1:
                self.extension = ".csv"
                self.separator = ";"
                self.reader = pd.read_csv
            case 2:
                self.extension = ".csv"
                self.separator = ","
                self.reader = pd.read_csv
        



   
## Global Variables
data_dir = os.listdir()


# Info for which columns to choose (and for future improvements)
# 2,3,4,5 : integer check
# 9: Start Date / 10: Submit Date


if __name__ == "__main__":

    print("### Please choose the file format of your choice ###\n
          0: Excel File (.xls)\n
          1: Comma-Separated Values File (.csv) European (;=sep)\n
          2: Comma-Separated Values File (.csv) American (,=sep)\n")
    choice = util.numeric_input_selector(3)
    if choice == 0:
        print("### Would you like to highlight certain values? ###\n")
        choice_2 = util.yesno_input()
        if choice_2:
            highlight = True
            hvalue = util.numeric_input()
            hdirection = util.yesno_input()

            #### LAST LEFT HERE


    sheet = Worksheet(choice)
    data_list, file_names = sheetIO.data_2_list(data_dir, sheet.extension, sheet.reader))

    if data_list:
        sheetIO.verify_input_list(data_list, file_names)
        if len(data_list):
            output = sheetOps.average(data_list, file_names)
    
            # Concat the output list
            output = pd.concat(output, axis=1)
            output = output.rename_axis(index="Questions", columns="File Name")
            sheetIO.file_output(choice, sheet.extension)
        else:
            print("The processing list is empty!")
    else:
        print("No valid input format files are found within work directory")
    input("Press Any Key to Exit")

