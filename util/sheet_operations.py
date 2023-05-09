#!/usr/bin/env python

import pandas as pd
from common_utils import * as util


############### COMMENTED OUT THE DATE IMPLEMENTATION, HEADACHE INDUCING SIMPLE PROBLEM
#def date_range(data_list):
#    date_range = []
#    while true:
#        # Choose granularity for date filtering
#        print("Please choose granularity of date filtering\n
#              0: Year Only (e.g. From 2000 To 2023)\n
#              1: Year+Month (e.g. From 2000-12 To 2012-06\n
#              2: Year+Month+Day (e.g. From 2000-12-12 To 2012-05-01")
#        choice = util.numeric_input_selector(3)
#
#        # Get start and end dates with accordance to the granularity
#        check = 0
#        print("Please input range of dates for filtering\n
#              If you want to have no upper or lower limit, fill the date with 0\n
#              e.g. 2012, 2020-00, 0000, 1999-12-00")
#
#        # Janky way of repeating this process, turn it into a function later
#        if not check:
#            date_in = input ("Type start date: ")
#        if check:
#            date_in = input ("Type end date: ")
#
#        # Validate the input, if invalid loop back.
#        # see how to use re.compile to improve performance
#        if choice == 2 and re.match(r"^((19|20)\d\d|0000)[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$", date_in): # By Full Date
#            counter += 1
#            date_range.append(date_in)
#        elif choice == 1 and re.match(r"^((19|20)\d\d|0000)[- /.](0[1-9]|1[012])$", date_in): # By Month
#            counter += 1
#            date_range.append(date_in)
#        elif choice == 0 and re.match(r"^((19|20)\d\d|0000)$", date_in): # By Year
#            counter += 1
#            date_range.append(date_in)
#        else:
#            print("Invalid input, please make sure your input matches with formatting\n")
#        
#        
#        # This is the idea to skip some unnecessary comparisons
#        if re.match(r"(^0000$|-00$|-00-)", date_range): # Can we just look at the tuple to match or do we have to go through each element
#            skip
#
#
#        # THE LOGIC IS THIS, BUT MATE SUBTRACTING DATES ARE DUMB AS FUCK.
#        # RATHER COMPARE YEARS THEN MONTHS THEN DAYS
#        # BUT THAT IS A VERY UGLY CODE
#        if check == 2:
#            if date_range[1] - date_range[0]:
#                OK
#            else:
#                NOK
#
#    for i in data_list:
#        i.iloc[:,9]



def average(data_list, file_names):
    output = []
    # Create dataframes with file name and averages
    for i in range(len(data_list)):
        df = data_list[i]

        # HARDCODED COLUMN LOCATION REMEMBER TO MODIFY AFTERWARDS #
        interm = pd.DataFrame(df.iloc[:,2:6].mean().round(3),columns=file_names[i])
        # Store in output list
        output.append(interm)
    return output

def highlight(data, value, direction):
    if direction:
        data = data.style.applymap(lambda x: f"color: {'red' if x < value else 'black'}")
    else:
        data = data.style.applymap(lambda x: f"color: {'red' if x > value else 'black'}")
