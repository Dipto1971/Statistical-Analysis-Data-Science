def bivariate_stats(df, label, roundto=4):
  import pandas as pd
  from scipy import stats

  output_df = pd.DataFrame(columns=['p-value', 'r-value', 'y = m(x) + b', 'F', 'X2'])

  for feature in df:
    # There Might be missing values for which analysis can come up with inaccuracy
    if feature != label:
     if pd.api.types.is_numeric_dtype(df[feature]) and pd.api.types.is_numeric_dtype(df[label]):
       # Process N2N relationships
       m, b, r, p, err = stats.linregress(df[feature], df[label])
       output_df.loc[feature] = [round(p, roundto), round(r, roundto), f"y={round(m, roundto)}x+{round(b, roundto)}", '-', '-']
     elif not pd.api.types.is_numeric_dtype(df[feature]) and not pd.api.types.is_numeric_dtype(df[label]):
       #  Process C2C relationships
       contingency_table = pd.crosstab(df[feature], df[label])
       chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
       
       output_df.loc[feature] = [round(p, roundto), '-', '-', '-', round(chi2, roundto)]
     else:
       # Process C2N & N2C relationships
       if pd.api.types.is_numeric_dtype(df[feature]):
        num = feature
        cat = label
       else:
        num = label
        cat = feature

       groups = df[cat].unique()
       group_lists = []
       for g in groups:
        group_lists.append(df[df[cat] == g][num])

       f, p = stats.f_oneway(*group_lists) # same as (group_lists[0], group_lists[1], ..., group_lists[n])

       output_df.loc[feature] = [round(p, roundto), '-', '-', round(f, roundto), '-']
  # return output_df.sort_values(by=['r-value'], ascending=False)
  #From strongest correlation to weakest correlation

  return output_df


