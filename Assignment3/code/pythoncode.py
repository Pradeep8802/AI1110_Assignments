'''
Name: I Sai Pradeep
Roll number: AI21BTECH11013
'''
'''
CBSE Probability Grade 12
Exercise 13.3
Question 8
'''
"""
Question Statement:
A factory has two machines A and B. Past record shows that machine A produced 60% of th items of output and machine B produced 40% of the items. Further,2% of the items produced by machine A and 1% produced by machine B were defective. All the items are put into one stockpile and then one item is chosen at random from this and is found to be defective. What is the probability that it was produced by machine B?
"""

import numpy as np
import pandas as pd
#using the input datas present in the excelsheet  
df = pd.read_excel("table2.xlsx")
data = np.array(df)
probs = dict(zip(data[:,0], data[:,1]))

# Computing the required probability
pr = (probs['Pr(Y=0|X=1)']*probs['Pr(X=1)']) / (probs['Pr(Y=0|X=0)'] * probs['Pr(X=0)'] + probs['Pr(Y=0|X=1)'] * probs['Pr(X=1)'])
print(format(pr, '.3f'))
