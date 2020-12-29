# import modules to read csv file
import os   # module for path in different OS systems
import csv  # module for csv files

# file path
election_csv = os.path.join('Resources', 'election_data.csv')

# create Lists and Dictionary to store data
voters = []
candidates_with_votes = {}  # dictionary to store candidate name as key and votes as value
#votes_percent = [] # list to store percentage of votes each candidate won


# open csv file
with open(election_csv) as csvfile:
  # Split the data on commas
  csvreader = csv.reader(csvfile, delimiter=',')
  # if header row exist
  header = next(csvreader)

  # read each row of data
  for row in csvreader:
    # iterate through each row and append to new lists
    voters.append(row[0])   
    # print(voters)

    # A complete list of candidates who received votes and the total number of votes each candidate won
    if row[2] not in candidates_with_votes:
      candidates_with_votes[row[2]] = 1
    else:      
      candidates_with_votes[row[2]] += 1

  #print(candidates_with_votes)


# The total number of votes
total_votes = len(voters)
#print(total_votes)


# The winner of the election based on popular vote
winner = max(candidates_with_votes, key=candidates_with_votes.get)
#print(winner)
 
 
#------- Print the Analysis to the Terminal ------------
print(30*'-')
print('Election Results')
print(30*'-')
print(f"Total Votes: {str(total_votes)}")
print(30*'-')
for x, y in candidates_with_votes.items():
  print(f"{x}: {str(round((candidates_with_votes[x] / total_votes * 100), 3))}% ({str(y)})")  
print(30*'-') 
print(f"Winner: {winner}")
print(30*'-')



#------- Export the results to a text file ------------

    

