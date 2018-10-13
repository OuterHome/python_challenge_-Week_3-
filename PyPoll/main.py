# This script analyzes votes cast in an election, and calculates:
#   The total number of votes cast
#   A complete list of candidates who received votes
#   The percentage of votes each candidate won
#   The total number of votes each candidate won
#   The winner of the election based on popular vote.
# It also prints the analysis to the terminal, and exports a text file
# with the results. 

  #Election Results (EXAMPLE)
  #-------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------

# import pandas to help manage and analyze the budget data
import pandas as pd

# Use pandas to read the data
df_votes = pd.read_csv("../PyPoll/election_data.csv", encoding = "utf-8", sep=",")

# Use pandas for a cursory look at the data
print(df_votes.head())

