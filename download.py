# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:25:45 2015

@author: mints
"""

from lxml import html
import requests
import sqlite3

conn = sqlite3.connect('ascl.sqlite')
def get(div, part):
    text = div[part].text_content().strip()
    text = text.replace("'", "''")
    return text

def save_page(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)

    items = tree.xpath('//div[@class="item"]')

    sql = 'insert into ascl_entries values '
    values = []

    for item in items:
        divs = item.getchildren()
        div1 = get(divs, 1).split(':')
        name = div1[0]
        title = ':'.join(div1[1:])
        item_code = [get(divs, 0)[1:-1],
                     name,
                     title,
                     get(divs, 2),
                     get(divs, 3)]
        values.append('(%s)' % ','.join(["'%s'" % xitem for xitem in item_code]))
    sql = '%s %s' % (sql, ",\n".join(values))
    print sql
    conn.execute(sql)
    conn.commit()

for i in xrange(1,13):
    url = 'http://ascl.net/code/all/page/%s/limit/100/order/title/listmode/full/dir/asc' % i
    print i
    save_page(url)
conn.close()