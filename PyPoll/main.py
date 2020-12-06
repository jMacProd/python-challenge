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
        
            
        #for candidate in candidatelist:
            #if row[2] == candidate: khan = khan + 1
            #votecountdict = {candidate:if row[2] = candidate: }
         #   name + candidate = []
          #  votecountdict = {candidate:(if row[2] == candidate):2}
        
        

        
        
        #The total number of votes each candidate won
        #I think I need to create a dictionary - set key:0
        #monthchangedict = {monthlist[i+1]: valuelistdiff[i] for i in range(len(monthlist)-1)} 
        #votercountdict = {"khan":(if row[2]thenlist1)}}
        
        #for name

        
        #if row[2] == "Khan": khan = khan + 1

       

#The percentage of votes each candidate won "uniquecount/voterlist"



#The winner of the election based on popular vote.

#def CountFrequency(my_list): 
#    votecountdict = {}
#    for item in my_list:
#        if item in votecountdict:
#            votecountdict[item] += 1
#        else
#            votecountdict[item] = 1
#
#    for key, value in votecountdict.items():



votecountdict = {}

for c in range(len(clTest)):
    votecountdict[clTest[c]] = clTest.count(
        clTest[c]
    )


#print(candidatelist) 
print(votecountdict)
 #   candidate()
 #   print(khan)


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