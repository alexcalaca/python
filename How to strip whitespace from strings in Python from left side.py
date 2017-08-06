# -*- coding: utf-8 -*-
"""
@author: Alexandre Calaça
You can reach me at alexcalaca@gmail.com
"""

"""
How to strip whitespace from strings in Python from left side
"""


import pandas as pd

#Create a python dictionary with pandas series values
dictionary = {
        'name': pd.Series([' Mark', ' Allen', 'Josh ', ' Chandler '], index=['a', 'b', 'c', 'd']),
        'city': pd.Series(['NYC', 'RJ', 'LA', 'New Jersey'], index=['a', 'b', 'c', 'd']),
        'age': pd.Series([29, 39, 51, 18], index=['a', 'b', 'c', 'd']),
        'ticket': pd.Series([30.25, 60.50, 60.50, 30.25], index=['a', 'b', 'c', 'd']),
        'bought?': pd.Series([True, False, True, False], index=['a', 'b', 'c', 'd'])
        }



#Data frame
df = pd.DataFrame(dictionary)

#Print the whole data values
print(df)

print("\nStripping whitespace from all names from left side")

#Use the lstrip() method to strip whitespace from all names from left side
print(df.name.str.lstrip())