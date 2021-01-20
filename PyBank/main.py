print("Hello from PyBank!")

#import module and csv reader
import os
import csv


csvpath = os.path.join("Resources", "budget_data.csv")
print(csvpath)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #count total number of months in CSV
    count = len(list(csvreader))
    print(count)
     

     #net total amount of Profit/Losses over the entire period


     #Changes in Profit/Losses over entire period 



     #Averages of changes


     #greatest increase in profits (date & amount) over entire period

     #greates decrease in losses (date and amount) over entire period

     