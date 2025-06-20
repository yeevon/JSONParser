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

def in_string_switch(bool_val):
    return False if bool_val else True

def split_data(data, split_val):
    char_collector = ''
    data_list = []
    depth = 0
    in_string = False
    data_dict = {}
    key = "" 

    if split_val == ',':
        for _char in data:

            if depth > 18:
                sys.exit(1)

            if _char in '{[':
                depth += 1
            elif _char in ']}':
                depth -= 1

            if _char == '"':
                in_string = in_string_switch(in_string)

            if _char == split_val and depth == 0 and not in_string:
                data_list.append(char_collector)
                char_collector = ""
            else:
                if _char:
                    char_collector += _char

        data_list.append(char_collector)

        return data_list
    else:
        for _char in data:

            if _char in '{[':
                depth += 1
            elif _char in ']}':
                depth -= 1

            if _char == '"':
                in_string = in_string_switch(in_string)

            if _char == split_val and depth == 0 and not in_string:
                if split_val == ':':
                    key = char_collector
                    split_val = ','
                else:
                    split_val = ':'
                    data_dict[key] = char_collector
                char_collector = ""
            else:
                if _char:
                    char_collector += _char

        data_dict[key] = char_collector
        return data_dict

def is_valid_key(key_list):
    for key in key_list:
        if key == '0' or key.isdigit():
            continue

        if key.count('"') != 2:
            return False
        
    return True

def is_valid_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def is_valid_value(value_list):
    is_True = True
    for value in value_list:
        value = value.strip()

        if ':' in value:
            print(12)
            if '{' not in value and '}' not in value:
                return False
            
        if value in ['[]', '{}']:
            print(5)
            continue
        elif value[0] in '[' and value[-1] in ']':
            print(6)
            if not is_valid_value(split_data(value[1:-1])):
                is_True = False
        elif value[0] in '{' and value[-1] in '}':
            print(7)
            if ',' in value:
                hard_parse_json(value.strip())
            else:
                new_dict = convert_to_dict([value.strip()])
                if not is_valid_key(new_dict.keys()) or not is_valid_value(new_dict.values()):
                    is_True = False
        elif value in ['true', 'false', 'null']:
            print(8)
            continue
        elif value == 0 or (not value.startswith('0') and (value.isdigit() or is_valid_int(value))):
            print(9)
            continue
        elif value.count('"') == 2:
            print(10)
            continue
        else:
            print(11)
            is_True = False

    return is_True

def convert_to_dict(data):
    return {
        key.strip():value.strip()
        for key,value in (d.split(':', 1) for d in data)
    }

def hard_parse_json(file_or_data):

    if file_or_data.strip().startswith('{') or file_or_data.strip().startswith('['):
        data = file_or_data
    else:
        with open(file_or_data, 'r') as test_file:
            data = test_file.read()

    data = data.strip()

    # Make sure there is data
    if not data:
        print(1)
        sys.exit(1)
    elif data == '{}':
        sys.exit(0)

    valid_json = data[0] + data[-1]
    
    if valid_json not in ['{}', '[]']:
        print(2)
        sys.exit(1)
    
    if valid_json == '[]':
        if is_valid_value([data]):
            sys.exit(0)
        else:
            sys.exit(1)

    data = data[1:-1]
    data_list = list(split_data(data))

    for d in data_list:
        if not d or not (':' in d) :
            print(3)
            sys.exit(1)

    data_dict = convert_to_dict(data_list)
    print(data_dict)
    print("<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(is_valid_key(data_dict.keys()))
    if not is_valid_key(data_dict.keys()) or not is_valid_value(data_dict.values()):
        print(4)
        sys.exit(1)

    sys.exit(0)

def main():

    file_name = sys.argv[1]
    print(file_name)
    # Easy mode
    # easy_parse_json(file_name)
    # Hard mode
    hard_parse_json(file_name)

if __name__ == "__main__":
    main()
