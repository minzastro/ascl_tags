# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 17:08:11 2015

@author: mints
"""

from collections import Counter

import sqlite3

conn = sqlite3.connect('ascl.sqlite')

full = []
for row in conn.execute('select title from ascl_entries'):
    full.append(row[0])

full = ' '.join(full)
full = full.split(' ')
co = Counter(full)
print co