print("Hello from PyPoll!")

#import modules
import os
import csv
import statistics as avg

#create path to csv file and rename
election_data_csv = os.path.join("Resources", "election_data.csv")
print(election_data_csv)

#Lists to store data to analyze later
total_votes_cast = []
candidate_list = []
candidate_votes = []
popular_vote = []

#csvreader to read csv file
election_data = csv.reader(election_data_csv, delimiter = ",")
print(election_data)

#skip header row in csv file
csv_header = next(election_data)
print(f"CSV Header: {csv_header}")


#total number of votes cast - add up # of voter IDs
#need to convert voter IDs into individual numerical values?
total_votes_cast = 0
for row in election_data:
    total_votes_cast = total_votes_cast + 1
    print(total_votes_cast)

#not correct - indicating there were only 26 votes
#do something in regards to totaling all values in column 0
#append to lists tomorrow