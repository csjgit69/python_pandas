import pandas as pd

# week 3 notes

def add_columns():
    df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
                       {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
                       {'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
                      index=['Store 1', 'Store 1', 'Store 2'])
    
    print('\n****** adding a new column \n')
    print('>>> Before adding Dates column:\n',df)
    df['Date'] = ['December 1', 'January 1', 'mid-May'] # add a column with data, must be same number of data as rows
    print('>>> After adding Dates column:\n',df)
    df['Delievered'] = True # add scalar (single value) and it gets auto-populated to all rows
    print('>>> After adding Delievered flag column:\n',df)
    #add a column and data with missing data
    df['Feedback'] = ['Positive',None,'Negative'] #filled in missing value manualy
    print('>>> After adding Feedback column:\n',df)
    # or can just add values you want if you have a nice index
    adf = df.reset_index()
    adf['Date'] = pd.Series({0: 'December', 2: 'mid-May'}) # Pandas will autfill missing data
    print('>>> After adding some Dates with index selection and using a series:\n',adf)

def merges():
    staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                             {'Name': 'Sally', 'Role': 'Course liasion'},
                             {'Name': 'James', 'Role': 'Grader'}])
    staff_df = staff_df.set_index('Name')
    student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                               {'Name': 'Mike', 'School': 'Law'},
                               {'Name': 'Sally', 'School': 'Engineering'}])
    student_df = student_df.set_index('Name')
    print('\n',staff_df,'\n',student_df,'\n')
    
    # do a merge of the 2 Dataframes above
    merge_df = pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)
    print('\nOuter (Union) Merged Dataframe:\n',merge_df)
    merge_df = pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)
    print('\nInner (Intersection) Merged Dataframe:\n',merge_df)
    #get list of all staff, and if they are student get the student info
    #this is a left join because staff_df is the first (left) DF listed
    merge_df = pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)
    print('\nLeft (staff + info from students if a staff person is a student also) Merged Dataframe:\n',merge_df)
    #get list of all students, and if they are staff get the staff info
    #this is a Right join because student_df is the second (Right) DF listed
    merge_df = pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)
    print('\nRight (student + info from staff if a student person is a staff also) Merged Dataframe:\n',merge_df)
    #using indexes to join Dataframes
    student_df2 = student_df.reset_index()
    staff_df2 = staff_df.reset_index()
    merge_df = pd.merge(staff_df2, student_df2, how='left', left_on='Name', right_on='Name')
    print('\nLeft but based on the common column Name from both DFs Merged Dataframe:\n',merge_df)
    
    staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                             {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                             {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
    student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                               {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                               {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])
    #example of when there are conflicts in DFs and can't happen cleanly
    #conflicting data is put in a column with old column name and an underscore x or y (location_x)
    #_x is always the Dataframe on the left (first one), _y is the one on the right (second one)
    print('\n',staff_df,'\n',student_df,'\n')
    merge_df = pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')
    print('\nLeft with conflicting columns in Merged Dataframe:\n',merge_df)
    
    
    



#add_columns()
merges()