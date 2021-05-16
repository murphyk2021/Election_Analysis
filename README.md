# Module 3:  PyPoll with Python
## An Introduction to Python 
- - - 
## Overview of Project
In this module students were asked to help Tom with the task of sorting through over 360,000 ballots to determine the winner of a congressional election in Colorado.  Although we could have used Excel to achieve this task, it is much easier and more efficient to use Python and Visual Studio Code instead. There are many similarities between the Python language and VBA, but there are also many differences that needed to be discussed and practiced during this exercise.  During this module we learned:
- proper formatting and syntax or Python language,
- how to create and manipulate lists and dictionaries,
- the order of operations of mathematical equations, 
- more about loops and conditionals,
- how to access a .csv, .xls, .txt file,
- how to write to a .txt file
---
## Election-Audit Results
From the data print out provided below we were able to determine how many votes each candidate received and from which county the votes were cast.
![Election Results Printout](https://github.com/murphyk2021/Election_Analysis/blob/8dcf3343fe2f68e999e75b01e35cfbb1730fb424/Resources/compiled_results.png)

- A total of 369,711 votes were cast in this election
- 6.7% (24,801) of the total votes were cast by citizens of **Arapahoe county**.
- 10.5% (38,855) of the total votes were cast by citizens of **Jefferson county**.
- 82.8% (306,055) of the total votes were cast by citizens of **Denver county**.
- The winning candidate, **Diana DeGette**, received 73.8% (272,892) of the total votes.
- The runner-up, **Charles Casper Stockham**, received 23.0% (85,213) of the total votes.
- The remaining candidate, **Raymon Anthony Doane**, received 3.1% (11,606) of the total votes.
- It appears we will not need to have a run-off election!

## Explanation of the Code
To carry ot this election audit we needed to first access another file by identifying the location of the file and importing the csv and os module so that VSC would be able to sort though the many data points.  To do this we used the code: 
![import dependecy code](https://github.com/murphyk2021/Election_Analysis/blob/3e0a46fe0472dbd11d8bff82fe698f9f800c32a7/Resources/importdependency.PNG)

### Step 1:  Prepare to collect information about our candidates, the number of votes, and determine who received the most votes.  
We established variables for all of these metrics before we even opened the file to read with the following variables.  
- candidate_options=[] <--List of candidates 
- candidate_votes = {} <--Dictionary which includes the **candidate name** as the key and the **number of votes received** as the value
- counties= [] <--List of the counties participating in the vote
- county_votes={} <--Dictionary which includes the **county** as the key and the **number of votes received** as the value
- winning_candidate= " " <-- The winner (as a str)
- winning_count = 0 <--The winner received this number of votes initialized at 0
- winning_percentage = 0 <-- The winner received this percentage of the votes initialized at 0
- most_county = " " <-- The county with the greatest number of votes(as str)
- most_votes = 0 <--The number of votes from the county with the most votes cast initialised at 0
- most_percentage = 0 <-- The percentage of the total votes cast in the county with the most votes initialized at 0
- total_votes = 0 <-- The count of all votes cast initialized to begin counting at 0.

### Step 2:  Start collecting information about the cadidates and the counties.   
We ran two **For loops** with **If statements** - one to create the list of candidates and te dictionary which included both the candidate name and the total count of votes they received.  The other was formatted to fill in the information about the counties.



### Step 3:  Determine the winner!

Things to add
Voter turnout per county (if given the population size)
