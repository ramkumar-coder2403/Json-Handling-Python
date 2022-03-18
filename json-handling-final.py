import json
from numbers import Number
import sys
from os import path

filename = 'Student.json'
empty = {"Students": [], "Marks": []}
listObj = []
new_stu = []

# Check if file exists
if path.isfile(filename) is False:
    with open("Student.json", "w") as outfile:
        json.dump(empty, outfile)
        print('Created')
else:
    print("File Already Exist")

# # Read JSON file
# with open(filename) as fp:
#   listObj = json.load(fp)

# # Verify existing list
# print(listObj)
# print(type(listObj))


def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def write_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)


def new_student():
    try:
        roll_number = int(input("Enter roll number: "))
        stu_details = [{
            "Name": str(input("Enter name: ")),
            "DateOfBirth":  str(input("Enter DateofBirth: ")),
            "PlaceOfBirth":  str(input("Enter PlaceofBirth: ")),
            "Number":  roll_number
        }, {
            "Number": roll_number,
            "English": int(input("Enter English mark: ")),
            "Science": int(input("Enter Science mark: ")),
            "Mathematics": int(input("Enter Mathematics mark: "))
        }]
    except ValueError:
        print('Enter Valid Inputs')
        new_student()
    return stu_details


data = read_json(filename)


def user_index():
    while True:
        print('\tINDEX\t')
        print('===============')
        if len(data['Students']) == 0:
            print('1. Add Student')
            print('0. Exit')
            try:
                opt = int(input("Enter : "))
                if opt == 1:
                    return opt
                    break
                elif opt == 0:
                    sys.exit()
                else:
                    None
            except ValueError:
                print('Enter Valid Menu')
                user_index()
        else:
            print('1. Add Student')
            print('2. Delete Student')
            print('0. Exit')
            try:
                opt = int(input("Enter : "))
                if opt == 1:
                    return opt
                    break
                elif opt == 2:
                    return opt
                    break
                elif opt == 0:
                    sys.exit()
                else:
                    None
            except ValueError:
                print('Enter Valid Menu')
                user_index()


val = user_index()
print('VALLL : ', val)
if val == 1:
    new_stu = new_student()
    data['Students'].append(new_stu[0])
    data['Marks'].append(new_stu[1])
    write_json(filename, data)
    print('Student data Successfully Added')
elif val == 2:
    print('Delete Option Not Implemented.')
    # print(len(data['Students']))
    # new_stu = new_student()

    # data['O_data'].append(stuff)

    # write_json('file.json', data)
