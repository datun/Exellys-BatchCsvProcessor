#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import os

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
        else:
            print("Input is not in correct form!\n")
            
            
def csv_avg(data_list, file_names):
    output = []
    # Create dataframes with file name and averages
    for i in range(len(data_list)):
        columns = [file_names[i] + " Average"]
        df = data_list[i]
        interm = pd.DataFrame(df.iloc[:,2:6].mean().round(3),columns=columns)
        # Store in output list
        output.append(interm)
    return output
    
## Global Variables
csv_list = os.listdir()


# In[5]:


# Info for which columns to choose (and for future improvements)
# 2,3,4,5 : integer check
# 9: Start Date / 10: Submit Date


# In[6]:


if __name__ == "__main__":
    data_list, file_names = csv_2_list(csv_list)
    input_checker(data_list, file_names)
    output = csv_avg(data_list, file_names)
    
    # Concat the output list
    output = pd.concat(output, axis=1)
    output = output.rename_axis(index="Questions", columns="File Name")


    # Get the working directory
    out_path = os.path.join(os.getcwd(), "processed_output.csv")
    print("Output file is saved at this path: " + str(out_path))
    # Save to working directory
    output.to_csv(out_path)

    input("Press Any Key to Exit")

