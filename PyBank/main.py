# -*- coding: UTF-8 -*-
"""
Author: Jeff Gielniak
Date: 2024-12-11
"""

# Dependencies
import csv
import os

# Files to load and output
file_to_load = os.path.join( "Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_sum = 0
net_change = 0
net_change_total = 0
next_profit = 0
greatest_increase = 0
greatest_decrease = 0
month_list = []

# Open and read the csv
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data, delimiter=",")
    
    # Skip the header row
    next(reader)

    #Set a variable for the first month's profit
    for row in reader:
        month_list.append(row[0])
        first_profit = int(row[1])
        break
    #Add first month's profit into total sum
    total_sum = first_profit
    #Create a monthlist and count the length to find total number of months    
    for row in reader:
        month_list.append(row[0])
        
    # Track the total and net change
        # Track the total
        total_sum += float(row[1])

        # Track the net change
        next_profit = int(row[1])
        net_change = next_profit - first_profit
        net_change_total += net_change
        
        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase:
            greatest_increase = net_change
            greatest_increase_month = (row[0])

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease:
            greatest_decrease = net_change
            greatest_decrease_month = (row[0])

        first_profit = next_profit

# Calculate the average net change across the months; take one month away because the delta is only over 85 values
Average_change = net_change_total / (len(month_list)-1)
Format_Average_change =f"{Average_change:.2f}"

# Generate and Print the output summary
print ("Financial Analysis")

print ("----------")

print ("The total number of months is:", len(month_list))
print ("The net total amount of Profit/Losses over the period: $", total_sum)
print ("The average change is:$", (Format_Average_change))
print ("The greatest increase in Profits:", greatest_increase_month, "$",greatest_increase)
print ("The greatest decrease in profits:", greatest_decrease_month, "$",greatest_decrease)

#Format values to a string so they can be written to a .txt
month_str=f'{len(month_list)}'
net_total_str=f'{total_sum}'
avg_str=f'{(Format_Average_change)}'
increase_str_month=f'{greatest_increase_month}'
increase_str=f'{greatest_increase}'
decrease_str_month=f'{greatest_decrease_month}'
decrease_str=f'{greatest_decrease}'

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------\n")
    txt_file.write("The total number of months is: ")
    txt_file.write(month_str)
    txt_file.write("\nThe net total amount of Profit/Losses over the period: $ ")
    txt_file.write(net_total_str)
    txt_file.write("\nThe average change is: $")
    txt_file.write(avg_str)
    txt_file.write("\nThe greatest increase in Profits:")
    txt_file.write(increase_str_month)
    txt_file.write(" $")
    txt_file.write(increase_str)
    txt_file.write("\nThe greatest decrease in profits:")
    txt_file.write(decrease_str_month)
    txt_file.write(" $")
    txt_file.write(decrease_str)

    