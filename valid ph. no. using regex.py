# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 15:35:32 2020

@author: 91852
"""

import re
print('enter no.')
n=input()
if re.match("^1-9[0-9]{9}$",n):
    print('valid')
else:
    print('invalid')
    