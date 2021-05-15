# Add dependencies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load=os.path.join('Resources', 'election_results.csv')

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#initialize a total vote counter and set to zero.
total_votes =0

#Create list for candidate names
candidate_options =[]

#Create an empty dictionary to store the vote counts for each candidate
candidate_votes={}

#declare empty string variable for the winner
winning_candidate=" "

#Set the winning count to begin at 0
winning_count = 0

#Set the winning percentage calculation to begin at 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:

    # read the file object with the reader function.
    file_reader=csv.reader(election_data)

    # assign variable to the header row
    headers=next(file_reader)

# 1. The total number of votes cast. 
  
    # print each row in the csv file and add to the total vote count.
    for row in file_reader:
        total_votes+=1
        
    #print the total votes
    #print(total_votes)

# 2. A complete list of candidates who received votes.

    #print the candidate name from each row (in column 3)
        candidate_name=row[2]
        #If the candidate does not match any existing candidate then add it to the list
        if candidate_name not in candidate_options:

            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            #Beging counting votes for candidates at 0
            candidate_votes[candidate_name]=0
            
        #Start counting the votes for each candidate
        candidate_votes[candidate_name]+=1

# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.

#Iterate through the candidate dictionary
for candidate_name in candidate_votes:

    #declare 'votes' as the value in the candidate dictionary
    votes=candidate_votes[candidate_name]

    #Calculate the percentage by dividing the candidate count by the total number of votes
    vote_percentage =float(votes)/float(total_votes)*100
    
    #print each candidates name, vote count, and percentage of the total votes
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

# 5. The winner of the election based on popular vote.
#if statement is true, then set the following variables to the values determined above
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count=votes
        winning_percentage = vote_percentage
        winning_candidate=candidate_name

candidate_votes[candidate_name]+=1

winning_candidate_summary = (
    f'-------------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count:  {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    f'-------------------------\n')
print(winning_candidate_summary)


