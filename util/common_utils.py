def numeric_input_selector(choice_range):
    while True:
        selection = input("Type your choice: ")
        try:
            if int(selection) not in range(choice_range):
                print("ERROR: Input is out of bounds!\n")
            else:
                return int(selection)
        except:
            print("ERROR: Input cannot be converted to integer!\n")


def yesno_input():
    while True:
        selection = input("Enter Y for YES, N for NO: ")
        if selection == "Y" or selection == "1":
            return True
        elif selection == "N" or selection == "0":
            return False
        else:
            print("ERROR: Unexpected input found, please type according to the formatting guide provided!\n")


def numeric_input():
    while True:
        selection = input("Enter a numeric value: ")
        try:
            print("Value is: "+ str(int(selection)) + " is this correct?")
            if yesno_input():
                return int(selection)
        except:
            print("ERROR: Input cannot be converted to integer!\n")

