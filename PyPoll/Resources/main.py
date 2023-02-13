import os # import os module
import csv # import module for csv files
csvFilePath=os.path.join("..","Resources","election_data.csv") # form a path to csv file

# variables to hold total votes, the candidate list, the number of votes
totalVotes=0
candidateList=[]
numberOfVotes={}
# declaring a variable to hold the max for the winning vote percentage and the winning vote count
winningPercentage=0
winningVote=0

# opening the csv file path into an object 
with open (csvFilePath) as csvFile:
    csvReader=csv.reader(csvFile, delimiter=",")
    # to store the header
    header= next(csvReader)
    # printing "Election Results" to terminal
    print("Election Results")
    print("------------------")
    
    # to read each row of data into the csv file 
    for row in csvReader:
        # adds to the total number of votes cast
        totalVotes=totalVotes + 1
        # declaring a variable to hold all the candidate names in the csv file
        candidateNames=row[2]
        # if the candidate names are not in our candidate list, add the candidate names and count for the number of votes for each candidate  
        if candidateNames not in candidateList:
            candidateList.append(candidateNames)
            numberOfVotes[candidateNames]=0
        numberOfVotes[candidateNames]=numberOfVotes[candidateNames] + 1
# print the number of total votes to terminal 
print(f"Total Votes: {totalVotes}")
print("------------------")

# writing "election results" and total number of votes cast to the txt file
outputFilePath=os.path.join("..","Analysis","output.txt")
with open(outputFilePath,"w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("------------------\n") 
    txtfile.write(f"Total Votes: {totalVotes}\n")  
    txtfile.write ("------------------\n")
    
    # to find the percentage of votes for each candidate 
    for candidateNames in numberOfVotes:
        votes=numberOfVotes[candidateNames]
        votePercentage=float(votes)/float(totalVotes)*100
        # printing the candidate name and percentage of votes for that candidate into terminal
        print(f"{candidateNames}: {votePercentage:.3f}% ({votes:})")
        # printing the candidate name, percentage of votes, and number of votes for that candidate into txt file
        txtfile.write((f"{candidateNames}: {votePercentage:.3f}% ({votes:})\n"))
    # to find the winning candidate, find the winning percentage, vote percentage, and name of winning candiate
        if votePercentage>winningPercentage:
            winningPercentage=votePercentage
            winningVote=votes
            winningCandidate=candidateNames
    
    # writing the results of the winning candidate onto text file
    txtfile.write ("------------------\n")
    txtfile.write (f"Winner: {winningCandidate}\n")
    txtfile.write ("------------------")
# printing the results of the winning candidate to the terminal    
print("------------------")
print(f"Winner: {winningCandidate}")
print("------------------")



