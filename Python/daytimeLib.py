import datetime

time = datetime.date.today()
print(time)
print(datetime.datetime.now())


import os
#getcwd : Current working directory
current_dir = os.getcwd()

print(current_dir)


import json

data = {'ganesh':23, 'hari':24, 'kamlesh':90}

json_string = json.dumps(data)

print(json_string)