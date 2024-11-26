import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r'C:\Users\Nitesh\Desktop\pyton\Book1.csv'
data = pd.read_csv(file_path)

# Inspect the data
print("First few rows of the data:")
print(data.head())

# Display data types of each column
print("\nData types of each column:")
print(data.dtypes)

# Display summary statistics
print("\nSummary statistics:")
print(data.describe(include='all'))

# Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Drop duplicates
data = data.drop_duplicates()
print("\nData after dropping duplicates:")
print(data.head())

# Exploratory Data Analysis

# Plot a histogram of the area codes
plt.figure(figsize=(10, 6))
data['Area.code'].plot(kind='hist', bins=10, title='Distribution of Area Codes')
plt.xlabel('Area Code')
plt.ylabel('Frequency')
plt.show()

# Scatter plot of Area Code vs Contact
plt.figure(figsize=(10, 6))
plt.scatter(data['Area.code'], data['Contact'])
plt.title('Area Code vs Contact')
plt.xlabel('Area Code')
plt.ylabel('Contact')
plt.show()

# Group and Aggregate Data

# Group by country and get the count of people in each country
country_counts = data.groupby('Country').size()
print("\nCount of people in each country:")
print(country_counts)

# Plot the number of people per country
plt.figure(figsize=(10, 6))
country_counts.plot(kind='bar', title='Number of People per Country')
plt.xlabel
