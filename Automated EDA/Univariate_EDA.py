def univariate(df):
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  import seaborn as sns

  output_df = pd.DataFrame(columns = ['type', 'count', 'missing', 'unique', 'mode', 'min', 'Q1',
                                      'median', 'Q3', 'max', 'mean', 'std', 'skewness', 'kurtosis'])
  
  for col in df:
    # Calculate metrics that apply to all dtypes
    dtype = df[col].dtype
    count = df[col].count()
    missing = df[col].isnull().sum()
    unique = df[col].nunique()
    mode = df[col].mode()[0]

    if pd.api.types.is_numeric_dtype(df[col]):
      # Calculate metrics that apply only to numeric features
      min = df[col].min()
      Q1 = df[col].quantile(0.25)
      median = df[col].median()
      Q3 = df[col].quantile(0.75)
      max = df[col].max()
      mean = df[col].mean()
      std = df[col].std()
      skewness = df[col].skew()
      kurtosis = df[col].kurtosis()

      output_df.loc[col] = [dtype, count, missing, unique, mode, min, Q1,
                            median, Q3, max, mean, std, skewness, kurtosis ]

      sns.histplot(data=df, x=col)     
      plt.show()              
    else:
      output_df.loc[col] = [dtype, count, missing, unique, mode, '-', '-',
                            '-', '-', '-', '-', '-', '-', '-']
      sns.countplot(data=df, x=col)
      plt.show()
  # output_df.to_csv('EDA.csv')
  return output_df