import pandas as pd
import numpy as np

#df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

df = pd.read_excel('Energy+Indicators.xls', skiprows=17, skipfooter=38, parse_cols = "C:F")
#df = pd.read_excel('Energy+Indicators.xls', index=2, skipcolumns=2, skiprows=17, skipfooter=38, .parse_cols = "C:F")

#print(df.columns.values)         
#                  .drop([0,1], axis=1)
df.reindex(['Energy Supply','Energy Supply per Capita','% Renewable']) #F I X
af = pd.DataFrame

af = df.rename(columns={0:'Country', 1:'Energy Supply', 2:'Energy Supply per Capita', 3:'% Renewable'})
#af = df.rename(columns={2:'Country', 3:'Energy Supply', 4:'Energy Supply per Capita', 5:'% Renewable'})


                  
                  
#for col in df.columns:
#    if col[:2] == '01':
#        df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
#    if col[:2] == '02':
#        df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
#    if col[:2] == '03':
#        df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
#    if col[:1] == '№':
#        df.rename(columns={col: '#' + col[1:]}, inplace=True)

#names_ids = df.index.str.split('\s\(')  # split the index by '('
# names_ids = df.index.str.split('(') # split the index by '('


##df.index = names_ids.str[0]  # the [0] element is the country name (new index)
##df['ID'] = names_ids.str[1].str[:3]  # the [1] element is the abbreviation or ID (take first 3 characters from that)
##
##df = df.drop('Totals')
##print(df.head())
#
#census_df = pd.read_csv('census.csv')
#
#
##print(census_df.head())
##print(census_df.loc['Alabama'])
##df = census_df[census_df['SUMLEV']==40]
#df = census_df[census_df['SUMLEV']==50]
#print(df.head())

#%%timeit -n 10
print('\n------ WTF???? ------')
avg = 0
#for state in df['STNAME'].unique():
#    avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])
#    print('Counties in state ' + state + ' have an average population of ' + str(avg))

#for group, frame in df.groupby('STNAME'):
#    print('--------\n',group)
#    
#    avg = np.average(frame['CENSUS2010POP'])
#    print('Counties in state ' + group + ' have an average population of ' + str(avg))

#df = df.set_index('STNAME')
#
#def fun(item):
#    if item[0]<'M':
#        return 0
#    if item[0]<'Q':
#        return 1
#    return 2
#
#for group, frame in df.groupby(fun):
##    print(group)
##    print(frame.head())
#    print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')

#df = pd.read_csv('census.csv')
#df = df[df['SUMLEV']==50]
#print(df.groupby('STNAME').agg({'CENSUS2010POP': np.average}))
#af = df.groupby('STNAME').agg({'CENSUS2010POP': np.average})
#print(pd.cut(af['CENSUS2010POP'],4))

#print(df.groupby('STNAME'))

# example of groupby and apply with a lambda function to sum to columns
#print(df.groupby('STNAME').apply(lambda df,a,b: sum(df[a] * df[b]), 'POPESTIMATE2010', 'POPESTIMATE2011'))

#shows two 
#print(type(df.groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']))
#print(type(df.groupby(level=0)['POPESTIMATE2010']))
#af = pd.DataFrame
# groupby and agg on a series. agg does both operations on 1 column, makes output columns
#print(df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average, 'sum': np.sum}))

# groupby and agg on two columns 
#af = df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011'].agg({'avg': np.average, 'sum': np.sum})
#print(af)

# shows confusion rename 
#af = df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011'].agg({'POPESTIMATE2010': np.average, 'POPESTIMATE2011': np.sum})
#print(af)


#df = pd.DataFrame(['A+','A','A-','B+','B','B-','C+','C','C-','D+','D'],
#                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
#df.rename(columns={0:'Grades'},inplace=True)
#print(df.head())
#print('----')
#print(df['Grades'].astype('category').head())

# notice ordering, smallest to greatest
#grades = df['Grades'].astype('category',
#                             categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
#                             ordered=True)
#grades.rename(columns={0:'Grades',1:'Grade'},inplace=True)
#print(grades.head())
#print(grades > 'A')


#df = pd.read_csv('cars.csv')
#af = df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean)
#print(af)

# example of timestamp,list is used to make 3 entries, nice shortbook
#t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
#print(t1)

