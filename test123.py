import csv
from bs4 import BeautifulSoup
import codecs
import os
import sys

maxInt = sys.maxsize
decrement = True

while decrement:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True
#csv.field_size_limit(sys.maxsize)

with open('./website_downloads_2017-11-02.csv', newline='', encoding='utf-8') as inf, open('./output.csv', 'w', newline='', encoding='utf-8') as outf:
  reader = csv.reader(inf)
  writer = csv.writer(outf, delimiter=',', quoting=csv.QUOTE_ALL)
  
  for line in reader:
  	if not line:
  		continue
  		
  	print(line[0])
inf.close()
outf.close()
