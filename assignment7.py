# Exercise 1:
# Create a numpy array containing the numbers from 1 to 10, and then reshape it to a 2x5 matrix.

# import numpy as np
#
# # Create a numpy array with numbers from 1 to 10
# array = np.arange(1, 11)
#
# # Reshape the array into a 2x5 matrix
# matrix = array.reshape(2, 5)
# print(matrix)

# Exercise 2:
# Create a numpy array containing the numbers from 1 to 20, and then extract the elements between the 5th and 15th index.

# import numpy as np
#
# # Create a numpy array with numbers from 1 to 20
# array = np.arange(1, 21)
#
# # Extract elements between the 5th and 15th index
# extracted_elements = array[5:15]
#
# print(extracted_elements)

# Exercise 3:
"""Create a Pandas series with the following data: {'apples': 3, 'bananas': 2, 'oranges': 1}. Then,
add a new item to the series with the key 'pears' and the value 4. """

# import pandas as pd
#
# # Create a Pandas series with the initial data
# data = {'apples': 3, 'bananas': 2, 'oranges': 1}
# series = pd.Series(data)
#
# # Add a new item to the series
# series['pears'] = 4
#
# print(series)

# Exercise 4:
# Create a dataframe with the following columns: name, age, and gender. The dataframe should have 10 rows of data.
#
import pandas as pd
#
# Define the data
data = {
    'name': ['Anna', 'Annie', 'Dexter', 'Bobby', 'Sanya', 'Nancy', 'Jimmy', 'George', 'Bunny', 'Jenny'],
    'age': [25, 30, 22, 28, 35, 27, 29, 24, 26, 31],
    'gender': ['Female', 'Female', 'Male', 'male', 'Female', 'Female', 'Male', 'male', 'Male', 'Female']
}

# Create the DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)


# Exercise 5:
"""Add a new column to the data frame created in question 4, called occupation.
The values for this column should be Programmer, Manager, and Analyst, corresponding to the rows in the dataframe."""


# Define the new column values
occupations = ['Programmer', 'Manager', 'Analyst', 'Programmer', 'Manager',
               'Analyst', 'Programmer', 'Manager', 'Analyst', 'Programmer']

# Add the new column to the DataFrame
df['occupation'] = occupations

# Display the updated DataFrame
print(df)

# Exercise 6:
# Select the rows of the dataframe where the age is greater than or equal to 30.

# Select rows where age is greater than or equal to 30
filtered_df = df[df['age'] >= 30]

# Display the filtered DataFrame
print(filtered_df)



# Exercise 7:
# Convert this dataframe to a csv file and read that csv file, finally display the contents.

import pandas as pd

# Assuming the previous DataFrame is already defined as 'df'
# Convert the DataFrame to a CSV file
df.to_csv('dataframe.csv', index=False)

# Read the CSV file into a new DataFrame
new_df = pd.read_csv('dataframe.csv')

# Display the contents of the new DataFrame
print(new_df)

