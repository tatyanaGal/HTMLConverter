import csv
from bs4 import BeautifulSoup

target_file = open("output.csv")


#links = soup.find_all('a')
#links = [link for link in links
 #        if link["href"].startswith("http://www.conakat.com/map/?p=")]
#zips = soup.find_all('i')

#for l, z in zip(links, zips):
 #   f.writerow((l.contents[0], z.contents[0]))

for line in csv.reader("website_downloads_2017-11-02.csv"):
  url = "http://www.independent.co.uk/news/world/americas/us-politics/jeff-sessions-russia-trump-investigation-george-papadopoulos-trouble-a8034546.html"
  site = "independent.co.uk" # spiegel.de

  html = line[0]
  doc = BeautifulSoup(html, "lxml")
  
  text = extract_text(doc, site)

  csv.write(target_file, [site, url, text])

close(target_file)


def extract_text(doc, site):
  if site == "spiegel.de":
    return extract_text_spiegel(doc)
  elif site == "welt.de":
    return extract_text_welt(doc)
  elif site == "independent.co.uk":
    return extract_text_independent(doc)
  else:
    return "unkown site"

def extract_text_spiegel(doc):
  return doc.find("div", {class_: "article-section"}).text


def extract_text_spiegel(doc):
  return doc.find("div", {class_: "welt-content"}).text


def extract_text_independent(doc):
  return doc.find("div", {class_: "article-section"}).text