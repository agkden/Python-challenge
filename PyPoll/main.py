# import modules to read csv file
import os   # module for path in different OS systems
import csv  # module for csv files

# file path
election_csv = os.path.join('Resources', 'election_data.csv')

# create Lists and Dictionary to store data
voters = []
# dictionary to store candidate name as key and votes as value
candidates_with_votes = {}  


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
    

    # A complete list of candidates who received votes and the total number of votes each candidate won
    if row[2] not in candidates_with_votes:
      candidates_with_votes[row[2]] = 1
    else:      
      candidates_with_votes[row[2]] += 1

  

# The total number of votes
total_votes = len(voters)


# The winner of the election based on popular vote
winner = max(candidates_with_votes, key=candidates_with_votes.get)

 

#------- Print the Analysis to the Terminal ------------

print(30*'-')
print('Election Results')
print(30*'-')
print(f"Total Votes: {total_votes}")
print(30*'-')
for x, y in candidates_with_votes.items():
  print(f"{x}: "+"{:.3%}".format((candidates_with_votes[x] / total_votes)) +f" ({y})") 
print(30*'-') 
print(f"Winner: {winner}")
print(30*'-')



#------- Export the results to a text file ------------

#  Set variable for output file
output_file = os.path.join('Analysis', 'election_final.txt')


# Open the output file for writing into it
with open(output_file, 'w') as txt_file:
  # writing data to a file
  txt_file.write(30*'-')
  txt_file.write('\nElection Results \n')
  txt_file.write(30*'-')
  txt_file.write(f"\nTotal Votes: {total_votes}\n")
  txt_file.write(30*'-'+'\n')
  for x, y in candidates_with_votes.items():
    txt_file.write(f"{x}: "+"{:.3%}".format((candidates_with_votes[x] / total_votes)) +f" ({y})\n") 
  txt_file.write(30*'-') 
  txt_file.write(f"\nWinner: {winner}\n")
  txt_file.write(30*'-')



 