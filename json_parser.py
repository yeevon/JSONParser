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

def parse_json(data):

    if len(data) == 2: # empty json file return curly braces
        return data
    else:
        for d in data:
            print(d)

def main():

    json_file = sys.argv[1]

    with open(json_file, 'r') as f:
        json_data = f.read()

        if not is_valid_json(json_data):
            print(0)
        else:
            print(1, "\nworks so far")


if __name__ == "__main__":

    main()
