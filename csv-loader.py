#!/usr/bin/env python

import numpy as np
import pandas as pd
import os
import re

def csv_2_list(csv_list):
    data_list = []  # Create a list with csv loaded as pandas
    file_names = [] # Store a list of valid file names
    for i in csv_list:
        if i.endswith(".csv"):
            try:
                # Skip the output file
                if i == "processed_output.csv":
                    continue
                else:
                    data_list.append(pd.read_csv(i))
                    file_names.append(i)
            except:
                print("Error regarding opening files.")
    return data_list, file_names
            

def input_checker(data_list, file_names):
    checking = True
    while checking:
        print("## This is the list of files that are loaded: ##")
        for i in range(len(file_names)):
            print(str(i) + ": " + str(file_names[i]))

        print("Does the list contain any unwanted .csv files?")
        in_var = input("Type Y/N (Y: Yes/ N: No): ")
        print("\n")

        if in_var.capitalize() == "Y":
            in_var = input("Type number assigned to the csv: ")
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
            
def csv_date_range(data_list):
    date_range = []
    while true:
        # Choose granularity for date filtering
        print("Please choose granularity of date filtering\n
              0: Year Only (e.g. From 2000 To 2023)\n
              1: Year+Month (e.g. From 2000-12 To 2012-06\n
              2: Year+Month+Day (e.g. From 2000-12-12 To 2012-05-01"        
        while true:
            selection = input("Type your choice: ")
            if int(selection) not in range(3):
              print("Invalid selection")
            else:
              break

        # Get start and end dates with accordance to the granularity
        check = 0
        print("Please input range of dates for filtering\n
              If you want to have no upper or lower limit, fill the date with 0\n
              e.g. 2012, 2020-00, 0000, 1999-12-00")

        # Janky way of repeating this process, turn it into a function later
        if not check:
            date_in = input ("Type start date: ")
        if check:
            date_in = input ("Type end date: ")

        # Validate the input, if invalid loop back.
        # see how to use re.compile to improve performance
        if selection == 2 and re.match(r"^((19|20)\d\d|0000)[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$", date_in): # By Full Date
            counter += 1
            date_range.append(date_in)
        elif selection == 1 and re.match(r"^((19|20)\d\d|0000)[- /.](0[1-9]|1[012])$", date_in): # By Month
            counter += 1
            date_range.append(date_in)
        elif selection == 0 and re.match(r"^((19|20)\d\d|0000)$", date_in): # By Year
            counter += 1
            date_range.append(date_in)
        else:
            print("Invalid input, please make sure your input matches with formatting\n")
        
        
        # This is the idea to skip some unnecessary comparisons
        if re.match(r"(^0000$|-00$|-00-)", date_range): # Can we just look at the tuple to match or do we have to go through each element
            skip


        # THE LOGIC IS THIS, BUT MATE SUBTRACTING DATES ARE DUMB AS FUCK.
        # RATHER COMPARE YEARS THEN MONTHS THEN DAYS
        # BUT THAT IS A VERY UGLY CODE
        if check == 2:
            if date_range[1] - date_range[0]:
                OK
            else:
                NOK

    for i in data_list:
        i.iloc[:,9]


def csv_avg(data_list, file_names):
    output = []
    # Create dataframes with file name and averages
    for i in range(len(data_list)):
        columns = [file_names[i] + " Average"]
        df = data_list[i]

        # HARDCODED COLUMN LOCATION REMEMBER TO MODIFY AFTERWARDS #
        interm = pd.DataFrame(df.iloc[:,2:6].mean().round(3),columns=columns)
        # Store in output list
        output.append(interm)
    return output
    
## Global Variables
csv_list = os.listdir()


# Info for which columns to choose (and for future improvements)
# 2,3,4,5 : integer check
# 9: Start Date / 10: Submit Date


if __name__ == "__main__":
    data_list, file_names = csv_2_list(csv_list)
    if data_list:
        input_checker(data_list, file_names)
        if len(data_list):
            output = csv_avg(data_list, file_names)
    
            # Concat the output list
            output = pd.concat(output, axis=1)
            output = output.rename_axis(index="Questions", columns="File Name")


            # Get the working directory
            out_path = os.path.join(os.getcwd(), "processed_output.csv")
            print("Output file is saved at this path: " + str(out_path))
            # Save to working directory
            output.to_csv(out_path)
        else:
            print("The processing list is empty!")
    else:
        print("No csv files are found within work directory")
    input("Press Any Key to Exit")

