import sys, json

def easy_parse_json(file_name):
    
    try:
        with open(file_name, 'r') as test_file:
            data_dict = json.load(test_file)
    except json.JSONDecodeError:
        print("Invalid Json")
        sys.exit(1)

    print(f'Valid Json: {data_dict}')
    sys.exit(0)


def split_data(data):
    parts_list = data.split(',')
    return parts_list

def is_valid_key(key_list):
    for key in key_list:
        if key.count('"') != 2:
            return False
    return True

def is_valid_value(value_list):
    is_True = True
    for value in value_list:
        value = value.strip()
        if value in ['[]', '{}']:
            continue
        elif value[0] in '[' and value[-1] in ']':
            if not is_valid_value([value[1:-1]]):
                is_True = False
        elif value[0] in '{' and value[-1] in '}':
            new_dict = convert_to_dict([value[1:-1].strip()])
            if not is_valid_key(new_dict.keys()) and not is_valid_value(new_dict.values()):
                is_True = False
        elif value in ['true', 'false', 'null']:
            continue
        elif value.isdigit():
            continue
        elif value.count('"') == 2:
            continue
        else:
            is_True = False

    return is_True

def convert_to_dict(data):
    return {
        key.strip():value.strip()
        for key,value in (d.split(':', 1) for d in data)
    }

def hard_parse_json(file_name):

    with open(file_name, 'r') as test_file:
        data = test_file.read()

    data = data.strip()


    # Make sure there is data
    if not data:
        sys.exit(1)
    elif data == '{}':
        sys.exit(0)

    valid_json = data[0] + data[-1]
       
    if valid_json != '{}':
        sys.exit(1)

    data = data[1:-1]
    data_list = split_data(data)


    for d in data_list:
        if not d:
            sys.exit(1)

        if ':' not in d:
            sys.exit(1)

    data_dict = convert_to_dict(data_list)

    if not is_valid_key(data_dict.keys()):
        sys.exit(1)

    if not is_valid_value(data_dict.values()):
        sys.exit(1)

    sys.exit(0)

def main():

    file_name = sys.argv[1]
    # Easy mode
    # easy_parse_json(file_name)
    # Hard mode
    hard_parse_json(file_name)
if __name__ == "__main__":
    main()
