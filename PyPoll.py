# Pull voting data from csv file
# Create list of dictionaries [{voter: ballot_ID, county: county_name, candidate: candiate_name}]
# Determine the total number of voters by county
# Determine the percentage of votes each candiate won by county
# Determine statewide total for voters
# Determine statewide winner for the election based on popular vote

# Adding dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_save = os.path.join("analysis", "election_analysis.txt")

#Initalizing candidate name's variable
winning_candidate = ""
# Setting Vote Accumulator to zero
total_votes = 0
# Setting Winning Accumulator to zero
winning_count = 0
# Setting Winning Percentage Accumulator to zero
winning_percentage = 0
# Empty List for candidates' names
candidate_options = []
# Empty Dictionary for candidate:votes
candidate_votes = {}
# Open the election results and read the file.
with open(file_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read Header Row
    headers = next(file_reader)
    # Looping through each row in the CSV file to gather total votes and candidates' names
    for row in file_reader:
        total_votes += 1
        # Assigning variable for candidate name row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            # Adding unique names to list
            candidate_options.append(candidate_name)
            # Tracking votes for each candidate
            candidate_votes[candidate_name] = 0 
            # Tallying Votes
        candidate_votes[candidate_name] += 1 
    with open(file_save, "w") as election_analysis:
        election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
        print(election_results, end="")
        # Saving to txt file
        election_analysis.write(election_results)
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list to get to vote count
        for candidate in candidate_votes:
            votes = candidate_votes[candidate]
            vote_percentage = (votes) / (total_votes) * 100
            candidate_results = (f"{candidate}: {float(vote_percentage):.1f}% ({votes:,})\n")
            print(candidate_results)
            # Save results to Election_Analysis.txt
            election_analysis.write(candidate_results)
            # Logic for election printout
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate
                winning_percentage = vote_percentage
            # Formatting for election printout
            winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
            # Saving to txt file
        election_analysis.write(winning_candidate_summary)