#import modules
import os
import csv


#create path to csv file and rename
election_data_csv = os.path.join("Resources", "election_data.csv")
save_file = os.path.join("Analysis", "election_data_textfile.txt")

#Lists to store data to analyze later
candidate_list = []
total_votes_cast = []

#Define variables and set initial values
total_votes = 0
popular_vote = 0
winner = ""
winners_votes = 0

#create a dictionary of lists for the candidate names and votes?
individual_candidate_votes = {}

#csvreader to read csv file
with open (election_data_csv, newline = "", encoding = "ISO-8859-1") as csvfile:
    election_data = csv.reader(csvfile, delimiter = ",")
    #print(election_data)

    #skip header row in csv file
    csv_header = next(election_data)
    #print(f"CSV Header: {csv_header}")


    #total number of votes cast - add up # of voter IDs
    #need to convert voter IDs into individual numerical values?
    for row in election_data:
        total_votes += 1
       
        #assign individual candidate ID for for each row, starting in Row 2
        individual_candidate = row[2]

        #if statement for if the candidate names' do/don't match
        if individual_candidate not in candidate_list:
            candidate_list.append(individual_candidate)

            #set dictionary value to zero for the for loop
            individual_candidate_votes[individual_candidate] = 0

        #as for loop finds associated names for individual candidates, add 1
        individual_candidate_votes[individual_candidate] = individual_candidate_votes[individual_candidate] + 1