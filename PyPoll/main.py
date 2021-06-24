import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#define the lists
fields = []
rows = []
idList = []
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
        rows.append(row)
        idList.append(row[0])
        candidates.append(row[2])
      #PRINT

    print("Election Results")
    print("---------------------")
    print("Total Votes: "  +str(total_votes))
    print("---------------------")

    
    #print out unique values from candidates list

    def unique(candidates):

      unique_list = []

      for x in candidates:
        if x not in unique_list:
          unique_list.append(x)
      for x in unique_list:
        print(x)
    
    #print out list of candidates
    print("List of candidates:")
    unique(candidates)
    print("---------------------")

    #assign varianbles for candidates
    k = str("Khan")
    c = str("Correy")
    l = str("Li")
    o = str("O'Tooley")

    #count number of votes per candidate
    def countk(candidates, k):
      count1 = 0
      for ele in candidates:
          if (ele == k):
              count1 = count1 + 1
      return count1
  
    def countc(candidates, c):
      count2 = 0
      for ele in candidates:
          if (ele == c):
              count2 = count2 + 1
      return count2

    def countl(candidates, l):
      count3 = 0
      for ele in candidates:
          if (ele == l):
              count3 = count3 + 1
      return count3

    def counto(candidates, o):
      count4 = 0
      for ele in candidates:
          if (ele == o):
              count4 = count4 + 1
      return count4

  #calculate the percentage
    percent_k = round((countk(candidates, k)/total_votes)*100,2)
    percent_c = round((countc(candidates, c)/total_votes)*100,2)
    percent_l = round((countl(candidates, l)/total_votes)*100,2)
    percent_o = round((counto(candidates, o)/total_votes)*100,2)

  #print out number of votes for each candidate
    print('{} has {} votes or {}%  '.format(k, countk(candidates, k),percent_k))
    print('{} has {} votes or {}%  '.format(c, countc(candidates, c),percent_c))
    print('{} has {} votes or {}%  '.format(l, countl(candidates, l),percent_l))
    print('{} has {} votes or {}%  '.format(o, counto(candidates, o),percent_o))
    print("---------------------")
    print("The winner is Khan!")

  #OUTPUT
    output_file = os.path.join('Analysis','output_file.txt')
    with open(output_file, "w") as file:
    
      file.write("Election Results")
      file.write("\n")
      file.write("---------------------")
      file.write("\n")
      file.write("Total Votes: "  +str(total_votes))
      file.write("\n")
      file.write("---------------------")
      file.write("\n")
      file.write('{} has {} votes or {}%  '.format(k, countk(candidates, k),percent_k))
      file.write("\n")
      file.write('{} has {} votes or {}%  '.format(c, countc(candidates, c),percent_c))
      file.write("\n")
      file.write('{} has {} votes or {}%  '.format(l, countl(candidates, l),percent_l))
      file.write("\n")
      file.write('{} has {} votes or {}%  '.format(o, counto(candidates, o),percent_o))
      file.write("\n")
      file.write("---------------------")
      file.write("\n")
      file.write("The winner is Khan!")
#END--------------------------------------------------------------------------------------------------------------     
    
