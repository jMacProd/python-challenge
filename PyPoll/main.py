import os
import csv

voterlist = []
candidatelist = []
clTest = []

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# skip the first line as it contains the headers
    next(csvreader, None)
        
    for row in csvreader:

        #The full list of votes cast - allows for a len count
        voterlist.append(row[0])

        #The full list of everytime a candidate is voted for - allows for a count of each candidate
        clTest.append(row[2])

        #A unique list of candidates who received votes
        #https://www.geeksforgeeks.org/python-get-unique-values-list/
        if row[2] not in candidatelist: candidatelist.append(row[2])


#To tally each candidates' votes
#https://www.tutorialspoint.com/counting-the-frequencies-in-a-list-using-dictionary-in-python
votecountdict = {}
for item in clTest:
    if (item in votecountdict):
        votecountdict[item] += 1
    else:
        votecountdict[item] = 1

#Create a list for the percentage of votes each candidate won
percentage  = []

for x in votecountdict:
    percentage.append(votecountdict[x] / len(voterlist))


#To call each value to print, they need to be in individual lists
#split dictionary into list



VCD_keys = votecountdict.keys() 
VCD_values = votecountdict.values()

#zip 3 lists and convert to list
zipped = zip(VCD_keys, VCD_values, percentage)
zipped_list = list(zipped)


#The winner of the election based on popular vote.
winner = max(votecountdict, key=votecountdict.get) 


#Need to create loop to allow each value to be printed separately in candidate tally summary

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {str(len(voterlist))}")
print(f"-------------------------")
for z in zipped_list:
   print(str(z[0]) + ": " + str('{:.3%}'. format(z[2])) + " (" + str(z[1]) + ")")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

#Export to textfile
output_path = os.path.join("Analysis", "PyPollAnalysis.txt")

with open(output_path, "w") as textfile:
    textfile.write(f"Election Results\n")
    textfile.write(f"-------------------------\n")
    textfile.write(f"Total Votes: {str(len(voterlist))}\n")
    textfile.write(f"-------------------------\n")
    for z in zipped_list:
        textfile.write(str(z[0]) + ": " + str('{:.3%}'. format(z[2])) + " (" + str(z[1]) + ")\n")
    textfile.write(f"-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write(f"-------------------------\n")