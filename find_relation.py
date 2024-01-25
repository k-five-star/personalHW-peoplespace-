import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'stock_data.csv'  # Update this path to the location of your CSV file
stock_data = pd.read_csv(file_path) # Read the CSV file into a DataFrame

# Convert 'Date' to datetime and sort data
stock_data['Date'] = pd.to_datetime(stock_data['Date']) # Convert 'Date' column to datetime
stock_data.sort_values(by=['name', 'Date'], inplace=True) # Sort the data by 'name' and 'Date'

# Calculating daily return for each stock
stock_data['Daily_Return'] = stock_data.groupby('name')['Close'].pct_change() * 100 # Calculate daily return for each stock

# Updated groupings based on the provided categories 
updated_grouped_stocks = {
    'Communication Services': ['XLC'],
    'Consumer Discretionary': ['XLY'],
    'Consumer Staples': ['XLP'],
    'Energy': ['XLE'],
    'Financials': ['XLF'],
    'Health Care': ['XLV'],
    'Industrials': ['XLI'],
    'Materials': ['XLB'],
    'Real Estate': ['XLRE'],
    'Technology': ['XLK'],
    'Utilities': ['XLU']
}

# Calculating average daily return for each new group
updated_average_returns = {} # Create an empty dictionary to store the average daily return for each group
for group, stocks in updated_grouped_stocks.items(): # Iterate through each group and its stocks
    group_data = stock_data[stock_data['name'].isin(stocks)] # Filter the data for the stocks in the group
    updated_average_returns[group] = group_data.groupby('Date')['Daily_Return'].mean() # Calculate the average daily return for the group

updated_average_returns_df = pd.DataFrame(updated_average_returns) # Convert the dictionary to a DataFrame

# Calculating the correlation matrix for the new groups
updated_correlation_matrix = updated_average_returns_df.corr() # Calculate the correlation matrix

# Creating a heatmap to visualize the correlations of the new groups
plt.figure(figsize=(10, 8)) # Set the size of the figure
sns.heatmap(updated_correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1) # Create the heatmap
plt.title('Correlation Matrix of Average Daily Returns Between New Groups') # Set the title of the heatmap
plt.show()
