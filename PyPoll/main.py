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

#split dictionary into list
#prit both lists to check order
#Print percentage list to check order
#zip 3 lists
#loop to print each value

VCD_keys = votecountdict.keys() 
VCD_values = votecountdict.values()
zipped = zip(VCD_keys, VCD_values, percentage)
zipped_list = list(zipped)

#for z in zipped_list:
#   print(str(z[0]) + ": " + str('{:.3%}'. format(z[2])) + " (" + str(z[1]) + ")")


#The winner of the election based on popular vote.
winner = max(votecountdict, key=votecountdict.get) 



#for key in votecountdict:
#        for figure in percentage:
#            print ("The key name is " + key + ": " + str('{0:.0%}'.format(figure)))

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