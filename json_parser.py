import sys

def clean_data(data):
    return ((data
             .replace(":", "")
             .replace(",", "")
             .replace('"', "")
             .replace("{", ""))
             .replace("}", ""))

def check_if_is_valid(data):
    data = clean_data(data)

    if data in {'true', 'false', 'null'}:
        return True

    return True if data.isdigit() else False


def is_valid_json(data):
    isValid = False
    data = data.strip() # Removed extra spaces

    if data == "": # check if file empty
        isValid = False
    elif data[0] == "{" and data[-1] == "}":
        d_list = data[1:-1].split() # Remove curly braces and create list

        if not d_list: # if file empty json return true
            return True

        for index, d in enumerate(d_list):
            l = len(d)

            if d[:1] != '"': #checks to see if key value pair start with double quotes
                isValid = False

                if index % 2 != 0: # Handle values that are not string literals
                    # if data is a valid type boolean, null, int
                    if check_if_is_valid(d):
                        if len(d_list) - 1 != index and d[-1] == ",": # Verify json format
                            isValid = True
                            continue
                        elif len(d_list) - 1 == index:
                            isValid = True
                            continue

                if not isValid:
                    break

            if index % 2 == 0: # Check key format
                if  d[l-2:l] == '":':
                    isValid = True
                else:
                    isValid = False
                    break
            else: # Check value format
                if index == len(d_list) -1 and d[-1] == '"':  # if last item no comma
                    isValid = True
                elif index != len(d_list) -1 and d[l-2:l] == '",': # if not last item check for comma
                    isValid = True
                else:
                    isValid = False
                    break

    return isValid

def parse_json_to_dictionary(data):

    if data.strip() == "{}":
        return dict()

    json_dict = dict()
    data_list = clean_data(data[1:-1]).split()

    for index, d in  enumerate(data_list):
        if index % 2 == 0:
            continue

        key = data_list[index-1].strip()
        value = d.strip()

        value = int(value) if value.isdigit() else value # is digit needs to get checked first
        value = True if value == 'true' else value
        value = False if value == 'false' else value
        value = None if value == 'null' else value

        json_dict[key] = value

    return json_dict

def main():

    json_file = sys.argv[1]

    with open(json_file, 'r') as f:
        json_data = f.read()

        if not is_valid_json(json_data):
            print(1)
        else:
            print(0)
            print(parse_json_to_dictionary(json_data))

if __name__ == "__main__":

    main()
