# Dependencies 
import os
import csv
from collections import Counter

id_column = []
candidates_column = []
Candidate_Votes = Counter()
Percent_Votes = []

# File to load for election data
election_data_path = os.path.join("PyPoll", "election_data.csv")


# Read the election data csv file
with open("election_data.csv", "r") as election_file:
    csvReader = csv.reader(election_file, delimiter=",")

# skip the first row since is a header
    next(csvReader)

# use len to give total number of votes by counting elements in id column
    for row in csvReader:
        id_column.append(row[0])
        candidates_column.append(row[2])
        total_votes = int(len(id_column))

# using the candidate column total votes by candidate, determine the candidate with the max votes, and then use tuple to return votes by candidate. 
    for candidate in candidates_column:
        Candidate_Votes[candidate] += 1
        winner = max(zip(Candidate_Votes.values(), Candidate_Votes.keys()))
        Ind_Votes = tuple(Candidate_Votes.values())
        Unique_Candidates = tuple(Candidate_Votes.keys())       

# determine the percent of votes each candidate is receiving.  
    for x in Ind_Votes:
        Percent_Votes.append((int(x)/total_votes)*100)

# print results to terminal.
print(f"Election Results")
print(f"-----------------------")
print(f"Total Votes: {total_votes}") 
print(Unique_Candidates)
print(Ind_Votes)
print(f"{Percent_Votes}%")
print(f"Winner: {winner[1]}")

# open results in a txt file. 
txtPath = os.path.join("..", "PyPoll", "election_data.txt")

with open(txtPath, "w") as txtfile:
    txtfile.writelines(f"Election Results" + "\n")
    txtfile.writelines(f"-----------------------" + "\n")
    txtfile.writelines(f"Total Votes: {total_votes}" + "\n") 
    txtfile.writelines(f"Candidates Running: {Unique_Candidates}" + "\n")
    txtfile.writelines(f"Votes by Candidate: {Ind_Votes}" + "\n") 
    txtfile.writelines(f"% of Votes: {Percent_Votes}%" + "\n")
    txtfile.writelines(f"Winner: {winner[1]}")
