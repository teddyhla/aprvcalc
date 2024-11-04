import pandas as pd

df = pd.read_csv('romeo/ROMEODevelopment_DataDictionary_2024-10-25.csv')

tdf = df[df['Variable / Field Name'].str.contains('t0')]

def rep_bind(df,replist):
    result_df = df.copy()
    for i in replist:
        temp_df = df.copy()
        print(i)
        temp_df[['Variable / Field Name', 'Form Name']]= temp_df[['Variable / Field Name', 'Form Name']].replace(r'^t0',i,regex=True)
        result_df = pd.concat([result_df, temp_df],ignore_index=True)
        print(result_df)
    return result_df

varlist = ['t1','t2','t3','t4','t5']

newdf = rep_bind(df = tdf, replist = varlist)

newdf.to_csv('allconcatlist.csv')

d2 = pd.read_csv('romeo/26draft.csv')

cols = d2.columns
cols = list(cols)
cols = list(filter(lambda x: 'Unnamed:' not in x, cols))

d3 = d2[cols]

d3.to_csv('cleanedup.csv')