import os
import csv

voterlist = []
candidatelist = []
clTest = []
#uniquename = []


#defining a function that can be used in the loop?
#def candidate():
#    for name in candidatelist:
#        if name not in uniquename:
#            uniquename.append(name)

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# skip the first line as it contains the headers
    next(csvreader, None)
        
    for row in csvreader:

        #The total number of votes cast
        #len(row)
        voterlist.append(row[0])

        clTest.append(row[2])

        #A complete list of candidates who received votes
        #https://www.geeksforgeeks.org/python-get-unique-values-list/
        if row[2] not in candidatelist: candidatelist.append(row[2])

        

   
#        votecountdict = {}
#        for name in candidatelist:
#            votecountdict[name] = 1
#                if name = row(2):
#                    len(row2)
#                else:
#                    0)
        
            
        #for candidate in candidatelist:
            #if row[2] == candidate: khan = khan + 1
            #votecountdict = {candidate:if row[2] = candidate: }
         #   name + candidate = []
          #  votecountdict = {candidate:(if row[2] == candidate):2}
        


#https://www.tutorialspoint.com/counting-the-frequencies-in-a-list-using-dictionary-in-python
votecountdict = {}
for item in clTest:
    if (item in votecountdict):
        votecountdict[item] += 1
    else:
        votecountdict[item] = 1
#for key, value in votecountdict.items():
#    print("% s -> % d" % (key, value))


#print(candidatelist) 
#print(votecountdict)
 #   candidate()
 #   print(khan)


#The percentage of votes each candidate won val

percentage  = []

for x in votecountdict:
    percentage.append(votecountdict[x] / len(voterlist))

#print(percentage)



#The winner of the election based on popular vote.
winner = max(votecountdict, key=votecountdict.get) 




print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {str(len(voterlist))}") #3521001
print(f"-------------------------")
#print(f"{votecountdict[0]}: {percentage[0]}% ({votecountdict[0]})")
#print(f"Correy: 20.000% (704200)")
#print(f"Li: 14.000% (492940)")
#print(f"O'Tooley: 3.000% (105630)")
#print(f"-------------------------")
print(f"Winner: {winner}")
#print(f"-------------------------")