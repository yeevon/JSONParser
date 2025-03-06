import sys

def main():
    json_file = sys.argv[1]

    with open(json_file, 'r') as f:
        json_data = f.read()

        if json_data == "":
            print(1)
        elif json_data[0] == "{" and json_data[-1] == "}":
            print(0)
        else:
            print(1)


if __name__ == "__main__":

    main()
