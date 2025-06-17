# -----------------------------------------
# 1. Importing Pandas
# -----------------------------------------
import pandas as pd

# -----------------------------------------
# 2. Creating a Series
# -----------------------------------------
data = [10, 20, 30]
labels = ['a', 'b', 'c']

series = pd.Series(data, index=labels)
print("Series:\n", series)
print("Access element by label:", series['b'])

# -----------------------------------------
# 3. Creating a DataFrame
# -----------------------------------------
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}

df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# -----------------------------------------
# 4. Reading & Writing Files
# -----------------------------------------
# df = pd.read_csv('data.csv')
# df.to_csv('output.csv', index=False)

# -----------------------------------------
# 5. Inspecting Data
# -----------------------------------------
print("\nHead:\n", df.head())
print("Tail:\n", df.tail())
print("Info:")
df.info()
print("Describe:\n", df.describe())

# -----------------------------------------
# 6. Accessing Columns and Rows
# -----------------------------------------
print("Single Column:\n", df['Name'])
print("Multiple Columns:\n", df[['Name', 'Age']])

print("Row by index (iloc):\n", df.iloc[1])   # Bob
print("Row by label (loc):\n", df.loc[0])     # Alice

# -----------------------------------------
# 7. Filtering Data
# -----------------------------------------
print("Age > 25:\n", df[df['Age'] > 25])
print("City is Mumbai:\n", df[df['City'] == 'Mumbai'])

# -----------------------------------------
# 8. Adding, Updating, and Deleting Columns
# -----------------------------------------
df['Salary'] = [50000, 60000, 70000]  # Add column
df['Age'] = df['Age'] + 1             # Update column
df.drop('City', axis=1, inplace=True) # Delete column

print("\nUpdated DataFrame:\n", df)

# -----------------------------------------
# 9. Handling Missing Values
# -----------------------------------------
df2 = pd.DataFrame({
    'Name': ['X', 'Y', 'Z'],
    'Score': [90, None, 80]
})
print("\nWith NaN:\n", df2)

print("Fill NaN with 0:\n", df2.fillna(0))
print("Drop rows with NaN:\n", df2.dropna())

# -----------------------------------------
# 10. GroupBy and Aggregation
# -----------------------------------------
df3 = pd.DataFrame({
    'Department': ['HR', 'HR', 'IT', 'IT'],
    'Salary': [30000, 40000, 50000, 60000]
})
grouped = df3.groupby('Department').mean()
print("\nGrouped by Department:\n", grouped)

# -----------------------------------------
# Summary:
# - Pandas has Series (1D) and DataFrame (2D).
# - Use `read_csv()`, `to_csv()` to load/save data.
# - Use `loc[]`, `iloc[]`, and conditions for filtering.
# - `groupby()`, `fillna()`, `dropna()` are essential tools.
# -----------------------------------------
