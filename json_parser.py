import sys

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

            if d[:1] != '"':
                isValid = False
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
    clean_data_list = ((data[1:-1]
                       .replace(":", "")
                       .replace(",", "")
                       .replace('"', "")
                       .replace("{", ""))
                       .replace("}", "")
                       .split())

    for index, d in  enumerate(clean_data_list):
        if index % 2 == 0:
            continue

        key = clean_data_list[index-1].strip()
        json_dict[key] = d.strip()

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
