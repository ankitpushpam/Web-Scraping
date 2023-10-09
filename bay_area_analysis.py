import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from web_Scraping import listing_data


'''
Question 1: What type of the house is most built in the Hayward town?

Conclusion: Single Family Residence is the most famous house type built over in the Hayward. 
And the interesting fact is there there a very few building with for the built type is Business Opportunity.

'''
df = listing_data.drop('Unnamed: 0', axis = 1)
Series=df['House_Type'].value_counts()
Series.plot(kind="bar",color='b')

'''
Question 2: To further explore more what style is more famous in the house type 'Single Family Residence'? 
Conclusion: In the House Type 'Single Family Residence ' the most famous style is 'customer', 'Prairie', and 'ranch'.
'''

ct=pd.crosstab(df['House_Type'],df['Style'])
ct.plot.bar(stacked=True)
plt.legend(title = 'Style' ,loc = 'sks')

df['Sold_Price'] = df['Sold_Price'].replace('– ', 0)
df['Sold_Price'] = df['Sold_Price'].str.replace('$', '')
df['Sold_Price'] = df['Sold_Price'].str.replace(',', '')
df['Sqft'] = df['Sqft'].replace('–', 0)
df['Sqft'] = df['Sqft'].str.replace(',', '')


df['Sold_Price'] = df['Sold_Price'].astype(float)
df['Sqft'] = df['Sqft'].astype(float)
sns.barplot(x='Sold_Price',y='Style',data=df,orient='h')

'''
Question 3: To furthermore explore in the style of the house, what is the sold price distribution of the style? 
Conclusion: Customer style is the most famous style in the hayward and the sold price is also maximum for this house.
'''

df['Sold_Price'] = df['Sold_Price'].astype(float)

'''
Question 4: To explore the relationship between the change in the sold_price vs sqft in Hayward city? 
Conclusion: The Sqft is positively correlated with the change on the sold price. 
When the sqft of a house will increase than the house sold price will also increase.
'''

sns.regplot('Sold_Price','Sqft',data=df)
plt.title('Changes in %s versus %s' %('Sold_Price','Sqft'))