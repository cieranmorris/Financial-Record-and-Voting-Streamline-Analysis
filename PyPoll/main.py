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


        #associate votes to tallied individual candidate names - for loop?
    for x in individual_candidate_votes:
        votes_per_candidate = individual_candidate_votes.get(x)

        #calculate % of each candidates' votes / total votes
        percent = float(votes_per_candidate) / float(total_votes) * 100
        #print(percent)

        #\n to break for loop because data file is so large
        #believe I need multiple dictionaries for a singular result output
        percent_results = (f"{x}: {percent:.3f}% ({individual_candidate_votes})\n")

        #print results
        #print(percent_results)


        #find the winner based on popular vote
        if votes_per_candidate > winners_votes:
            winners_votes = votes_per_candidate
            winner = x
    
with open(save_file, "w") as txtfile:
    summary_table = (f"Election Results\n")
    f"-------------------------\n"
    f"Total Votes {total_votes}\n"
    f"-------------------------\n"
print(summary_table)








# print("Election Results")
# print("---------------------------")
# print(f"Total Votes: {total_votes}")
# print("---------------------------")
# print("")



