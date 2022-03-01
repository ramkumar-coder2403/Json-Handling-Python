import json

# Opening JSON file
f = open('./data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
# print(tabulate(headers=[table, 'Serial Number',
#   'Student Name', 'Student Name']))

# table = []

print("\Serial Number", "\t", "Student Name", "\t", "Student Number")
print("-----------", "\t", "------------", "\t", "-------------")
# for cels in range(70, 280, 10):

#     fahr = 1.8 * cels + 32
#     print(cels, "\t\t", fahr)

idx = 0
for i in range(len(data['Students'])):
    idx += 1
    print(idx, "\t\t", data['Students'][i]['Name'],
          "\t\t", data['Students'][i]['Number'])


val = int(input("Enter your value: "))
if val > idx | val == 0:
    print("Number Not Valid!")
else:
    print("English", "\t", "Science", "\t", "Maths")
    print("-----------", "\t", "------------", "\t", "-------------")

for j in range(len(data['Marks'])):
    if data['Students'][val-1]['Number'] == data['Marks'][j]['Number']:
        print(data['Marks'][j]['English'], "\t\t", data['Marks'][j]['Science'],
          "\t\t", data['Marks'][j]['Maths'])


# Closing file
f.close()
