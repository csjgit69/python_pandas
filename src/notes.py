import pandas as pd

# .loc and .iloc work on rows
# ['name'] directly on dataframes works on columns

#df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
print('\n****** the raw DataFrame \n')
print(df.head())

# .loc and .iloc are index operators (rows)
print('\n****** .iloc example\n')
print(df.loc['Store 1'])

#['name'] on a dataframe works on columns
print('\n****** column selection, direct indexing \n')
print(df['Item Purchased'])

#chaing works but it returns a copy, most operations return a 'view' it affects how changes can be made
print('\n****** example of chaining, used to sub select, i think \n')
print(df.loc['Store 1']['Cost'])

# can use .loc and a split operator with 2d selection
print('\n****** another way to column select, with slicing\n')
print(df.loc[:,['Item Purchased']])

# can use .loc and a split operator with 2d selection
print('\n****** another way to column select, with slicing, and passing a list of columns\n')
print(df.loc[:,['Item Purchased', 'Cost']])

# drop example, it doesn't change dataframe, returns new copy modified
print('\n****** example of drop not changing dataframe, returns new copy modified\n')
print('df drop return value\n',df.drop('Store 1'))
print('\ndf after drop', df)

# del key work does affect dataframe, making a copy to show
df2 = df.copy()
print('\n****** example of del keyword on dataframes\n')
print('\ndf2 before del: \n',df2)
del df2['Name']
print('\ndf2 after del \'name\': \n', df2)

#adding a column is easy
print('\ndf before adding location: \n', df)
df['Location'] = None
print('\ndf after adding location None: \n', df)

#messing with the core data
costs = df['Cost']
costs += 2
print('\ncosts before copy/change:\n', df['Cost'], '\n\ncosts series:\n', costs)

# how to use iPython "Magic Methods" inside a console like Spyder
# shell commands are kernal specific, these don't work on Windows for example
#print('\n****** shell commands/Magic Methods in a console\n')
#ipy = get_ipython()
#print(ipy.magic('ls'))
#print(ipy.magic('cat olympics.csv'))
#print(ipy.magic('cat $PATH'))

# read in a CSV file to process it. part of Panda's is file reading/processing methods
print('\n****** working on a CSV file\n')
df2 = pd.read_csv('olympics.csv')
df2 = pd.DataFrame(df2) # let Spyder know this is a Dataframe
print(df.head())

# index index (row names) set by 'index_col' 0 is first column.
# column names set by the first row read in, skiprows tells Pandas to use 2nd row for column names
df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1)
df = pd.DataFrame(df) # let Spyder know this is a Dataframe
print(df.head())
print(df.columns)

# make the column headers pretty
# column names are 01
for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
        print(col, '::', col[4:])
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True)

#print(df.head())


# boolean conditions with DFs, operator is applide to whole DF
print(df['Gold'] > 0)

# where function takes a boolean function and returns a new DF with the conditions meet
print('\n****** where and boolean functions examples\n')
df_only_gold = df.where(df['Gold'] > 0)
print(df_only_gold.head(), '\n\n')
print('Countries with only a gold: ', df_only_gold['Gold'].count(), ' Countries with a gold: ', df['Gold'].count())

# where can be overloaded with operator in selector
df_only_gold = df.where(df['Gold'] > 0)
print(df_only_gold.head(), '\n\n')
print('Countries with only a gold: ', df_only_gold['Gold'].count(), ' Countries with a gold: ', df['Gold'].count())

t_len = len(df[(df['Gold']>0) | (df['Gold.1']>0)])
print('Lenght of Gold & Gold.1: ', t_len)
print('Has won a Winter Gold but not Summer: ', df[(df['Gold.1']>0) & (df['Gold']==0)])

# how to change index's and move them around
# when you make a new index, the old one is distroyed, data lost if not manually saved
# start with df, and make a new column, and put into it the current index
print('\n****** messing with indexes\n')
df2 = df
df2['Countries'] = df2.index # create a new column, but the current index into it (Country names)
df2 = df2.set_index('Gold') # sets the Gold column to the index
print(df2.head())
df2 = df2.reset_index() #puts a numbered index in place, current index becomes a column
print(df2.head())


# multi-level indexes and complex data sets
print('\n***** multi-level indexes and complex data sets\n')
df = pd.read_csv('census.csv')
df = pd.DataFrame(df) # let Spyder know this is a Dataframe
print(df.head())
print('\n Unique sumlevel entries: ',df['SUMLEV'].unique())

# SUMLEV 40 == county level, 50 == State
df = df[df['SUMLEV']==50] # update Dataframe to just have state level data
print(df.head())
# filter unwanted data (columns) by keeping the ones we want
columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
df = df[columns_to_keep]
print(df.head())
df = df.set_index(['STNAME','CTYNAME'])
print(df.head())
print(df.loc[ [('Michigan', 'Washtenaw County'),('Michigan','Wayne County')] ])


# adding a row to a data frame and giving it indexes
print('\n***** adding rows, indexes\n')
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

print('\nStart Data Frame:\n',df)
df = df.set_index([df.index, 'Name'])
df.index.names = ['Location', 'Name']
# need to add to a Dataframe with a series, like this:
df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn')))
print('\nEnd Data Frame:\n',df)


# missing values examples
print('\n***** working with missing data\n')
df = pd.read_csv('log.csv')
df = pd.DataFrame(df) # let Spyder know this is a Dataframe
print(df.head())
# filling in missing data, fisrt sort the data, so fill functions work
df = df.set_index(['time','user']) #set the index to time, and then sort the data on the index
df = df.sort_index()
print(df.head())
df.fillna




