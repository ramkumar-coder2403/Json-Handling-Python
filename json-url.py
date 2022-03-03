import requests
import sys


r = requests.get("https://api.npoint.io/53141e20efcc35709569")
data = r.json()

# data = json.load(f)

print('\n')
print("Serial number", "\t", "Student name", "\t", "Student number")
print("==============", "\t", "============", "\t", "==============")
idx = 0
sl = 0
tot = 0
for i in range(len(data['Students'])):
    idx += 1
    print(idx, "\t\t", data['Students'][i]['Name'],
          "\t\t", data['Students'][i]['Number'])

while True:
    val = input(
        "Enter the Serial Number for more details or type exit to quit: ")
    try:
        n_val = int(val)
        if n_val == 0 or n_val > idx:
            None
        else:
            break
    except ValueError:
        if val == 'exit':
            sys.exit()
        else:
            None
print('\n')
print("Name of the Student : ", data['Students'][n_val-1]['Name'], '\n')

print("Serial number", "\t", "Subject", "\t", "Mark", "\t", "Status")
print("==============================================")

for j in range(len(data['Marks'])):
    if data['Students'][n_val-1]['Number'] == data['Marks'][j]['Number']:
        for key in data['Marks'][j]:
            if key == 'Number':
                continue
            sl += 1
            tot += int(data['Marks'][j][key])
            if int(data['Marks'][j][key]) < 35:
                sts = 'fail'
            else:
                sts = 'pass'

            print(sl, "\t\t", key, "\t", data['Marks'][j][key], "\t", sts)

print("==============================================")
print('Total', "\t\t\t\t", tot)
print("==============================================")
