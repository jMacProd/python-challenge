import os
import csv

clTest = []



csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# skip the first line as it contains the headers
    next(csvreader, None)
        
    for row in csvreader:

        clTest.append(row[2])

colors_dict = {}
#for c in range(len(clTest)):
#for c in clTest:
#    colors_dict[clTest[c]] = clTest.count(
#        clTest[c]
#        )

for name in candida


colors_dict[1] = [5]

print(colors_dict)

