# This script analyzes financial records to produce a .csv file called budget_data.csv.
# The analysis performed includes:
#   The total number of months included in the dataset
#   The total net amount of "Profit/Losses" over the entire period
#   The average change in "Profit/Losses" between months over the entire period
#   The greatest increase in profits (date and amount) over the entire period
#   The greatest decrease in profits (date and amount) over the entire period

# import pandas to help manage and analyze the budget data
import pandas as pd

# save the path to the raw dataset in a variable
#budget_data = "C:\Users\james\Desktop\LearnPython\Gitlab\python_challenge\PyBank", encoding = "utf-8"

# Use pandas to read the data
budget_data_pd = pd.read_csv(r"C:\Users\james\Desktop\LearnPython\Gitlab\python_challenge\PyBank\budget_data.csv", encoding = "utf-8", sep=",")

## Use pandas for a cursory data analysis
budget_data_pd.head()

# Collect a list of all columns in the dataframe
budget_data_pd.columns

# Calculate and print the total number of months included in the dataset (86 total)
total_num_months = len(budget_data_pd["Date"])
print(f"Total Months: {total_num_months}")

# Calculate and print the total net amount of "Profit/Losses" over the entire period ($38,382,578)
total_net = budget_data_pd["Profit/Losses"].sum()
print(f"Total: ${total_net}")

# Create a new difference column in the dataframe
average_change = budget_data_pd["Profit/Losses"].diff()
budget_data_pd = budget_data_pd.assign(Difference=(average_change).values)

# Calculate and print the average change in "Profit/Losses" between months over the entire period ($-2315.12)
average_change = budget_data_pd["Profit/Losses"].diff().mean()
print(f"Average Change: ${average_change}")

# Calculate and print the greatest increase in profits (date and amount) over the entire period ($1,926,159)
greatest_inc_profit = budget_data_pd["Profit/Losses"].diff().max()
greatest_inc_profit_date = budget_data_pd.loc[budget_data_pd["Difference"] == greatest_inc_profit]


#print greatest_inc_profit_datein Profits: ($" + (greatest_inc_profit_date[["Date","Difference"]]) + ")")
#print("Greatest Increase in Profits: ($)") 
print((greatest_inc_profit_date[["Date","Difference"]]))

# Calculate and print the greatest decrease in profits (date and amount) over the entire period (-$2,196,167)
greatest_dec_profit = budget_data_pd["Profit/Losses"].diff().min()
greatest_dec_profit_date = budget_data_pd.loc[budget_data_pd["Difference"] == greatest_dec_profit]
#print("Greatest Decrease in Profits: ($" + str(greatest_dec_profit_date[["Date", "Difference"]]) + ")")
#print("Greatest Decrease in Profits: ($)")
greatest_dec_profit_date.
print((greatest_dec_profit_date[["Date", "Difference"]]))

# remove header from dataframe

#budget_data_pd.columns = budget_data_pd_noheader.iloc[0]
#budget_data_pd = budget_data_pd.columns[1:]
#budget_data_pd.to_csv

## FIIIIIIIXXXXXXX SUMMMMARRRY TABLE LAST 2 VALUES!!!!!!
# Place all data in summary dataframe and print in terminal
summary_table = pd.DataFrame({
    "Total Number of Months":[total_num_months],
    "Total Net Profit":[total_net],
    "Avg Profit/Loss Change":[average_change],
    "Greatest Profit Increase":[greatest_inc_profit_date],
    "Greatest Profit Decrease":[greatest_dec_profit_date],
})

summary_table.head()

# Export summary_table to .csv file
summary_table.to_csv("summary_table.csv", index=False, header=True)
