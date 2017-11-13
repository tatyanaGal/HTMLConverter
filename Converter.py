import csv
from bs4 import BeautifulSoup

target_file=open("output.csv")

def extract_text(doc, site):
  if site == "spiegel.de":
    return extract_text_spiegel(doc)
  elif site == "welt.de":
    return extract_text_welt(doc)
  elif site == "independent.co.uk":
    #return extract_text_independent(doc)
    table = doc.findAll("p")
    for row in table:
      print(row.text)

  #else:
   # return "unkown site"

def extract_text_spiegel(doc):
  return doc.find("div", {class_: "article-section"}).text


def extract_text_spiegel(doc):
  return doc.find("div", {class_: "welt-content"}).text


def extract_text_independent(doc):
  return doc.find("<p>").text


#AB HIER!!!
with open("test.csv") as filer:
  rd = csv.reader(filer)

  for row in rd:
    if not row:
      continue

    url=row[1]
    if url.startswith("http://www.independent.co.uk"):
      site = "http://www.independent.co.uk"
      html=row[2]
      doc=BeautifulSoup(html, "lxml")

      #text = extract_text(doc, site)

      #csv.writer(target_file, [site, url, text])

      #print(site)
      #print(html)
      #print(url)

      table = doc.findAll("p")
      

      with open("output.csv","w") as target:
        file = csv.writer(target)
        for row in table:
          file.writerow([site, url, row.text])

target.close()
#close("output.csv")


#funktionierende Ausgabe von URLS:
#with open("website_downloads_2017-11-12.csv") as filer:
#  rd = csv.reader(filer)

#  for row in rd:
 #   if not row:
  #    continue

   # print(row[1])
    

#url = "http://www.independent.co.uk/news/world/americas/us-politics/jeff-sessions-russia-trump-investigation-george-papadopoulos-trouble-a8034546.html"
  #site = "independent.co.uk" # spiegel.de

  #html = line[0]
  #doc = BeautifulSoup(html, "lxml")
  
  #text = extract_text(doc, site)

  #csv.write(target_file, [site, url, text])

#close(target_file)


