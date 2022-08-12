#!/usr/bin/env python3

# This script displays what is currently on WRKF at the cmd
# UNFINISHED
# Also, I'm attempting to completely bodge this with stackoverflow snippets

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.wrkf.org/wrkf-schedule'
htmldoc = urlopen(url)

def get_tables(htmldoc):
    # soup = BeautifulSoup.BeautifulSoup(htmldoc)
    soup = BeautifulSoup(htmldoc)
    return soup.findAll('table')

table = get_tables(htmldoc)

def makelist(table):
  result = []
  allrows = table.findAll('tr')
  for row in allrows:
    result.append([])
    allcols = row.findAll('td')
    for col in allcols:
      thestrings = [unicode(s) for s in col.findAll(text=True)]
      thetext = ''.join(thestrings)
      result[-1].append(thetext)
  return result

table_list = makelist(table) 

print(table_list)
