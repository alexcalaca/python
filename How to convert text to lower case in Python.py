# -*- coding: utf-8 -*-
"""
@author: Alexandre Calaça
You can reach me at alexcalaca@gmail.com
"""

"""
How to convert text to lower case in Python
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

print("\nConverting all names to lower case")

#Use the lower() method to convert strings to lower case
print(df.name.str.lower())