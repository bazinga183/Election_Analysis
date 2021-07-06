import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0

#Create an array for candidates
candidate_options = []

#Declare an empty dictionary
candidate_votes = {}

#How to determine a winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: read and analyze data here.
     file_reader = csv.reader(election_data)

     #Print each row in the CSV file
     headers = next(file_reader)

     for row in file_reader:
          #Increment total_votes for every row
          total_votes += 1

          #Print the candidate name from each row
          candidate_name = row[2]

          #Add the candidate name to the candidate list if not already present
          if candidate_name not in candidate_options:
               
               #Add candidates to the list
               candidate_options.append(candidate_name)

               #Track the candidates' vote count
               candidate_votes[candidate_name] = 0

          #Add a vote if it is cast for a cadidate
          candidate_votes[candidate_name] += 1

          #Iterate throught the candidate list
     for candidate_name in candidate_votes:

          #Retrieve count of a candidate
          votes = candidate_votes[candidate_name]

          #Calculate the percentage of votes
          vote_percentage = float(votes) / float(total_votes) * 100

          print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
          
          #To do: print out each candidate's name, vote count, and percentafe of votes to the terminal
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               #If true, set winning_count = votes and winning_percent = to vote_percentage
               winning_count = votes
               winning_percentage = vote_percentage
               winning_candidate = candidate_name

#The winner of the election
     winning_candidate_summary = (
          f"---------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote Count: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"---------------------\n"
     )          
     print(winning_candidate_summary)
