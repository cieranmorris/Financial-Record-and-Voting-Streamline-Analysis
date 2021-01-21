print("Hello from PyBank!")

#import module and csv reader
import os
import csv


budget_data_csv = os.path.join("Resources", "budget_data.csv")
print(budget_data_csv)

#Lists to store data
total_months = []
total_amount = []


with open(budget_data_csv) as csvfile:
    budget_data = csv.reader(csvfile, delimiter= ",")

    print(budget_data)

    csv_header = next(budget_data)
    print(f"CSV Header: {budget_data}")

    #count total number of months in CSV
    total_months = len(list(budget_data))
    print(total_months)
     
    total = 0
   

     #net total amount of Profit/Losses over the entire period

    for row in csvreader:
         #total Profit/Losses in column 1
         #get Profit/losses into a python list
        total_amount.append(row[1])
        total_amount = int(row[1])
        net_total = net_total + total

        print(net_total)



     #Changes in Profit/Losses over entire period 



     #Averages of changes


    # def average(profit_loss_change):
        
    #     length = len(profit_loss_change)
    #     total = 0.0

    #     for number in profit_loss_change:
    #         total += number
        
    #     return total / length





     #greatest increase in profits (date & amount) over entire period

        # max_profit = list[]
        # max_profit = max()
        # print(max_profit)

     #greates decrease in losses (date and amount) over entire period

       min_profit = list[]
       min_profit = min()
       print(min_profit)


     #print("Financial Analysis")
     #print("-----------------------------")

     #print("Total Months: {total_months}")
     #print("Total: {net_total}")
     #print("Average Change: ")
     #print("Greatest Increase in Profits: ")
     #print("Greatest Decrease in Profits")

