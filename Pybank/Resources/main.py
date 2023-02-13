import os # operating system
import csv # import module for csv file 

# to store file path 
csvFilePath= os.path.join ("..", "Resources","budget_data.csv")
# to read file using open command
with open (csvFilePath,'r') as csvFile:
    # to set up reader for the csv file 
    csvReader=csv.reader(csvFile,delimiter=",")
    # to store header
    header=next(csvReader)
    # to print Financial Analysis onto the terminal
    print("Financial Analysis")
    print("--------------------------")

    # accumulator for total number of months, net total, and average of the changes in "profit/losses"
    totalMonths=0
    total=0
    average=0
    # declaring variables to hold the max
    greatest=[" ", 0]
    smallest=[" ", 0]
    # list for the changes in "Profit/Losses"
    changeList=[]

    # for each row in the csv file 
    for row in csvReader:
        # adds to the total months count
        totalMonths= totalMonths + 1
        # adds to the total net profit/loss count
        total=total + int(row[1])
        # since our first month does not have a previous profit/loss
        if totalMonths !=1:
            # calculates the change of profit/losses over the entire period
            change=int(row[1])-previous
            # adds the value to the change list
            changeList.append(change)
            # if the greatest increase in profits is greater than our current greatest increase of 0, then update our greatest increase
            if change>greatest[1]:
                greatest=[row[0], change]
            # if the greatest decrease in profits is smaller than our current greatest decrease of 0, then update our greatest decrease
            elif change<smallest[1]:
                smallest=[row[0],change]

        previous=int(row[1]) # variable to declare what the previous profit/loss change was 
        

average= sum(changeList)/(len(changeList)) # to find the average of the changes in "profit/losses"

# printing the results to the terminal 
print(f"Total Months: {totalMonths}")
print(f"Total: ${total}")
print(f"Average Change= ${average:.2f}")
print(f"The Greatest Increase In Profits: {greatest[0]} (${greatest[1]})")
print(f"The Greatest Decrease In Profits: {smallest[0]} (${smallest[1]})")

# write the results to the txt.file
outputFilePath=os.path.join("..","Analysis","output.txt")
with open(outputFilePath,"w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------\n") 
    txtfile.write(f"Total Months: {totalMonths}\n")  
    txtfile.write(f"Total: ${total}\n")
    txtfile.write(f"Average Change= ${average:.2f}\n")
    txtfile.write(f"The Greatest Increase In Profits: {greatest[0]} (${greatest[1]})\n")
    txtfile.write(f"The Greatest Decrease In Profits: {smallest[0]} (${smallest[1]})\n")




