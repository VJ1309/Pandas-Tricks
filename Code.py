# Pandas Query Function

#to filter df based on criteria
df.query('sex=="Male" & size>2').head(10) 

#to filter df based on variable & criteria
days = ["Sat", "Sun"] 
df.query('sex=="Male" & size>2 & day==@days').head(10)

# to sort df based on largest values 
df.nlargest(5, 'total_bill') 
df.nsmallest(5, 'total_bill') 

-----------------------------------------------------------------

# Pandas Group-by Function

#Groupby: Different Aggregation Methods
df.groupby(by=['sex', 'smoker']).agg(['sum', 'mean'])

#Groupby: Different Aggregation Methods for individual columns
agg_criteria = {'total_bill': 'sum', 
                'tip': 'mean'}

df.groupby(by=['sex', 'smoker']).agg(agg_criteria)


------------------------------------------------------------------
#Below function categorizes tip column to different lables based on the bin size
bins = [0, 2, 4, float('inf')]
labels = ['small','medium','high']
df['tip_category'] = pd.cut(df['tip'], bins=bins, labels=labels)
df.head(15)
