print("Hello from PyBank!")

#import module and csv reader
import os
import csv


csvpath = os.path.join("Resources", "budget_data.csv")
print(csvpath)

#Lists to store data
total_months = []
net_total = []
profit_loss_changes = []
average_change = []
profit_increase = []
loss_decrease = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #count total number of months in CSV
    total_months = len(list(csvreader))
    print(total_months)
     
    total = 0
   

     #net total amount of Profit/Losses over the entire period

    for row in csvreader:
         #total Profit/Losses in column 1
         #get Profit/losses into a python list

        total_profit_loss = int(row[1])
        net_total = total_profit_loss + total
        print(net_total)



     #Changes in Profit/Losses over entire period 



     #Averages of changes


     #greatest increase in profits (date & amount) over entire period

     #greates decrease in losses (date and amount) over entire period




     #print("Financial Analysis")
     #print("-----------------------------")

     #print("Total Months: {total_months}")
     #print("Total: {net_total}")
     #print("Average Change: ")
     #print("Greatest Increase in Profits: ")
     #print("Greatest Decrease in Profits")

