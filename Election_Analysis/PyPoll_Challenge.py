# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
counties = []
county_votes = {}

# Track the winning candidate, vote count and percentage

#declare empty string variable for the winner
winning_candidate = " "

#Set the winning count to begin at 0
winning_count = 0

#Set the winning percentage calculation to begin at 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
#county with the most votes
most_county = " "

#Number of votes for the county with the most votes
most_votes = 0

#the percentage of the total votes come from this county
most_percentage = 0


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    
    #read the file object with the reader function
    reader = csv.reader(election_data)

    #Don't read header row
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name=row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to the candidate list
        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name]=0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name]+=1

        # 4a: Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in counties:

            # 4b: Add the existing county to the list of counties.
            counties.append(county_name)
        
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name]=0
            
        # 5: Add a vote to that county's vote count.
        county_votes[county_name]+=1
       
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end=" ")

    #save to text file
    txt_file.write(election_results)

        #6a: Write a for loop to get the county from the county dictionary.
    for county_name in counties:
        # 6b: Retrieve the county vote count.
        votes_per_county=county_votes[county_name]

        # 6c: Calculate the percentage of votes for the county.
        vote_percentage=float(votes_per_county)/float(total_votes)*100

        # 6d: Print the county results to the terminal.
        voter_turnout=(f'{county_name}: {vote_percentage:.1f}%: ({votes_per_county:,})\n')
        
        print(voter_turnout)

        # 6e: Save the county votes to a text file.
        txt_file.write(voter_turnout)

        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes_per_county > most_votes) and (vote_percentage > most_percentage):
            most_votes = votes_per_county
            most_percentage = vote_percentage
            most_county = county_name
    
    # 7: Print the county with the largest turnout to the terminal.
    county_voter_results=(
        f'-------------------------\n'
        f'Largest County Turnout:  {most_county}\n'
        f'-------------------------\n')
    print(county_voter_results)
            
    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(county_voter_results)

     # Save the final candidate vote count to the text file.
        #for candidate_name in candidate_votes:
    for candidate_name in candidate_votes:
        #declare 'votes' as the value in the candidate dictionary
        votes=candidate_votes[candidate_name]

        #Calculate the percentage by dividing the candidate count by the total number of votes
        candidate_vote_percentage =float(votes)/float(total_votes)*100
    
        #print each candidates name, vote count, and percentage of the total votes
        candidate_results=(f'{candidate_name}: {candidate_vote_percentage:.1f}% ({votes:,})\n')

        #Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        #Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (candidate_vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = candidate_vote_percentage
            winning_candidate = candidate_name
    
    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    #Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
