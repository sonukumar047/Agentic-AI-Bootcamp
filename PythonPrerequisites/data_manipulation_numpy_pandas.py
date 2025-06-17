import pandas as pd
import numpy as np

# -----------------------------------------
# 1. Create a sample DataFrame
# -----------------------------------------
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, np.nan, 40],
    'Salary': [50000, 60000, 70000, 80000, np.nan],
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT']
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# -----------------------------------------
# 2. Handling Missing Values
# -----------------------------------------
print("\nFilling NaN in Age with mean:")
df['Age'].fillna(df['Age'].mean(), inplace=True)

print("Dropping rows with missing Salary:")
df.dropna(subset=['Salary'], inplace=True)

# -----------------------------------------
# 3. Apply NumPy functions
# -----------------------------------------
df['Log_Salary'] = np.log(df['Salary'])
df['Age_Squared'] = np.square(df['Age'])

print("\nWith NumPy applied:\n", df)

# -----------------------------------------
# 4. Filtering Data
# -----------------------------------------
print("\nEmployees in IT Department with Age > 30:")
print(df[(df['Department'] == 'IT') & (df['Age'] > 30)])

# -----------------------------------------
# 5. Sorting Data
# -----------------------------------------
sorted_df = df.sort_values(by='Salary', ascending=False)
print("\nSorted by Salary Descending:\n", sorted_df)

# -----------------------------------------
# 6. Aggregation and Grouping
# -----------------------------------------
grouped = df.groupby('Department')[['Salary', 'Age']].mean()
print("\nAverage Salary and Age by Department:\n", grouped)

# -----------------------------------------
# 7. Adding Derived Columns
# -----------------------------------------
df['Tax'] = df['Salary'] * 0.1
df['Net_Salary'] = df['Salary'] - df['Tax']

print("\nAfter Adding Tax and Net Salary:\n", df)

# -----------------------------------------
# 8. Mapping & Replacing Values
# -----------------------------------------
dept_map = {'HR': 'Human Resources', 'IT': 'Information Tech', 'Finance': 'Accounts'}
df['Department'] = df['Department'].map(dept_map)

print("\nMapped Department Names:\n", df)

# -----------------------------------------
# 9. Renaming Columns
# -----------------------------------------
df.rename(columns={'Name': 'Employee Name'}, inplace=True)
print("\nAfter Renaming:\n", df)

# -----------------------------------------
# 10. Reset Index if Needed
# -----------------------------------------
df.reset_index(drop=True, inplace=True)
print("\nFinal Cleaned DataFrame:\n", df)

# -----------------------------------------
# Summary:
# - Combine Pandas + NumPy for efficient transformation.
# - Use `fillna`, `dropna`, `apply`, and NumPy math functions.
# - Perform filtering, aggregation, and derived column creation.
# - Clean data by renaming, mapping, and resetting index.
# -----------------------------------------
