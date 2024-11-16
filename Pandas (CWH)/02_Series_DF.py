import numpy as np
import pandas as pd

# Series
series = pd.Series(np.random.rand(35))
type(series)
print(series)

# DataFrame
data_frame = pd.DataFrame(np.random.rand(334, 5), index=np.arange(334))
# column = 5, row = 334, np.arrange is used to set index
print(data_frame)
print(type(data_frame))

# Statistics on DataFrame
stat_df = data_frame.describe()
print(stat_df)

# Transpose
print(data_frame.T)

# Sorting
print(data_frame.sort_index(axis=1, ascending=False))
# Here, axis=1 means column wise sorting, axis=0 means row wise sorting

# Dataframe is created using combination of Series
print(type(data_frame[0]))




# VIEW: View is a shallow copy of the dataframe,
# any changes made in the view will be reflected in the original dataframe
# In memory location, both the dataframes will be directed to the same location
# new_df = data_frame.copy()
# new_df[0][0] = 0.5


#  .loc and .iloc
print(data_frame.iloc[0, 0])
# This will return the value at 0th row and 0th column
# whatever is the index, it will be considered as the row and column number

print(data_frame.loc[0, 0])
# This will return the value at 0th row and 0th column
# Actual names should be used as row and column names

# Query
print(data_frame.loc[(data_frame[0] > 0.5) & (data_frame[3] > 0.5)])
# This checks conditions on column 0 and 3 and returns the rows which satisfy the condition
