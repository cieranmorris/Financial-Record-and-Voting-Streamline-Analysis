
#import modules and path to files
import os
import csv
import statistics as avg


budget_data_csv = os.path.join("Resources", "budget_data.csv")
print(budget_data_csv)

#Lists to store data
total_months_change = []
total_amount = []
profit_loss = []
profit_change = []

#average function for profit_change

def Average(myList):
  mean_average = avg.mean(myList)
  return(mean_average)

#create csvreader for file   
with open(budget_data_csv) as csvfile:
  budget_data = csv.reader(csvfile, delimiter= ",")

  #print(budget_data)

  csv_header = next(budget_data)
  print(f"CSV Header: {budget_data}")

#count total number of months in CSV
#net total amount of Profit/Losses over the entire period

#Define variables
  month = 0
  total_months =0 
  net_total_amount = 0
  current_row = 0
  previous_row = 0
  monthly_change = 0
  total_price_change = 0
  initial_loop = True
  greatest_increase = 0
  greatest_decrease = 0
  greatest_increase_month = 0
  greatest_decrease_month = 0
  


  for row in budget_data:
    total_months = total_months + 1
    #print(row[1])

    net_total_amount = net_total_amount + int(row[1])
    #if the first row (no calculations), but remember last month profit
    if total_months == 1:
      last_months_profit = int(row[1])
    else:
      #calculate monthly change and remember the current row as the last month's profit
      monthly_change = int(row[1]) - last_months_profit
      last_months_profit = int(row[1])

      #append monthly changes to the total_months_change list
      total_months_change.append(monthly_change)

      #calculate greatest increase in profits
      if monthly_change > greatest_increase:
        greatest_increase = monthly_change
        greatest_increase_month = (row[0])

      if monthly_change < greatest_decrease:
        greatest_decrease = monthly_change
        greatest_decrease_month = (row[0])



  #calculate average monthly changes
  avg = Average(total_months_change)

print("Financial Analysis")
print("-----------------------------")
print(f' Total Months: {total_months}')
print(f' Total: {net_total_amount}')
print(f"Average Change: {avg}")
print(f"Greatest Increase in Profits: {greatest_increase_month} ({greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} ({greatest_decrease})")

