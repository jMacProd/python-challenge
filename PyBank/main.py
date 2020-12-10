import os
import csv
import statistics

monthlist = []
nettotal = 0
valuelist = []

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# skip the first line as it contains the headers
    next(csvreader, None)

    for row in csvreader:
        
        #Total number of months = count the rows - Len
        #create list of months
        monthlist.append(row[0])
        
        #net total amount of "Profit/Losses = progressive accumulation
        #So create variable total = 0 and add to variable
        nettotal = nettotal + int(row[1])

        #Create list of value changes - don't include first cell
        #Create a list of values then do (item 2 - 1)
        valuelist.append(row[1])


#for change in valuelist - needs to be after for loop and no longer in open file :
#https://stackoverflow.com/questions/7172933/calculate-difference-between-adjacent-items-in-a-python-list
valuelistdiff = [int(valuelist[n])-int(valuelist[n-1]) for n in range(1,len(valuelist))]

#average of the changes in "Profit/Losses"
#https://careerkarma.com/blog/python-average/#:~:text=We%20can%20find%20the%20average,the%20Python%20mean()%20function. 
average = statistics.mean(valuelistdiff)

#Create a dictionary of month:change
#https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/
#Need to create not include first month on list
monthchangedict = {monthlist[i+1]: valuelistdiff[i] for i in range(len(monthlist)-1)} 

#find max value in dictionary and return key
#https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/
greatestincreasekey = max(monthchangedict, key=monthchangedict.get) 
greatestincreasevalue = max(valuelistdiff)

#find min value in dictinary and return key
greatestdecreasekey = min(monthchangedict, key=monthchangedict.get) 
greatestdecreasevalue = min(valuelistdiff)

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {str(len(monthlist))}")
print(f"Total: ${str(nettotal)}")
print(f"Average  Change: ${round(average, 2)}")
print(f"Greatest Increase in Profits: {greatestincreasekey} (${greatestincreasevalue}) ")
print(f"Greatest Decrease in Profits: {greatestdecreasekey} (${greatestdecreasevalue}) ")

#Export to textfile
output_path = os.path.join("Analysis", "PyBankAnalysis.txt")

with open(output_path, "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write(f"----------------------------\n")
    textfile.write(f"Total Months: {str(len(monthlist))}\n")
    textfile.write(f"Total: ${str(nettotal)}\n")
    textfile.write(f"Average  Change: ${round(average, 2)}\n")
    textfile.write(f"Greatest Increase in Profits: {greatestincreasekey} (${greatestincreasevalue})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatestdecreasekey} (${greatestdecreasevalue})\n")
    

