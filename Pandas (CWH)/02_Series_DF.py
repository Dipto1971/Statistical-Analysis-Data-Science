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
