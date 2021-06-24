import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#define the lists
fields = []
rows = []
months = []
pl = []
pl_change = []
average_change = []

# Method 2: Improved Reading using CSV module

with open(csvpath, newline= '') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    fields = next(csvreader)
    #print(f"Field Names: {fields}")

    #calculating # of rows and total revenue
    total_revenue = 0
    for row in csvreader:
        rows.append(row)
        months.append(row[0])
        pl.append(row[1])
        #sums profit/loss list
        total_revenue += int(row[1])

    
    i = 0
    for i in range(len(pl) - 1):
        # Take the difference between two months 
        monthly_profit_loss = int(pl[i+1]) - int(pl[i])
        # append the monthly profit/loss calculation to pl_change list
        pl_change.append(monthly_profit_loss)

        #Calculate Avg Change
        Total = sum(pl_change)
        average_change = round(Total / len(pl_change),2)
    
    #Greatest increase , greatest decrease

    greatest_increase = max(pl_change)
    max_month_increase = pl_change.index(greatest_increase) + 1
    greatest_decrease = min(pl_change)
    max_month_decrease = pl_change.index(greatest_decrease) + 1
    
    #print in terminal

    print("Financial Analysis")
    print("---------------------------------")
    print("Total no. of months: %d"%(csvreader.line_num - 1))
    print("Net total amount of Profits/Losses: $" +str(total_revenue))
    print("Average Change: $" +str(average_change))
    print('Greatest increase: ${} at month {}'.format(str(greatest_increase), months[max_month_increase]))
    print('Greatest decrease: ${} at month {}'.format(str(greatest_decrease), months[max_month_decrease]))

    #OUTPUT
    output_file = os.path.join('Analysis','output_file.txt')
    with open(output_file, "w") as file:
    
        
            file.write("Financial Analysis")
            file.write("\n")
            file.write("----------------------------")
            file.write("\n")
            file.write("Total no. of months: %d"%(csvreader.line_num - 1))
            file.write("\n")
            file.write("Net total amount of Profits/Losses: $" +str(total_revenue))
            file.write("\n")
            file.write("Average Change: $" +str(average_change))
            file.write("\n")
            file.write('Greatest increase: ${} at month {}'.format(str(greatest_increase), months[max_month_increase]))
            file.write("\n")
            file.write('Greatest decrease: ${} at month {}'.format(str(greatest_decrease), months[max_month_decrease]))


