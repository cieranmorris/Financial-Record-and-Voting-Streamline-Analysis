
#import modules and path to files
import os
import csv
import statistics as average


budget_data_csv = os.path.join("Resources", "budget_data.csv")
print(budget_data_csv)

#Lists to store data
total_months = []
total_amount = []
profit_loss = []
profit_change = []

#average function for profit_change
def Average(myList):
   return(avg.mean(myList))

#create csvreader for file   
with open(budget_data_csv, newline = "", encoding = "ISO-8859-1") as csvfile:
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
  initial_loop = 0
  greatest_increase = 0
  greatest_decrease = 0


  for row in budget_data:
      total_months = total_months + 1
      print(row[1])
      net_total_amount = net_total_amount + int(row[1])

      #append calculations to lists  
      # total_months.append(row[0])
      # profit_loss.append(int(row[1]))



  #Changes in Profit/Losses over entire period
      current_row = int(row[1])
      if initial_loop == False:
        monthly_change = current_row - previous_row


#   # see if this code section is necessary at this point?
#   # def average(profit_loss_change):
      
#   #     length = len(profit_loss_change)
#   #     total = 0.0

#   #     for number in profit_loss_change:
#   #         total += number
      
#   #     return total / length





#   #greatest increase in profits (date & amount) over entire period

# max_profit = list[]
# max_profit = max(profit_change)
# print(max_profit)

# #greates decrease in losses (date and amount) over entire period

# min_profit = list[]
# min_profit = min(profit_change)
# print(min_profit)


print("Financial Analysis")
print("-----------------------------")
print(f' net_total_amount {net_total_amount}')
print(f' total_months {total_months}')

# print("Average Change: {average_profit_changes}")
# print("Greatest Increase in Profits: {max_profit}")
# print("Greatest Decrease in Profits: {min_profit}")

