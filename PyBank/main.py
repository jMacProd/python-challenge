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

    #header = next(csvreader)

    #Total number of months = count the rows - Len
    #create list of months
    for row in csvreader:
        
        #Total number of months = count the rows - Len
            #create list of months
        monthlist.append(row[0])
        
        #net total amount of "Profit/Losses = progressive accumulation
            #So create variable total = 0 and add to variable
        nettotal = nettotal + int(row[1])

        #Create list of value changes - don't include first cell
            #list = (i.2 = (i.2 - 1))
            #I think create a list of values then do item 2 -1
        valuelist.append(row[1])

        #Possibly Zip list of months and list of value changes?

        # greatest increase in profits
            # minimum value = min(List of value changes)
            #how to identify the month it alligns to?

        #greatest decrease in profits
            # minimum value = max(List of value changes) 
#rowcount = len(monthlist)

#for change in valuelist - needs to be after for loop and no longer in open file :
#    I was think this "valuechangelist.append(int(change[1])-int(change[1-1]))"
#   but had to get from stackoveflow https://stackoverflow.com/questions/7172933/calculate-difference-between-adjacent-items-in-a-python-list
valuelistdiff = [int(valuelist[n])-int(valuelist[n-1]) for n in range(1,len(valuelist))]
#print (valuelistdiff)
#print(len(valuelistdiff))

#average of the changes in "Profit/Losses"
# https://careerkarma.com/blog/python-average/#:~:text=We%20can%20find%20the%20average,the%20Python%20mean()%20function. 
        #   "average = statistics.mean(List of value changes)"
average = statistics.mean(valuelistdiff)
#print(round(average, 2))

#create new month list removing the first item
#then create a dictionary of month:change
#find max value in dictionary and return key
#find min value in dictinary and return key
newmlist = monthlist[1, 5]
#newmonthlist.pop(0)
print(newmlist)
#print(len(newmonthlist))




print(f"Financial Analysis")
print(f"  ----------------------------")
print(f"Total Months: {str(len(monthlist))}")
print(f"Total: ${str(nettotal)}")
print(f"Average  Change: ${round(average, 2)}")
#print(f"Greatest Increase in Profits: ")
#print(f"Greatest Decrease in Profits:  ")

#Export to textfile