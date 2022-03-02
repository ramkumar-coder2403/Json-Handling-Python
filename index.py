import json

# Opening JSON file
f = open('data.json')

# returns JSON object as
# a dictionary
data = json.load(f)


print("\Serial Number", "\t", "Student Name", "\t", "Student Number")
print("-----------", "\t", "------------", "\t", "-------------")

idx = 0
for i in range(len(data['Students'])):
    idx += 1
    print(idx, "\t\t", data['Students'][i]['Name'],
          "\t\t", data['Students'][i]['Number'])


while True:
    try:
        val = int(input("Enter Valid number: "))
        if val == 0 or val > idx:
            None
        else:
            break
    except ValueError:
        None

print("English", "\t", "Science", "\t", "Maths")
print("-----------", "\t", "------------", "\t", "-------------")

for j in range(len(data['Marks'])):
    if data['Students'][val-1]['Number'] == data['Marks'][j]['Number']:
        print(data['Marks'][j]['English'], "\t\t", data['Marks'][j]['Science'],
              "\t\t", data['Marks'][j]['Maths'])

# Closing file
f.close()
