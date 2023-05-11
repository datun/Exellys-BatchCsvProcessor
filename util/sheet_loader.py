#!/usr/bin/env python

import os
import re
import pandas as pd
from common_utils import *


def data_2_list(data_dir, file_format, reader):
    data_list = []  # Create a list with csv loaded as pandas
    file_names = []  # Store a list of valid file names
    for i in data_dir:
        if i.endswith(file_format):
            try:
                # Skip the output file
                if i == "processed_output"+file_format:
                    continue
                else:
                    data_list.append(reader(i))
                    file_names.append(i)
            except:
                print("Error regarding opening files.")
    return data_list, file_names
            

def verify_input_list(data_list, file_names):
    checking = True
    while checking:
        print("## This is the list of files that are loaded: ##")
        for i in range(len(file_names)):
            print(str(i) + ": " + str(file_names[i]))

        print("Does the list contain any unwanted .csv files?")
        in_var = input("Type Y/N (Y: Yes/ N: No): ")
        print("\n")

        if in_var.capitalize() == "Y":
            in_var = input("Type the number of file to be removed from list: ")
            print("\n")
            if in_var.isdigit():
                in_var = int(in_var)
                if in_var < len(data_list):
                    data_list.pop(in_var)
                    file_names.pop(in_var)
                else:
                    print("Input is out of range!\n")
            else:
                print("Input is not a digit!\n")
        elif in_var.capitalize() == "N":
            checking = False
            # Accepted inputs are finalised, inferring data type
            for i in data_list:
                i = i.infer_objects()
        else:
            print("Input is not in correct form!\n")


def file_output(out_data, option, extension):
    # Get the working directory
    out_path = os.path.join(os.getcwd(), "processed_output"+ extension)
    print("Output file is saved at this path: " + str(out_path))
    # Save to working directory
    if option == 0:
        out_data.to_excel(out_path)
    else:
        out_data.to_csv(out_path)



