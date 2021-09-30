import pandas as pd
import numpy as np

data = data = {'Name1': ['Tom', 'Joseph', 'Krish', 'John', 'John', 'Sam', 'Bill'], 'Name2' : ['Matt', 'Joseph', 'Kayle', 'Kyle', 'John', 'Sammy', 'Bill'], 'Number' : [1,2,3,4,5,6,7]}
df = pd.DataFrame(data)

#Code to allow you to replace values with condition
#This time we will change the Number column's value to 1 if we have the same value for Name1 and Name2

for i in range(len(df)):
    if df['Name1'][i] == df['Name2'][i]:
        df.loc[i, 'Number'] = 1
    else:
        pass

# You can add more condition on top of this for loop
# For example:
for i in range(len(df)):
    if df['Name1'][i] == 'Bill':
        pass
    # This way you won't have 7 from Number column changed to 1
    else:
        for j in range(len(df)):
            if df['Name1'][j] == df['Name2'][j]:
                df.loc[j, 'Number'] = 1
            else:
                pass

# Or you can add values to the column

for i in range(len(df)):
    if df['Name1'][i] != 'Bill':
        df['Name1'][i] = df['Name1'][i] + ', Kim'
    else:
        for j in range(len(df)):
            if df['Name1'][j] == df['Name2'][j]:
                df.loc[j, 'Number'] = 1
            else:
                pass