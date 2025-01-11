
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

# Variable that tracks the total nummber of votes cast 
total_votes_count = 0  

# Dictionary that tracks each canidates votes 
candidates_votes_count = {}

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skips the header row
    header = next(reader)

    # Counts and tracks the total votes that each candidate recieved 
    for row in reader:
        total_votes_count += 1
        candidate = row[2]
        if candidate in candidates_votes_count:
            candidates_votes_count[candidate] += 1
        else:
            candidates_votes_count[candidate] = 1


# Creates a variable to store the election results, and desired output text
election_results = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes_count}\n"
    "-------------------------\n"
)

# Combines the candidate votes and percentage to the election results
for candidate, votes in candidates_votes_count.items():
    vote_percentage = (votes / total_votes_count) * 100
    candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes} votes)\n"
    election_results += candidate_results

# Determine the winning candidate
winning_candidate = max(candidates_votes_count, key=candidates_votes_count.get)

# Adds to the elections results variable for the winner and desired output text
election_results += (
    "-------------------------\n"
    f"Winner: {winning_candidate}\n"
    "-------------------------\n"
)

# Prints the results
print(election_results)

# Outputs the election results to the txt file 
with open(file_to_output, "w") as txt_file:
    txt_file.write(election_results)
