import os
import csv

voterlist = []
candidatelist = []
uniquename = []

#defining a function that can be used in the loop?
def candidate():
    for name in candidatelist:
        if name not in uniquename:
            uniquename.append(name)

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# skip the first line as it contains the headers
    next(csvreader, None)
        
    for row in csvreader:

        #The total number of votes cast
        #len(row)
        voterlist.append(row[0])

        #A complete list of candidates who received votes
        #https://www.geeksforgeeks.org/python-get-unique-values-list/
        candidatelist.append(row[2])

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.

print(candidatelist)
#print(candidate())

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {str(len(voterlist))}") #3521001
print(f"-------------------------")
#print(f"Khan: 63.000% (2218231)")
#print(f"Correy: 20.000% (704200)")
#print(f"Li: 14.000% (492940)")
#print(f"O'Tooley: 3.000% (105630)")
#print(f"-------------------------")
#print(f"Winner: Khan")
#print(f"-------------------------")