# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
Candidates_options =[]
Candidates_dict ={}

# Winning Candidate and Winning Count Tracker
winning_total = 0
winning_candidate = ""

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data, delimiter=",")

    # Skip the header row
    header = next(reader)
    
    # Loop through each row of the dataset and process it
    for row in reader:
        #print(row)

        # Increment the total vote count for each row
        total_votes+=1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in Candidates_options:
            Candidates_options.append(candidate_name)
            Candidates_dict[candidate_name]=0

        # Add a vote to the candidate's count
        Candidates_dict[candidate_name]+=1

#Determine the winning candidate by counting votes in dictionary
for key in Candidates_dict.keys():
    if Candidates_dict[key] > winning_total:
        winning_candidate = key
        #Determine the winning total number of votes
        winning_total = Candidates_dict[key]

# Calculate the percentages for each candidate and format them as percentages     
Percentage_0 = f'{Candidates_dict[Candidates_options[0]] / total_votes}'
number_0 = float(Percentage_0)
percent_0 = number_0 *100
Percentage_0_format = f"{percent_0:.3f}%"
Percentage_1 = f'{Candidates_dict[Candidates_options[1]] / total_votes}'
number_1 = float(Percentage_1)
percent_1 = number_1 *100
Percentage_1_format = f"{percent_1:.3f}%"
Percentage_2 = f'{Candidates_dict[Candidates_options[2]] / total_votes}'
number_2 = float(Percentage_2)
percent_2 = number_2 *100
Percentage_2_format = f"{percent_2:.3f}%"

#Convert integers to strings so they can be written in .txt file
total_votes_str = f'{total_votes}'
Count_0_str = f'{Candidates_dict[Candidates_options[0]]}'
Count_1_str = f'{Candidates_dict[Candidates_options[1]]}'
Count_2_str = f'{Candidates_dict[Candidates_options[2]]}'

# Generate and print the winning candidate summary in terminal
print(Candidates_dict)
print ("Election Results")

print ("----------")

print ("Total Votes:", f'{total_votes}')

print ("----------")

print (Candidates_options[0], Percentage_0_format, "Vote Total:", Candidates_dict[Candidates_options[0]])
print (Candidates_options[1], Percentage_1_format, "Vote Total:", Candidates_dict[Candidates_options[1]])
print (Candidates_options[2], Percentage_2_format, "Vote Total:", Candidates_dict[Candidates_options[2]])

print ("----------")

print ("Winner: ", winning_candidate)

print ("----------")

# Save the winning candidate summary to the text file
# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("---------------\n")
    txt_file.write("Total Votes: ")
    txt_file.write(total_votes_str)
    txt_file.write("\n---------------\n")
    txt_file.write(Candidates_options[0])
    txt_file.write(": ")
    txt_file.write(Percentage_0_format)
    txt_file.write(" Votes: ")
    txt_file.write(Count_0_str)
    txt_file.write("\n")
    txt_file.write(Candidates_options[1])
    txt_file.write(": ")
    txt_file.write(Percentage_1_format)
    txt_file.write(" Votes: ")
    txt_file.write(Count_1_str)
    txt_file.write("\n")
    txt_file.write(Candidates_options[2])
    txt_file.write(": ")
    txt_file.write(Percentage_2_format)
    txt_file.write(" Votes: ")
    txt_file.write(Count_2_str)
    txt_file.write("")
    txt_file.write("\n---------------\n")
    txt_file.write("Winner: ")
    txt_file.write(winning_candidate)
    txt_file.write("\n---------------")
    


    