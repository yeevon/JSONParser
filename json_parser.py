import string
import sys

# TODO: Future refactor to handle multiple dicts as values embedded inside dicts or list
# TODO: Add validation to check for correct punctuation
# TODO: code clean up

def clean_data(json_file):
    clean_list = list() # declare new clean list

    with open(json_file, 'r') as f: # read json file
        json_data = f.read().strip() # strip json data of leading and trailing spaces

        data_list = json_data[1:-1].split('"') # remove json curly braces and split list based on "

        for data in data_list:  # Loop to create cleaned list

            # Data clean up removing spaces, commas, colons and returns
            data = data.strip(" ,:\n")
            if data == "":
                continue
            clean_list.append(data)

    return clean_list

def convert_to_list(data_list):

    if "[" in data_list:
        x = data_list.index("]") # get index of the end of the dict
        sub_list = data_list[data_list.index("[") + 1: x] # create sublist of items in the dictionary

        value = list() # declare new dictionary
        for data in sub_list: # loop through sublist and add items to new dictionary
            value.append(data) # add key value to dictionary

        while True: # Loop in reverse to recreate the list
            if data_list[x] == "[": # check if back at the beginning of the dictionary
                data_list[x] = value # replace with new dictionary created
                break

            data_list.pop(x) # remove list items that are part of constructed dictionary
            x -= 1
    return data_list

def create_dict(data_list):
    value = dict()  # declare new dictionary
    for index, data in enumerate(data_list):  # loop through sublist and add items to new dictionary
        if index % 2 == 0:  # if loop on key skip to next item
            continue

        # add key value to dictionary
        if isinstance(data, str) and data.isdigit():
            value[data_list[index - 1]] = int(data)
        elif data == "true":
            value[data_list[index - 1]] = True
        elif data == "false":
            value[data_list[index - 1]] = False
        elif data == "null":
            value[data_list[index - 1]] = None
        else:
            value[data_list[index - 1]] = data

    return value

# Reconstruct json value that is a dictionary
def convert_to_dict(data_list):

    if "{" in data_list:
        x = data_list.index("}") # get index of the end of the dict
        sub_list = data_list[data_list.index("{") + 1: x] # create sublist of items in the dictionary

        value = create_dict(sub_list)

        while True: # Loop in reverse to recreate the list
            if data_list[x] == "{": # check if back at the beginning of the dictionary
                data_list[x] = value # replace with new dictionary created
                break

            data_list.pop(x) # remove list items that are part of constructed dictionary
            x -= 1

    return data_list


def are_key_value_valid(d):
    if d.count('"') != 2:  # Make sure each item has two " symbols
        if d not in ['true', 'null', 'false']:  # Check if data is boolean or null
            if not d.isdigit():  # check if data is digit
                return False
    return True


def is_valid_json(data):

    is_valid = True

    with open(data, 'r') as j_data:
        jd = j_data.read().strip() # set data to jd

        if jd == "": # Return false for empty file
            return False

        if jd[0] == "{" and jd[-1] == "}": # Verify json starts/ends {}
            if len(jd) == 2: # Return true for empty json
                return True

        # Return false if invalid punctuation at end of file
        if jd[-2] in string.punctuation:
            if jd[-2] != '"' and jd[-2] != '}' and jd[-2] != ']':
                return False

        jd_list = jd[1:-1].strip().split(' ') # Create list

        # clean and rebuild list
        sub_list = list()
        for d in jd_list:
            if d == "": # skip empty list item
                continue

            d = d.strip(" ,\n")  # Strip unneeded characters from data
            sub_list.append(d)
        jd_list = sub_list


        for d in jd_list:
            print("-------------------------------")
            print(d)
            if "{" in d: # Check if value is valid json
                if d != "{}":  # Make sure json not empty
                    x = jd_list.index("}")
                    sub_data = " ".join(jd_list[jd_list.index(d):  x + 1]) # get json value and undo split
                    sub_json = sub_data[1:-1].split(':')  # split based on semicolon

                    for sub_d in sub_json: # step through json make sure values are valid
                        if not are_key_value_valid(sub_d):
                            return False

                    # if json is valid remove already validated items from data list
                    while True:
                        if jd_list[x] != "{":
                            jd_list.pop(x)
                            x -= 1
                        else:
                            break

            elif "[" in d: # Check if data is a valid list
                if d != "[]":  # make sure list not empty
                    x = [i for i, item in enumerate(jd_list) if "]" in item]

                    start = jd_list.index(d)
                    end = x[0]

                    sub_data = " ".join(jd_list[start:  end + 1])  # get list value and undo split


                    if "," in sub_data: # split and loop if multiple list items
                        sub_list = sub_data[1:-1].split(",")
                        for sub_d in sub_list:
                            if not are_key_value_valid(d):
                                return False
                    else:
                       if not are_key_value_valid(sub_data[1:-1]):
                            return False

                    while True:
                        if start != end:
                            jd_list.pop(end)
                            end -= 1
                        else:
                            break

            elif not are_key_value_valid(d):
                return False

    return is_valid


def main():

    data_list = sys.argv[1]
    if is_valid_json(data_list):
        print(0, end=" ")
        data_list = clean_data(data_list)
        data_list = convert_to_dict(data_list)
        data_list = convert_to_list(data_list)
        data_dict = create_dict(data_list)
        print(data_dict)
    else:
        print(1)




if __name__ == "__main__":

    main()
