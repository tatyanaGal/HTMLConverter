import csv

#Print the file in the console
with open('./website_downloads_2017-11-02.csv', newline='', encoding='utf-8') as csvfile:
	reader=csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
	for row in reader:
		print([r.encode('utf-8').decode('unicode_escape') for r in row])