# import modules to read csv file
import os   # module for path in different OS systems
import csv  # module for csv files

# file path
budget_csv=os.path.join('Resources', 'budget_data.csv')

# create Lists to store data
date = []
profit_losses = []
profit_losses_changes = []

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
    
    profit_losses.append(int(row[1]))
    



# The total number of months included in the dataset
total_months = len(date)


# The net total amount of "Profit/Losses" over the entire period
total_profit_losses = sum(profit_losses)


# Calculate the changes in "Profit/Losses" over the entire period
for i in range(len(profit_losses)-1):    
  profit_losses_changes.append(profit_losses[i+1]-profit_losses[i])
    

# Find the average of "Profit/Losses" changes
average_change = sum(profit_losses_changes) / len(profit_losses_changes)


# Find the greatest increase in profits (date and amount) over the entire period
greatest_increase = max(profit_losses_changes)



# Find the greatest decrease in losses (date and amount) over the entire period
greatest_decrease = min(profit_losses_changes)




#------- Print the Analysis to the Terminal ------------
print(30*'-')
print('Financial Analysis')
print(30*'-')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit_losses}')
print(f'Average Change: ${round(average_change, 2)}')
print(f'Greatest Increase in Profits: {date[(profit_losses_changes.index(greatest_increase)+1)]} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {date[(profit_losses_changes.index(greatest_decrease)+1)]} (${greatest_decrease})')


#------- Export the results to a text file ------------

# Create "Analysis" folder
os.mkdir("Analysis")

# Set variable for output file
output_file = os.path.join('Analysis', 'budget_final.txt')

Text = [
        f'\nTotal Months: {total_months}\n',
        f'Total: ${total_profit_losses}\n',
        f'Average Change: ${round(average_change, 2)}\n',
        f'Greatest Increase in Profits: {date[(profit_losses_changes.index(greatest_increase)+1)]} (${greatest_increase})\n',
        f'Greatest Decrease in Profits: {date[(profit_losses_changes.index(greatest_decrease)+1)]} (${greatest_decrease})'
      ]

# Open the output file for writing
with open(output_file, 'w') as txt_file:
  # writing data to a file
  txt_file.write('Financial Analysis \n')
  txt_file.write(30*'-')
  txt_file.writelines(Text)




  


