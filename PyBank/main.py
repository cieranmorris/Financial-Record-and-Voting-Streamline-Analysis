
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
with open(budget_data_csv) as csvfile:
    budget_data = csv.reader(csvfile, delimiter= ",")

    #print(budget_data)

    csv_header = next(budget_data)
    print(f"CSV Header: {budget_data}")

    #count total number of months in CSV
    #total_months = len(list(budget_data)) -- Farshad said don't use

   total_months =0
   for row in budget_data:
       total_months = total_months + 1
       print(total_months)

     #net total amount of Profit/Losses over the entire period
   total = 0
   for row in budget_data:
         #total Profit/Losses in column 1
         #get Profit/losses into a python lists you created
         total_months.append(row[0])

         profit_loss.append(int(row[1]))

         #calculate the total
   net_total_amount = 0
   for x in profit_loss:
           net_total_amount = x + net_total_amount
           print(net_total_amount)



     #Changes in Profit/Losses over entire period
     profit_change = [profit_loss[x + 1]] - profit_loss[x] for x in range(0, len(profit_loss)-1)]





     #Averages of changes
     average_profit_changes = average(profit_change)
     print(average_profit_changes)


    # see if this code section is necessary at this point?
    # def average(profit_loss_change):
        
    #     length = len(profit_loss_change)
    #     total = 0.0

    #     for number in profit_loss_change:
    #         total += number
        
    #     return total / length





     #greatest increase in profits (date & amount) over entire period

        max_profit = list[]
        max_profit = max(profit_change)
        print(max_profit)

     #greates decrease in losses (date and amount) over entire period

       min_profit = list[]
       min_profit = min(profit_change)
       print(min_profit)


     print("Financial Analysis")
     print("-----------------------------")

     print("Total Months: {total_months}")
     print("Total: {net_total_amount}")
     print("Average Change: {average_profit_changes}")
     print("Greatest Increase in Profits: {max_profit}")
     print("Greatest Decrease in Profits: {min_profit}")

