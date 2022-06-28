# -*- coding: utf-8 -*-
"""
@author: Alexandre Calaça
"""

"""
How to sort data by an axis in Python
"""

import pandas as pd

#Create a python dictionary with pandas series values
dictionary = {
        'name': pd.Series(['Mark', 'Allen', 'Josh'], index=['a', 'b', 'c']),
        'city': pd.Series(['NYC', 'RJ', 'LA'], index=['a', 'b', 'c']),
        'age': pd.Series([29, 39, 51], index=['a', 'b', 'c']),
        'ticket': pd.Series([30.25, 60.50, 60.50], index=['a', 'b', 'c']),
        'bought?': pd.Series([True, False, True], index=['a', 'b', 'c'])
        }



#Data frame
df = pd.DataFrame(dictionary)


#Print the whole data values
print(df)

print("\nSort the elements by an axis")

#Use the sort_index method to sort the elements by an axis
print(df.sort_index(axis = 0, ascending=False))
