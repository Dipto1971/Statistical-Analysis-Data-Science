import numpy as np
import pandas as pd

# Creating a Dictionary

student_data_set = {
    "name": ["student1", "student2", "student3"],
    "id" : ["2022-1", "2022-2", "2022-3"],
    "CGPA" : [3.55, 4.0, 3.9]
}

df = pd.DataFrame(student_data_set);
# Dataframe converts the dictionary into a table format excel sheet
print(df)

df.to_csv("./Pandas (CWH)/student_data.csv")
# This will create a csv file with the name student_data.csv and store the data in it

df.to_csv("./Pandas (CWH)/student_data_no_index.csv", index=False)
# This will create a csv file with the name student_data_no_index.csv and store the data in it without the index

df.head(2)
# This will print the first 2 rows of the dataframe

df.tail(2)
# This will print the last 2 rows of the dataframe

Stat_data = df.describe()
print(Stat_data)
# count, mean, std, min, 25%, 50%, 75%, max of the dataframe
