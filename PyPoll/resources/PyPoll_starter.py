# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

"""
Modernized Vote - Count Processor
This script reads the election data from the CSV file, calculates total votes, 
determines the percentage of votes for each candidate, and identifies the winner, 
and outputs 
"""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Variable that tracks the total number of votes cast 
total_votes_count = 0  

# Dictionary that tracks each candidate's votes 
candidates_votes_count = {}

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Track the votes that each candidate received 
    for row in reader:
        total_votes_count += 1
        candidate = row[2]
        if candidate in candidates_votes_count:
            candidates_votes_count[candidate] += 1
        else:
            candidates_votes_count[candidate] = 1

# Prepare election results
election_results = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes_count}\n"
    "-------------------------\n"
)

# Add candidate results to the election results
for candidate, votes in candidates_votes_count.items():
    vote_percentage = (votes / total_votes_count) * 100
    candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes} votes)\n"
    election_results += candidate_results

# Determine the winning candidate
winning_candidate = max(candidates_votes_count, key=candidates_votes_count.get)

# Add winner to the election results
election_results += (
    "-------------------------\n"
    f"Winner: {winning_candidate}\n"
    "-------------------------\n"
)

# Print and save the results
print(election_results)

with open(file_to_output, "w") as txt_file:
    txt_file.write(election_results)


        
        # Print a loading indicator (for large datasets)
        # !!print(". ", end="")

        # Increment the total vote count for each row


        # Get the candidate's name from the row


        # If the candidate is not already in the candidate list, add them


        # Add a vote to the candidate's count


# Open a text file to save the output
# !!with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)


    # Write the total vote count to the text file


    # Loop through the candidates to determine vote percentages and identify the winner


        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage


    # Generate and print the winning candidate summary


    # Save the winning candidate summary to the text file
