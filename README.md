## Run program
 - Start virtaual env
 - Run pytest

 ```bash
 pytest
 ```



## Done 
Challenge completed using json

```python
def easy_parse_json(file_name):
    
    try:
        with open(file_name, 'r') as test_file:
            data_dict = json.load(test_file)
    except json.JSONDecodeError:
        print("Invalid Json")
        sys.exit(1)

    print(f'Valid Json: {data_dict}')
    sys.exit(0)
```
---------------------
# Doing Challenge without using json

## Step 1
- In this step your goal is to parse a valid simple JSON object, specifically: 
‘{}’ and an invalid JSON file and correctly report which is which. So you should 
build a very simple lexer and parser for this step. 

- Your program should report to the standard output stream a suitable message 
and exit with the code 0 for valid and 1 for invalid. It is conventional for CLI 
tools to return 0 for success and between 1 and 255 for an error and allows us to 
combined CLI tools to create more powerful programs. Check out write your own wc 
tool for more on combing simple cli tools. 

- You can test your code against the files in the folder tests/step1. 
Consider automating the tests so you can run them repeatedly as you progress 
through the challenge.

```python
def hard_parse_json(file_name):

    with open(file_name, 'r') as test_file:
        data = test_file.read()

    data = data.strip()

    if not data:
        sys.exit(1)

    valid_json = data[0] + data[-1]
       
    if valid_json != '{}':
        sys.exit(1)


    sys.exit(0)

def main():

    file_name = sys.argv[1]
    # Easy mode
    # easy_parse_json(file_name)
    # Hard mode
    hard_parse_json(file_name)
```

## Step 2
In this step your goal is to extend the parser to parse a simple JSON object containing string keys and string values, i.e.:
```json
{"key": "value"}
```
You can test against the files in the folder tests/step2.

## Done
```python
def split_data(data):
    parts_list = data.split(',')
    return parts_list

def is_valid_key(key_list):
    for key in key_list:
        if key.count('"') != 2:
            return False
    return True

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

    data_dict = {
        key.strip():value.strip()
        for key,value in (d.split(':', 1) for d in data_list)
    }

    if not is_valid_key([d for d in data_dict]):
        sys.exit(1)

    sys.exit(0)

def main():

    file_name = sys.argv[1]
    # Easy mode
    # easy_parse_json(file_name)
    # Hard mode
    hard_parse_json(file_name)
```

## Step 3
In this step your goal is to extend the parser to parse a JSON object containing string, numeric, boolean and null values, i.e.:

```json
{
  "key1": true,
  "key2": false,
  "key3": null,
  "key4": "value",
  "key5": 101
}
```
You can test against the files in the folder tests/step3.

## Done
```python
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
        if value[0] in '[{' and value[-1] in ']}':
            continue
        elif value in ['true', 'false', 'null']:
            continue
        elif value.isdigit():
            continue
        elif value.count('"') == 2:
            continue
        else:
            is_True = False

    return is_True

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

    data_dict = {
        key.strip():value.strip()
        for key,value in (d.split(':', 1) for d in data_list)
    }

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
```

## Step 4
In this step your goal is to extend the parser to parse a JSON object with object and array values, i.e.:
```json
{
  "key": "value",
  "key-n": 101,
  "key-o": {},
  "key-l": []
}
```

You can test against the files in the folder tests/step4.

## Done
```python
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
```

## Step 5
Pass all 36 test scenarios in test/ folder

## Done
```python

```