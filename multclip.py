import sys
import json


SAVED_DATA = "clipboard.json" # path to the json file


def save_data(filepath, data):
    with open(filepath, "w") as f: # w for write
        json.dump(data, f) # saving the data (like a dictionary)


def load_data(filepath): #loading the chosen data
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1] # taking the second argument, the passed command 
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = input("Enter the relative data: ")
        save_data(SAVED_DATA, data)
        print("Data saved!")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            print(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.")