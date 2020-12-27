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
    #print(date)

    profit_losses.append(int(row[1]))
    #print(profit_losses)


# The total number of months included in the dataset
total_months = len(date)
#print(total_months)

# The net total amount of "Profit/Losses" over the entire period
total_profit_losses = sum(profit_losses)
#print(total_profit_losses)

# Calculate the changes in "Profit/Losses" over the entire period
for i in range(len(profit_losses)-1):    
  profit_losses_changes.append(profit_losses[i+1]-profit_losses[i])
  #print(profit_losses_changes)  

# Find the average of "Profit/Losses" changes
average_change = sum(profit_losses_changes) / len(profit_losses_changes)
#print(average_change)

# Find the greatest increase in profits (date and amount) over the entire period
greatest_increase = max(profit_losses_changes)
#print(greatest_increase)
#print(date[(profit_losses_changes.index(greatest_increase)+1)])

# Find the greatest decrease in losses (date and amount) over the entire period
greatest_decrease = min(profit_losses_changes)
#print(greatest_decrease)
#print(date[(profit_losses_changes.index(greatest_decrease)+1)])


#------- Print the Analysis to the Terminal ------------
print(30*'-')
print('Financial Analysis')
print(30*'-')
print('Total Months: ' + str(total_months))
print('Total: $' + str(total_profit_losses))
print('Average Change: $' + str(round(average_change, 2)))
print('Greatest Increase in Profits: ' + (date[(profit_losses_changes.index(greatest_increase)+1)]) + ' ($' + str(greatest_increase) + ')')
print('Greatest Decrease in Profits: ' + (date[(profit_losses_changes.index(greatest_decrease)+1)]) + ' ($' + str(greatest_decrease) + ')')


#------- Export the results to a text file ------------

# Create "Analysis" folder
os.mkdir("Analysis")

# Set variable for output file
output_file = os.path.join('Analysis', 'budget_final.txt')

Text = [
        '\nTotal Months: ' + str(total_months) + '\n',
        'Total: $' + str(total_profit_losses) + '\n',
        'Average Change: $' + str(round(average_change, 2)) + '\n',
        'Greatest Increase in Profits: ' + (date[(profit_losses_changes.index(greatest_increase)+1)]) + ' ($' + str(greatest_increase) + ')' + '\n',
        'Greatest Decrease in Profits: ' + (date[(profit_losses_changes.index(greatest_decrease)+1)]) + ' ($' + str(greatest_decrease) + ')'
      ]

# Open the output file for writing
with open(output_file, 'w') as txt_file:
  # writing data to a file
  txt_file.write('Financial Analysis \n')
  txt_file.write(30*'-')
  txt_file.writelines(Text)




  


