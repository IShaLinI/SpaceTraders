#Merge all of the page files into a single file

import json

data = []

for i in range(1, 251):
    with open("data/systems/page" + str(i) + ".json") as json_file:
        jsonData = json.load(json_file)
        for i in range(0, len(jsonData['data'])):
            data.append(jsonData['data'][i])

with open("data/systems.json", 'w') as outfile:
    json.dump(data, outfile, indent=4)