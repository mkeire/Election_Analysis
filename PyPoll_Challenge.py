# Adding dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_save = os.path.join("analysis", "election_analysis.txt")

# Initalizing State voting variables
winning_candidate = ""
# Setting candidate vote accumulator to zero
total_votes = 0
# Setting Winning Accumulator to zero
winning_count = 0
# Setting Winning Percentage Accumulator to zero
winning_percentage = 0
# Empty List for candidates' names
candidate_options = []
# Empty Dictionary for candidate:votes
candidate_votes = {}
# Open the election results and read the file

#Initializing County voting variables.
# Empty list for county names
county_names = []
# Empty dictionary for county votes
county_votes = {}
# Empty string for county with largest number of votes casted
largest_county = ""
# Total votes for a county
county_total_votes = 0
# County with the most votes
county_max_votes_total = 0

with open(file_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read Header Row
    headers = next(file_reader)
    # Looping through each row in the CSV file to gather total votes and candidates' names
    for row in file_reader:
        #State Results
        total_votes += 1
        # Assigning variable for candidate name row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            # Adding candidate names to list -  no duplicates
            candidate_options.append(candidate_name)
            # Tracking votes for each candidate
            candidate_votes[candidate_name] = 0 
        # Tallying Candidate Votes
        candidate_votes[candidate_name] += 1 

        # County Results
        county_total_votes += 1
        county_name = row[1]
        if county_name not in county_names:
            #Adding county names to list - no duplicates
            county_names.append(county_name)
            # Tracking county votes
            county_votes[county_name] = 0
        # Tallying Votes per county
        county_votes[county_name] += 1

    with open(file_save, "w") as election_analysis:
        election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\n"
        f"County Votes:\n"
        )
        print(election_results, end="")
        # Saving to txt file
        election_analysis.write(election_results)

        # Calculate county vote percentages and total votes
        # Iterate through the county list to get to their respective vote count
        for county in county_votes:
            # Initalize variable for county votes
            c_votes = county_votes[county]
            county_vote_percentage = (c_votes) / (county_total_votes) * 100
            county_results = (f"{county}: {float(county_vote_percentage):.1f}% ({c_votes:,})\n")
            print(county_results)
            # Save County results to Election_Analysis.txt
            election_analysis.write(county_results)
            # Logic for county with most votes
            if (c_votes > county_max_votes_total):
                county_max_votes_total = c_votes
                largest_county = county
            # Formatting County with the most votes
            largest_county_summary = (
                f"-------------------------\n"
                f"Largest County Turnout: {largest_county}\n"
                f"-------------------------\n"
            )
        print(largest_county_summary)
        election_analysis.write(largest_county_summary)
        # Calculate total vote percentages and total votes for each candidate
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