# -*- coding: utf-8 -*-
"""
@author: Alexandre Calaça
"""

"""
How to replace a substring in a string in Python
"""


import pandas as pd

#Create a python dictionary with pandas series values
dictionary = {
        'name': pd.Series([' Mark', ' Allen', 'Josh ', ' Chandler ', 'Emily '],
                          index=['a', 'b', 'c', 'd', 'e']),
        'city': pd.Series(['NYC', 'RJ', 'LA', 'New Jersey', 'Salvador'],
                          index=['a', 'b', 'c', 'd', 'e']),
        'age': pd.Series([29, 39, 51, 18, 65], index=['a', 'b', 'c', 'd', 'e']),
        'ticket': pd.Series([30.25, 60.50, 60.50, 30.25, 60.50],
                            index=['a', 'b', 'c', 'd', 'e']),
        'bought?': pd.Series([True, False, True, False, False],
                             index=['a', 'b', 'c', 'd', 'e'])
        }



#Data frame
df = pd.DataFrame(dictionary)

#Print the whole data values
print(df)

print("\nReplacing all whitespaces with underscores")

#Use the str.replace() method to replace a substring in a string in Python
print(df.name.str.replace(' ', '_'))
