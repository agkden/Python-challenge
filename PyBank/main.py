# import modules to read csv file
import os   # module for path in different OS systems
import csv  # module for csv files

# file path
budget_csv=os.path.join('Resources', 'budget_data.csv')

# create Lists to store data
date = []
profit_losses = []


# open csv file
with open(budget_csv) as csvfile:
  # Split the data on commas
  csvreader = csv.reader(csvfile, delimiter=',')
  # if header row exist, skip the first row
  header = next(csvreader)

  # Loop through the data
  for row in csvreader:
    # iterate through each row and append to new lists
    date.append(row[0])
    #print(date)

    profit_losses.append(int(row[1]))
    #print(profit_losses)


# The total number of months included in the dataset
total_months = len(date)
#print(total_months)


# The net total amount of "Profit/Losses" over the entire period
total_profit_losses = sum(profit_losses)
#print(total_profit_losses)




#------- Print the Analysis to the Terminal ------------
print(30*'-')
print('Financial Analysis')
print(30*'-')
print('Total Months: ' + str(total_months))
print('Total: $' + str(total_profit_losses))







  


