import pandas as pd
import numpy as np


# week 3 notes

## ****************************************************************************
## min_max that returns a new serries with old indexes
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})


## ****************************************************************************
## min_max new full Dataframe
def min_max2(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    row['max'] = np.max(data)
    row['min'] = np.min(data)
    return row


## ****************************************************************************
##
def add_columns():
    df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
                       {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
                       {'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
                      index=['Store 1', 'Store 1', 'Store 2'])

    print('\n****** adding a new column \n')
    print('>>> Before adding Dates column:\n', df)
    df['Date'] = ['December 1', 'January 1', 'mid-May']  # add a column with data, must be same number of data as rows
    print('>>> After adding Dates column:\n', df)
    df['Delievered'] = True  # add scalar (single value) and it gets auto-populated to all rows
    print('>>> After adding Delievered flag column:\n', df)
    # add a column and data with missing data
    df['Feedback'] = ['Positive', None, 'Negative']  # filled in missing value manualy
    print('>>> After adding Feedback column:\n', df)
    # or can just add values you want if you have a nice index
    adf = df.reset_index()
    adf['Date'] = pd.Series({0: 'December', 2: 'mid-May'})  # Pandas will autfill missing data
    print('>>> After adding some Dates with index selection and using a series:\n', adf)


## ****************************************************************************
##
def merges():
    staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                             {'Name': 'Sally', 'Role': 'Course liasion'},
                             {'Name': 'James', 'Role': 'Grader'}])
    staff_df = staff_df.set_index('Name')
    student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                               {'Name': 'Mike', 'School': 'Law'},
                               {'Name': 'Sally', 'School': 'Engineering'}])
    student_df = student_df.set_index('Name')
    print('\n', staff_df, '\n', student_df, '\n')

    # do a merge of the 2 Dataframes above
    merge_df = pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)
    merge_df = pd.DataFrame(merge_df)
    print('\nOuter (Union) Merged Dataframe:\n', merge_df)
    merge_df = pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)
    merge_df = pd.DataFrame(merge_df)
    print('\nInner (Intersection) Merged Dataframe:\n', merge_df)
    # get list of all staff, and if they are student get the student info
    # this is a left join because staff_df is the first (left) DF listed
    merge_df = pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)
    print('\nLeft (staff + info from students if a staff person is a student also) Merged Dataframe:\n', merge_df)
    # get list of all students, and if they are staff get the staff info
    # this is a Right join because student_df is the second (Right) DF listed
    merge_df = pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)
    print('\nRight (student + info from staff if a student person is a staff also) Merged Dataframe:\n', merge_df)
    # using indexes to join Dataframes
    student_df2 = student_df.reset_index()
    staff_df2 = staff_df.reset_index()
    merge_df = pd.merge(staff_df2, student_df2, how='left', left_on='Name', right_on='Name')
    print('\nLeft but based on the common column Name from both DFs Merged Dataframe:\n', merge_df)
    staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                             {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                             {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
    student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                               {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                               {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])
    # example of when there are conflicts in DFs and can't happen cleanly
    # conflicting data is put in a column with old column name and an underscore x or y (location_x)
    # _x is always the Dataframe on the left (first one), _y is the one on the right (second one)
    print('\n', staff_df, '\n', student_df, '\n')
    merge_df = pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')
    print('\nLeft with conflicting columns in Merged Dataframe:\n', merge_df)

    print('\n>>> Merging based on multiple keys per Dataframe:\n')
    staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                             {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                             {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
    student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                               {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                               {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])
    print('\n', staff_df, '\n', student_df, '\n')
    # use first and last names to get union of Dataframes with data in it that has both people in both Dataframes
    merge_df = pd.merge(staff_df, student_df, how='inner', left_on=['First Name', 'Last Name'], right_on=['First Name', 'Last Name'])
    print('\nMerging on multiple keys (columns), first and last name:\n', merge_df, '\n')


## ****************************************************************************
##
def lambda_play():
    sum = lambda x, y: x + y
    min = lambda x: np.amin(x, axis=0)
    a = (9, 3, 1, 10)
    b = [-1, 2, 4, 10]
    c = {4, 5, 1, 89}
    print('FUCK IT ALL!!!---')
    print('a is type: ', type(a), ' values: ', a)
    print('b is type: ', type(b), ' values: ', b)
    print('c is type: ', type(c), ' values: ', c)
    print('sum: ', sum(5, 6))
    print('min: ', min([[10, 2, 3, -1], [9, 9, -2, np.NaN], [10, 10, 10, -10]]))
    print('min: ', min(a))
    print('min: ', min(b))
    print('min: ', min(c))
    return 0


## ****************************************************************************
##
def map_play():
    c = [39.2, 36.5, 37.3, 38, 37.8]
    print('original temp list in celcius: ', c)
    f = list(map(lambda x: (float(9) / 5) * x + 32, c))
    print('Temp list mapped to fahrenheit:', f)
    c = list(map(lambda x: (float(5) / 9) * (x - 32), f))
    print('fahrenheit temps mapped back to celcius: ', c)
    return 0

def st_hash(item):
    if (item[0] < 'M'):
        return 0
    if (item[0] < 'Q'):
        return 1
    return 2


def groupby_play():
    df = pd.DataFrame(pd.read_csv('census.csv'))
    df = df[df['SUMLEV'] == 50]

    #    print('>>> finding average across the census data with a for loop:')
    #    for state in df['STNAME'].unique():
    #        avg = np.average(df.where(df['STNAME'] == state).dropna()['CENSUS2010POP'])
    #        print(state,' has an average counties population of ',avg,' in 2010.' )

    #    print('\n**********\n**********\n')
    #    print('>>> finding average across the census data with groupby:')
    #    for group, frame in df.groupby('STNAME'):
    #        avg = np.average(frame['CENSUS2010POP'])
    #        print(group,' has an average counties population of ',avg,' in 2010.' )

    df2 = df.set_index('STNAME')

    print('\n**********\n')
    for group, frame in df2.groupby(st_hash):
        print('There are ', len(frame), ' records in group ', group, 'for processing.')

    print('\n**********\n')
    df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                       'key2': ['one', 'two', 'one', 'two', 'one'],
                       'data1': np.random.randint(19, size=5),
                       'data2': np.random.randint(19, size=5)})
    print('df to play with:')
    print(df)
    print('')
    grouped = df['data1'].groupby(df['key1'])
    print('grouped:')
    print(grouped)
    print('grouped.mean() is: ', grouped.mean())
    print('--')
    # create 2 keys, master/sub (is that the way to think of it?) and group the data. operations can be performed on the group_object
    print('another means: ', df['data1'].groupby([df['key1'], df['key2']]).sum())

    states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
    years = np.array([2005, 2005, 2006, 2005, 2006])

    df2 = df['data1'].groupby([states, years])
    print('How the fuck does this work? :')
    print(df2.sum())
    print('---')
    print('-- Single Key --')
    # groupby object supports iteration, generationg a sequence of 2-tuples, group-name & group-data
    for name, group in df.groupby('key1'):
        print('group name: ', name)
        print('group data:\n', group)
    print('---')
    print('-- Double Key --')
    # with multikeys:
    for (k1, k2), group in df.groupby(['key1', 'key2']):
        print('group name: ', (k1, k2))
        print('group data:\n', group)

    # can be useful to make a hash/dic from the grouping on the key:
    pieces = dict(list(df.groupby(['key1'])))
    print('----')
    print('-- groupby to make hash table/dictionary')
    print('key1 == a:\n',pieces['a'])
    print('key1 == b:\n',pieces['b'])

    print('---')
    print('-- grouping on rows, by entry type')
    print('df by entry type:')
    print(df.dtypes)
    print('-- groupby dtypes on axis = 1')
    for dtype, group in df.groupby(df.dtypes, axis=1):
        print('dtype:\n',dtype)
        print('group:\n',group)
    print('-- groupby dtypes on axis = 0')
    for dtype, group in df.groupby(df.dtypes, axis=0):
        print('dtype:\n',dtype)
        print('group:\n',group)

    return 0

## ****************************************************************************
##
def pd_apply_play():
    # HOW to autocomplete after a CSV load!!!!
    df = pd.read_csv('census.csv')
    # df = pd.DataFrame(df)
    print('FUCK IT ALL!!!---')
    print('>>>> 1/10/2018 all autocompletes without tricks seems to work')

    df = pd.DataFrame(df[df['SUMLEV'] == 50])
    df.set_index(['STNAME', 'CTYNAME'], inplace=True)
    df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})
    # print('\n>> Census data Dataframe read in:\n',df.head(),'\n')

    # create new column with values from multiple rows
    # here axis is the index to use in the function given, axis=1 means all rows (why?)
    df2 = df.apply(min_max, axis=1)
    df2 = pd.DataFrame(df2)
    # print('\nDataframe after apply min_max method:\n',df2.head(),'\n')
    df3 = df.apply(min_max2, axis=1)
    df3 = pd.DataFrame(df3)
    # print('\nDataframe after apply min_max2 method:\n',df3.head(),'\n')

    rows = ['POPESTIMATE2010',
            'POPESTIMATE2011',
            'POPESTIMATE2012',
            'POPESTIMATE2013',
            'POPESTIMATE2014',
            'POPESTIMATE2015']
    df4 = df  # make a copy so I can add columns easily as I do below

    df4 = pd.DataFrame(df).head(100)
    df4['max'] = df.apply(lambda x: np.max(x[rows]), axis=1)
    df4['min'] = df.apply(lambda x: np.min(x[rows]), axis=1)

    print('\nDataframe after apply with lambda method:\n',df4.head(),'\n')

    # Agg example
    print('---')
    print('-- example of \'agg\', it takes a column name and function to apply to it')
    df = pd.DataFrame(df[df['SUMLEV'] == 50])
    group2 = df.groupby('STNAME').agg({'CENSUS2010POP': np.average})
    print(group2.head())
    print('')
    print('agg without groupby, see the counties still in the data, not sure what it did tbh')
    group2 = df.agg({'CENSUS2010POP': np.average})
    print(group2.head())

    return 0



print('*****************************')
print('********** New Run **********\n')

#add_columns()
#merges()
#lambda_play()
#map_play()
#groupby_play()
pd_apply_play()
print('')
print('********** End Run **********')
print('*****************************\n')
