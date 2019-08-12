import os 
import csv
#total will be used to sum the total number of months
monthtotal = 0
#sumtotal will be the sum of profit/losses over the entire period
sumtotal = 0
#listrows  will be used for storing rows in a list
listrows = []
#mylist2 used for difference and month matching
listrows2 = []
#allmonths is a list of all the months 
allmonths = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
#sum that will be used in calculating average
sum1 = 0
#y will be used as a placeholder
y = 0
csvpath = os.path.join("..","financial_records.csv")

with open(csvpath, newline = "") as csvfile:

    #reads the files
    csvreader = csv.reader(csvfile,delimiter = ",")

    #header will take in the name of the columns in the first row. The cursor is now on the first first row with values that we will work with. 
    header = next(csvreader)

    #loop that runs through csvfile 
    for row in csvreader:

        #add the row to our first list
        listrows.append(row)

        #splitting month-year
        monthyear = row[0]
        month = monthyear.split("-")
        #if statement check if the month is in the list months
        if allmonths.count(month[0]) == 1:
            monthtotal = monthtotal + 1

        #adds up the profits 
        sumtotal = sumtotal + int(row[1])

    #---------------------The average of the changes in "Profit/Losses" over the entire period-----------------------------------------
    for i in range(1,len(listrows)): 
        #taking the difference of the previous "Profit/Losses" to the current "Profit/Losses".
        difference = int(listrows[i][1]) - int(listrows[i-1][1]) 
        #adds up the difference
        sum1 = sum1 + difference 
        #keeps count and will be used in dividing the sum1
        y = y + 1 
        #adds the current month and difference to listrows2
        listrows2.append([listrows[i][0],difference]) 
    #calculate average
    averages = round(sum1/y,2)

    #for loop and if statement that finds the greatest value and the corresponding month 
    maxvalue = listrows2[0][1]
    maxmonth = listrows2[0][0]
    for k in range(1,len(listrows2)):
        if int(listrows2[k][1]) > int(maxvalue):
            maxvalue = listrows2[k][1]
            maxmonth = listrows2[k][0] 

    #for loop and if statement that finds the Greatest Decrease in Profit and the corresponding month
    minvalue = listrows2[0][1]
    minmonth = listrows2[0][0]
    for h in range(1,len(listrows2)):
        if int(listrows2[h][1]) < int(minvalue):
            minvalue = listrows2[h][1]
            minmonth = listrows2[h][0] 

print("Financial Analysis")
print("------------------------------")
print("Total months: ", monthtotal)
print("Total: $",sumtotal)
print("Average Change: $",averages)
print("Greatest Increase in Profits:",maxmonth,"($",maxvalue,")")
print("Greatest Decrease in Profits:",minmonth,"($",minvalue,")")

#Export a text file    
file = "Finacial_Report.txt"
with open(file,'w') as f:
    print("Financial Analysis",file = f)
    print("------------------------------",file = f)
    print("Total months: ", monthtotal,file = f)
    print("Total: $",sumtotal, file = f)
    print("Average Change: $",averages,file = f)
    print("Greatest Increase in Profits:",maxmonth,"($",maxvalue,")",file = f)
    print("Greatest Decrease in Profits:",minmonth,"($",minvalue,")", file = f)

    f.close()
