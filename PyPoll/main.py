# import modules to read csv file
import os   # module for path in different OS systems
import csv  # module for csv files

# file path
election_csv = os.path.join('Resources', 'election_data.csv')

# create Lists to store data
candidates = []
voters = []

Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0

# open csv file
with open(election_csv) as csvfile:
  # Split the data on commas
  csvreader = csv.reader(csvfile, delimiter=',')
  # if header row exist
  header = next(csvreader)

  # read each row of data
  for row in csvreader:
    # iterate through each row and append to new lists
    candidates.append(row[2])
    #print(candidates)

    voters.append(row[0])
    # print(voters)

    # The total number of votes each candidate won
    if row[2] == "Khan":
      Khan_votes += 1
    elif row[2] == "Correy":
      Correy_votes += 1
    elif row[2] == "Li":
      Li_votes += 1
    elif row[2] == "O'Tooley":
      OTooley_votes += 1

# The total number of votes
total_votes = len(voters)
#print(total_votes)


  

#------- Print the Analysis to the Terminal ------------
print(30*'-')
print('Election Results')
print(30*'-')
print('Total Votes: ' + str(total_votes))
print(30*'-')
print('Khan: ' + str(Khan_votes))
print('Correy: ' + str(Correy_votes))
print('Li: ' + str(Li_votes))
print("O'Tooley: " + str(OTooley_votes))
print(30*'-')
print('Winner: ')
print(30*'-')


#------- Export the results to a text file ------------

    

