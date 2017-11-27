import csv
from bs4 import BeautifulSoup
import codecs
import os, sys, string

# ALLGEMEIN 
# Die gecrawlten csv Datei sind folgendermassen aufgebaut:
# 1. Zeile: "irgendeine Zahl 1","url 1","html-Seite 1"
# 2. Zeile: blank
# 3. Zeile: "irgendeine Zahl 2","url 2","html-Seite 2"
# 4. Zeile: blank
# usw.
#

## Notwendig, um die langen HTML-Texte ablesen zu koennen. KP wat dat ist...
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


## Neue Loesung:
with open('./website_downloads_2017-11-02.csv', newline='', encoding='utf-8') as inf, open('./output.csv', 'w') as outf:
  reader = csv.reader(inf)
  writer = csv.writer(outf, delimiter=',', quoting=csv.QUOTE_ALL)
  
  for line in reader: # csv wird zeilenweise abgelesen - line = Zeile 1 usw. 
    # Leere Zeilen in csv werden uebersprungen
    if not line: 
      continue

    liste=[]

    #BeautifulSoup-Teil
    html=line[2].encode('utf-8').decode('unicode_escape') #decode/encode um Sonderzeichen auszublenden, z.B. \n oder \t... KP aber wie das genau funktioniert
    doc=BeautifulSoup(html, "lxml")

    # Hier wird die if-Abfrage fuer verschiedenen Websiten durchgefuehrt
    ### Independent:
    if line[1].startswith("http://www.independent.co.uk"):
      table = doc.find_all("p")
      final_list = []
      liste=[line[0], line[1]]
      
      # Jeder gefundene Tag wird einzeln abgelesen
      for zeile in table:
        strr = zeile.get_text() 

        # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht. Es kann sein, dass die drei Befehle ueberfluessig sind... KP was sie genau machen...
        strr = os.linesep.join([s for s in strr.splitlines() if s])
        strr = "".join([s for s in strr.strip().splitlines(True) if s.strip("\r\n")])
        strr = strr.replace("\r", "").replace("\n", "")
        
        # hier wird jeder Tag zu einer Liste hinzugefuegt
        final_list.append(strr)

      strin=' . '.join(final_list) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " . ")
     
      writer.writerow([liste[0],liste[1],strin]) # schreibt alles in einer Zeile von der output-Datei

    ### The Guardian
    elif line[1].startswith("https://www.theguardian.com"):
      table = doc.find_all("p")
      final_list = []
      liste=[line[0], line[1]]
      
      # Jeder gefundene Tag wird einzeln abgelesen
      for zeile in table:
        strr = zeile.get_text() 

        # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht. Es kann sein, dass die drei Befehle ueberfluessig sind... KP was sie genau machen...
        strr = os.linesep.join([s for s in strr.splitlines() if s])
        strr = "".join([s for s in strr.strip().splitlines(True) if s.strip("\r\n")])
        strr = strr.replace("\r", "").replace("\n", "")
        
        # hier wird jeder Tag zu einer Liste hinzugefuegt
        final_list.append(strr)

      strin=' . '.join(final_list) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " . ")
     
      writer.writerow([liste[0],liste[1],strin]) # schreibt alles in einer Zeile von der output-Datei

    ### Spiegel
    elif line[1].startswith("https://www.spiegel.de"):
      pass

    # usw.


# schliesst die Dateien
inf.close()
outf.close()



      #for d in doc.findALL("div", attrs={"class": "text-wrapper"}):
      # table.append(d.findALL("p"))
      #class_="text-wrapper" attrs={"itemprop": "articleBody"}



       #strin=strin.replace("\n"," ").replace("  ","TT")
      #liste.append(strin)
      #print(strin.replace('\n',''))
      #print(liste[2])
#AB HIER!!!
# liste=[]#

# with open('./test.csv', newline='', encoding='utf-8') as filer:
#   rd = csv.reader(filer, delimiter=',', quoting=csv.QUOTE_ALL)

#   liste.extend(rd)#


#   for row in rd:
#     if not row:
#       continue
    
#       #r.encode('utf-8').decode('unicode_escape')
#     url=r[1].encode('utf-8').decode('unicode_escape')

#     if url.startswith("http://www.independent.co.uk"):
#       site = "http://www.independent.co.uk"




#     html=r[2].encode('utf-8').decode('unicode_escape')

#     doc=BeautifulSoup(html, "lxml")
#       table=doc.findAll("p")
#         r[2]=r[2].replace("table")

#     Print(url)
#     print(html)
#     liste.append(row)
# filer.close()

# with open('./output.csv', 'w', newline='', encoding='utf-8') as ff:
#   file=csv.writer(ff, delimiter=',', quoting=csv.QUOTE_ALL)
#   for rows in liste:
#     file.writerow(rows)
#     #file.writerow([codecs.encode(str(rows), 'unicode_escape').decode('utf-8')])
# ff.close()


        #table = doc.findAll("p")
      #text = extract_text(doc, site)

      #csv.writer(target_file, [site, url, text])

      #print(site)
      #print(html)
      #print(url)

      
      

      #with open("output.csv","w") as target:
       # file = csv.writer(target)
        #file.writerow([site, url])
        #for row in table:
         # file.writerow([row.text])

#filer.close()
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


