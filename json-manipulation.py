import json
import sys
from os import path

# initialize/declaration part
filename = 'Student.json'
empty = {"Students": [], "Marks": []}
listObj = []
new_stu = []

# Check if file exists
if path.isfile(filename) is False:
    with open("Student.json", "w") as outfile:
        json.dump(empty, outfile)
else:
    try:
        with open(filename, 'r') as f:
            data=json.load(f)
            len(data['Students'])
    except:
        with open(filename, "w") as outfile:
            json.dump(empty, outfile)


def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def write_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


# Read JSON file
data = read_json(filename)


def view_all_rec():
    print("{:<8} {:<25} {:<10}".format(
        'S.No', 'Student name', 'Student number'))
    print("{:<8} {:<25} {:<10}".format(
        '====', '============', '=============='))
    for i in range(len(data['Students'])):
        print("{:<8} {:<25} {:<10}".format(
            i+1, data['Students'][i]['Name'], data['Students'][i]['Number']))
    print('_________________________________________________')
    while True:
        val = input(
            "Enter the S.No for more details or type exit to Main menu: ")
        try:
            n_val = int(val)
            if n_val == 0 or n_val > len(data['Students']):
                None
            else:
                break
        except ValueError:
            if val.lower().replace(" ", "") == 'exit':
                main()
            else:
                None
    print('_________________________________________________')
    view_rec_by_id(n_val)


def view_rec_by_id(n_val):
    tot = 0
    print("Name of the Student : ",
          data['Students'][n_val-1]['Name'], '\n')
    print("{:<8} {:<25} {:<10} {:<10}".format(
        'S.No', 'Subject', 'Mark', 'Status'))
    print("{:<8} {:<25} {:<10} {:<10}".format(
        '====', '=======', '====', '======'))

    for j in range(len(data['Marks'])):
        if data['Students'][n_val-1]['Number'] == data['Marks'][j]['Number']:
            for key in data['Marks'][j]:
                if key == 'Number':
                    continue
                tot += int(data['Marks'][j][key])
                if int(data['Marks'][j][key]) < 35:
                    sts = 'fail'
                else:
                    sts = 'pass'

                print("{:<8} {:<25} {:<10} {:<10}".format(
                    list(data['Marks'][j]).index(key), key, data['Marks'][j][key], sts))
                # print(list(data['Marks'][j]).index(key), "\t\t", key, "\t",
                #       data['Marks'][j][key], "\t", sts)

    print("===================================================")
    print("{:<10} {:>27}".format('TOTAL', tot))
    print("===================================================")
    while True:
        choice = input(
            "Do you want see other details?: yes/no ")
        if choice.lower().replace(" ", "") == 'yes':
            view_all_rec()
        elif choice.lower().replace(" ", "") == 'no':
            break
    main()


def chk_student_byID(roll_number):
    for i in range(len(data['Students'])):
        if data['Students'][i]['Number'] == roll_number:
            return True
    return False


def new_student():
    while True:
        try:
            roll_number = input("Enter roll number: ")
            int(roll_number)

            chk_roll = chk_student_byID(roll_number)
            if chk_roll == False:
                stu_details = [{
                    "Name": str(input("Enter name: ")),
                    "DateOfBirth":  str(input("Enter DOB(dd-mm-yyyy): ")),
                    "PlaceOfBirth":  str(input("Enter PlaceOfBirth: ")),
                    "Number":  roll_number
                }, {
                    "Number": roll_number,
                    "English": int(input("Enter English mark: ")),
                    "Science": int(input("Enter Science mark: ")),
                    "Mathematics": int(input("Enter Mathematics mark: "))
                }]
                break
            else:
                print('STUDENT RECORD ALREADY FOUND.')
                None
        except ValueError:
            print('***ENTER VALID DETAILS***')
            print('_________________________________________________')
            None
    return stu_details


def delete_student(roll_num):
    for i in range(len(data['Students'])):
        if data['Students'][i]['Number'] == roll_num:
            del data['Students'][i]
            break
    for j in range(len(data['Marks'])):
        if data['Marks'][j]['Number'] == roll_num:
            del data['Marks'][j]
            write_json(filename, data)
            return True
    return False


def index_main():
    while True:
        print('\t\tINDEX\t\n=============================')
        print(
            '1. View All Records\n2. Add new Student\n3. Delete existing Student\n0. Exit')
        print('=============================')
        try:
            opt = int(input("Enter Option : "))
            if opt == 1 or opt == 2 or opt == 3:
                return opt
            elif opt == 0:
                sys.exit()
            else:
                None
        except ValueError:
            print('***ENTER VALID MENU OPTION***')


# FUNCTION CALL
def main():
    while True:
        val = index_main()
        if val == 1:
            if len(data['Students']) == 0:
                print('_________________________________________________')
                print('STUDENT RECORDS NOT FOUND.')
            else:
                view_all_rec()
        elif val == 2:
            new_stu = new_student()
            data['Students'].append(new_stu[0])
            data['Marks'].append(new_stu[1])
            write_json(filename, data)
            print('_________________________________________________')
            print('STUDENT RECORD ADDED SUCCESSFULLY.')

            None
        elif val == 3:
            while True:
                try:
                    roll_num = input("Roll Num : ")
                    int(roll_num)
                    if delete_student(roll_num):
                        print('_________________________________________________')
                        print('STUDENT RECORD DELETED SUCCESSFULLY.')

                    else:
                        print('STUDENT RECORD NOT FOUND.')
                    break
                except ValueError:
                    print('***ENTER VALID ROLL NUMBER***')
                    None


main()
