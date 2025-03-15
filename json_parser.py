import sys

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

def list_value(data_list):

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
def dict_value(data_list):

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




def main():

    data_list = clean_data(sys.argv[1])
    print(data_list)
    data_list = dict_value(data_list)
    data_list = list_value(data_list)
    data_dict = create_dict(data_list)

    print("--------------------------------------------------")
    print(data_dict)





if __name__ == "__main__":

    main()
