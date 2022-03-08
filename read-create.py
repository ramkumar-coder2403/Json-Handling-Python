import requests
import json

# READ JSON DATA
r = requests.get("https://api.npoint.io/4eacf98e7fde073a4cea")
data = r.json()
data = str(data)
print(type(data))


# CONVERT USER STRING TO JSON
lst = []
u_in = 0
while True:
    u_in = u_in+1
    print('Enter Input ', u_in, ' : ')
    val = input("")
    lst.append(val)
    if u_in == 3:
        break

jsonlist = [{'data1': lst[0]}, {'data2': lst[1]}, {'data3': lst[2]}]
jsonString = json.dumps(jsonlist, indent=4)
print(jsonString)
