file = open('./csv_file.txt', 'r')
lines = file.readlines()
file.close()

lines = [ line.strip() for line in lines ]

clubs = []

for line in lines:
    now = line.split(',')
    clubs.append( {'club': now[0], 'country': now[2], 'city': now[1]} )

import json

result = open('./json_file.txt', 'w')
json.dump(clubs, result)
result.close()
