import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#define the lists
fields = []
rows = []
idList = []
votes = 0
winner_votes = 0
candidates = []
candidate_votes = []
results = []

# Method 2: Improved Reading using CSV module

with open(csvpath, newline= '') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    fields = next(csvreader)
    #print(f"Field Names: {fields}")

    #calculating # of rows and total revenue
    total_votes = 0
    for row in csvreader:
    
        #sums votes
        total_votes+= 1
        idList.append(row[0])
        candidates.append(row[2])
      #PRINT

    print("Election Results")
    print("---------------------")
    print("Total Votes: "  +str(total_votes))
    print("---------------------")

  #gets harder from here
#--------------------------------------------------------------------------------------------------------------     
    
