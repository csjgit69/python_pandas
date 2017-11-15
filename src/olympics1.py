import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
    if col[:1] == '№':
        df.rename(columns={col: '#' + col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(')  # split the index by '('
# names_ids = df.index.str.split('(') # split the index by '('

df.index = names_ids.str[0]  # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3]  # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
#print(df.head())


# Question 0(Example)
# What is the first country in df?
# This function should return a Series.

# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting
    return df.iloc[0]


# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs

# print(answer_zero())

# -----------------------------------------------------
# Question 1
# Which country has won the most gold medals in summer games?
# This function should return a single string value.
def answer_one():
    tmp = df.nlargest(1, 'Gold').index[0]
    # print(tmp)
    return tmp


#print(answer_one())
#print(type(answer_one()))

# tmp = sorted( [df['Gold']-df['Gold.1']], key=lambda x: x[1])
# pd.Series(data={'Cost':3.00, 'Item Purchased':'Kitty Food'}, name=('Store 3','Kevyn')))
# tmp = pd.Series(data={df['Gold'] - df['Gold.1']}, name=('Country', 'Gold'))


# -----------------------------------------------------
# Question 2
# Which country had the biggest difference between their summer and winter gold medal counts?
# This function should return a single string value.
def answer_two():
    #tmp = (df['Gold'] - df['Gold.1']).to_frame('Gold').nlargest(1,'Gold').index[0]
    #tmp = tmp.to_frame('Gold')
    return (df['Gold'] - df['Gold.1']).to_frame('Gold').nlargest(1,'Gold').index[0] #tmp #.nlargest(1,'Gold').index[0]

#print(answer_two())
#print(type(answer_two()))

# -----------------------------------------------------
# Question 3
# Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?
# (Summer Gold−Winter Gold)/ Total Gold
# Only include countries that have won at least 1 gold in both summer and winter.
# This function should return a single string value.
def answer_three():
    tmp = df.where((df['Gold']>0)& (df['Gold.1']>0)).dropna()
    tmp = ((tmp['Gold']- tmp['Gold.1'])/tmp['Gold.2']).to_frame('Gold').nlargest(1,'Gold').index[0]
    return tmp

#print(answer_three())
#print(type(answer_three()))

# -----------------------------------------------------
# Question 4
#Write a function that creates a Series called "Points" which is a weighted value where each gold medal (Gold.2) counts for 3 points, silver medals (Silver.2)
# for 2 points, and bronze medals (Bronze.2) for 1 point. The function should return only the column (a Series object) which you created.
#This function should return a Series named Points of length 146
def answer_four():
    tmp = (3*df['Gold.2'])+(2*df['Silver'])+(df['Bronze'])
    #print("---- DF -----")
    #print(df['Gold.2'].head())
    #print("---- TMP -----")
    #print(tmp.head())
    return (3*df['Gold.2'])+(2*df['Silver'])+(df['Bronze'])

#print(answer_four())
#print(type(answer_four()))

census_df = pd.read_csv('census.csv')

#print(census_df.head())
#print(census_df.loc['Alabama'])
#df = census_df[census_df['SUMLEV']==40]
#print(df.head())


# -----------------------------------------------------
# Question 5
# Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)
# This function should return a single string value.
def answer_five():
    df_filter = census_df[census_df['SUMLEV']==50].set_index(['STNAME']) #fliter out state data
    #print(df_filter)

    state_df = pd.DataFrame()
    state_df['State'] = df_filter.index.unique()
    #print(state_df)
    state_df['CountyCnt'] = 0

    state_df.set_index('State',inplace=True)
    for st in state_df.index:
        stcount = df_filter.loc[st].shape[0]
        #print(state_df.loc[st].shape[0]) #, state_df.loc[st].count())
        state_df['CountyCnt'].loc[st] = stcount

    return state_df.nlargest(4,'CountyCnt')

#print("fml", answer_five())
#print(type(answer_five()))


# -----------------------------------------------------
# Question 6
# Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)?
# Use CENSUS2010POP.
# This function should return a list of string values.

def answer_seven():
    # county level data, not state level
    df_filter = census_df[census_df['SUMLEV'] == 50].set_index(['STNAME'])  # filter out state data
    # print(df_filter)

    #state data frame
    state_df = pd.DataFrame()
    #put in unique state names from above
    state_df['State'] = df_filter.index.unique()
    # print(state_df) # debuge
    #will hold sum of top 3 counties per state
    state_df['Top3Pop'] = 0
    state_df.set_index('State', inplace=True)

    for st in state_df.index:
        countiespop = 1
        stcount = df_filter.loc[st].shape[0]
        # print(state_df.loc[st].shape[0]) #, state_df.loc[st].count())
        state_df['Top3Pop'].loc[st] = stcount
    return "YOUR ANSWER HERE"

print("fml", answer_seven())
#print(type(answer_seve())
