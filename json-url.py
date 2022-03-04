import requests

r = requests.get("https://api.npoint.io/53141e20efcc35709569")
data = r.json()

tot = 0

print('\n')
print("Serial number", "\t", "Student name", "\t", "Student number")
print("==============", "\t", "============", "\t", "==============")

for i in range(len(data['Students'])):
    print(i+1, "\t\t", data['Students'][i]['Name'],
          "\t\t", data['Students'][i]['Number'])

while True:
    val = input(
        "Enter the Serial Number for more details or type exit to quit: ")
    try:
        n_val = int(val)
        if n_val == 0 or n_val > len(data['Students']):
            None
        else:
            print('\n')
            print("Name of the Student : ",
                  data['Students'][n_val-1]['Name'], '\n')

            print("Serial number", "\t", "Subject",
                  "\t", "Mark", "\t", "Status")
            print("==============================================")

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

                        print(list(data['Marks'][j]).index(key), "\t\t", key, "\t",
                              data['Marks'][j][key], "\t", sts)

            print("==============================================")
            print('Total', "\t\t\t\t", tot)
            print("==============================================")
            tot = 0
    except ValueError:
        if val == 'exit':
            # sys.exit()
            break
        else:
            None
