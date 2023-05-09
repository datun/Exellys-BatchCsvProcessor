

def numeric_input_selector(choice_range):
    while true:
        selection = input("Type your choice: ")
        try int(selection):
            if int(selection) not in range(choice_range):
                print("ERROR: Input is out of bounds!\n")
            else:
                return int(selection)
        except:
            print("ERROR: Input cannot be converted to integer!\n)

