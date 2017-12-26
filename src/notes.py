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








