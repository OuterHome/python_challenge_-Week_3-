# This script analyzes votes cast in an election, and calculates:
#   -The total number of votes cast
#   -A complete list of candidates who received votes
#   -The percentage of votes each candidate won
#   -The total number of votes each candidate won
#   -The winner of the election based on popular vote.
# It also prints the analysis to the terminal, and exports a text file
# with the results. 

# import pandas to help manage and analyze the budget data
import pandas as pd

# Use pandas to read the data
votes = "election_data.csv"
df_votes = pd.read_csv(votes)

# Calculate total number of votes cast
total_votes = df_votes["Voter ID"].count()

# Compute complete list of candidates who received votes
got_votes = df_votes["Candidate"].unique()

# Calculate the percentage of votes each candidate received
grouped_vote = df_votes.groupby(["Candidate"]).count()
perc_vote = (grouped_vote / total_votes)
perc_vote_sized = perc_vote.drop(columns=["County"])*100

# Calculate the total number of votes each candidate received
votes_received = grouped_vote.drop(columns=["County"])

# Calculate the winner of the election based on popular vote
winner = votes_received.sort_values(["Voter ID", "Candidate"], ascending=False)

# Rename "Voter ID" column to "Percent of Vote"
perc_vote_sized_rename = perc_vote_sized.rename(columns={'Voter ID': 'Percent of Vote'})

# Rename "Voter ID" column to "Percent of Vote"
votes_received_rename = votes_received.rename(columns={'Voter ID': 'Total Votes'})

# Join percent and total vote dataframes
joined_summary = perc_vote_sized_rename.join(votes_received_rename)

# Change percent of vote formatting
joined_summary["Percent of Vote"]=joined_summary["Percent of Vote"].map("{:.3f}%".format)

#Sort and explicitly define a sorted summary dataframe
joined_summary_sorted = joined_summary.sort_values(by=['Total Votes'], ascending=False)

#Print Analysis to Terminal
print("Election Results")
print("----------------------------------")
print("Total Votes: " + str(total_votes))
print("----------------------------------")
print(joined_summary_sorted)
print("----------------------------------")
print("Winner: "+ winner.index[0])
print("----------------------------------")

# Export summary_table to .csv file
joined_summary_sorted.to_csv("vote_output.csv", index=True, header=True)

