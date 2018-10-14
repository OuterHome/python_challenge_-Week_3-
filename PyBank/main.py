# This script analyzes financial records to produce a .csv file called budget_data.csv.
# The analysis performed includes:
#   The total number of months included in the dataset
#   The total net amount of "Profit/Losses" over the entire period
#   The average change in "Profit/Losses" between months over the entire period
#   The greatest increase in profits (date and amount) over the entire period
#   The greatest decrease in profits (date and amount) over the entire period

# import pandas to help manage and analyze the budget data
import pandas as pd

# Use pandas to read the data
budget = "budget_data.csv"
budget_data_pd = pd.read_csv(budget)

# Collect a list of all columns in the dataframe
budget_data_pd.columns

# Calculate the total number of months included in the dataset (86 total)
total_num_months = len(budget_data_pd["Date"])

# Calculate the total net amount of "Profit/Losses" over the entire period ($38,382,578)
total_net = budget_data_pd["Profit/Losses"].sum()

# Create a new difference column in the dataframe
average_change = budget_data_pd["Profit/Losses"].diff()
budget_data_pd = budget_data_pd.assign(Difference=(average_change).values)

# Calculate the average change in "Profit/Losses" between months over the entire period ($-2315.12)
average_change = budget_data_pd["Profit/Losses"].diff().mean()

# Calculate the greatest increase in profits (date and amount) over the entire period ($1,926,159)
greatest_inc_profit = budget_data_pd["Profit/Losses"].diff().max()
greatest_inc_profit_date = budget_data_pd.loc[budget_data_pd["Difference"] == greatest_inc_profit]

# Calculate the greatest decrease in profits (date and amount) over the entire period (-$2,196,167)
greatest_dec_profit = budget_data_pd["Profit/Losses"].diff().min()
greatest_dec_profit_date = budget_data_pd.loc[budget_data_pd["Difference"] == greatest_dec_profit]

## Tried this but it didn't work right, to add $ to parts of the list
## greatest_inc_profit_date.loc[25, "Difference"] = greatest_inc_profit_date.loc[25, "Difference"].map("${:}".format)

# Convert greatest increase and decrease dataframes to lists
greatest_inc_profit_date_list = greatest_inc_profit_date[["Date", "Difference"]].values.tolist()
greatest_dec_profit_date_list = greatest_dec_profit_date[["Date", "Difference"]].values.tolist()

# Place all data in summary dataframe
budget_output = pd.DataFrame({"Total Number of Months":[total_num_months],
                            "Total Net Profit in $":[total_net],
                            "Avg Profit/Loss Change in $":[average_change],
                            "Greatest Monthly Profit Increase in $":greatest_inc_profit_date_list,
                            "Greatest Monthly Profit Decrease in $":greatest_dec_profit_date_list}, index=[''])

# Print summary in terminal in requested style
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_num_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_inc_profit_date_list}")
print(f"Greatest Decrease in Profits: {greatest_dec_profit_date_list}")

# Export summary_table to .csv file
budget_output.to_csv("budget_output.csv", index=False, header=True)

