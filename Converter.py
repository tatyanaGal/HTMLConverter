import csv
import bs4
import codecs
import os, sys, string, warnings
from itertools import islice
import sys
import time


# ALLGEMEIN 
# Die gecrawlten csv Datei sind folgendermassen aufgebaut:
# 1. Zeile: "Timetag","RSS","URL","html-Seite 1"
# 2. Zeile: "Timetag","RSS","URL","html-Seite 2"
# usw.
#

## Notwendig, um die langen HTML-Texte ablesen zu koennen. 
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

warnings.filterwarnings("ignore", category=UserWarning, module="bs4")


## HTML-Converter:
def text_extract(file_to_extract):

  with open(file_to_extract, newline='', encoding="utf-8") as inputFile, open("./extracted/extracted_" + sys.argv[2] + ".csv", 'w') as outputFile:
    reader = csv.reader(inputFile)
    writer = csv.writer(outputFile, delimiter=',', quoting=csv.QUOTE_ALL)
    
    # Lese bestimmte Anzahl von Zeilen ab:
    #for line in islice(reader, 200):
    for line in reader: # csv wird zeilenweise abgelesen - line = Zeile 1 usw. 
      #print("----Line checked----")
    
      #  # Leere Zeilen in csv werden uebersprungen
      # if not line: 
      #   continue

      #BeautifulSoup-Teil

      html=line[3].encode(encoding="utf-8").decode(encoding='unicode_escape', errors="strict") #decode/encode um Sonderzeichen auszublenden, z.B. \n oder \t... 
      htmlText=bs4.BeautifulSoup(html, "lxml")

      ########################## Hier wird die if-Abfrage fuer verschiedenen Webseiten durchgefuehrt
      

      ############################################################## AU News ############################################################

      ### Advertiser Australia
      #re.compile("p-text") http://rssfeeds.theadvertiser.com
      if line[1].startswith("http://rssfeeds.theadvertiser.com"):
        if htmlText.find_all(name="p", attrs={"class": "p-text"}):

          wholeText = htmlText.find_all(name="p", attrs={"class": "p-text"})
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"AU",artikel]) # schreibt alles in einer Zeile von der output-Datei



      ### Daily Telegraph Australia
      elif line[1].startswith("http://www.dailytelegraph.com.au"):

        if htmlText.find(name="div", attrs={"class": "tg-tlc-storybody cf"}):

          wholeText = htmlText.find(name="div", attrs={"class": "tg-tlc-storybody cf"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"AU",artikel]) # schreibt alles in einer Zeile von der output-Datei



      ### Herald Sun Australia FUNK NICHT
      elif line[1].startswith("http://www.heraldsun.com.au"):

        if htmlText.find(name="article", attrs={"class": "article-content"}):
        #if htmlText.find(name="article", attrs={"itemprop": "articleBody"}):

          wholeText = htmlText.find(name="article", attrs={"class": "article-content"}).find_all(name="p")
          #wholeText = htmlText.find(name="article", attrs={"itemprop": "articleBody"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"AU",artikel]) # schreibt alles in einer Zeile von der output-Datei



      ### The Age Australia FUNK NICHT
      elif line[1].startswith("http://www.theage.com.au"):

        if htmlText.find(name="div", attrs={"class": "article_body"}):

          wholeText = htmlText.find(name="div", attrs={"class": "article_body"}).find_all(name="p")
          #wholeText = htmlText.find(name="div", attrs={"itemprop": "articleBody"}).find_all("p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"AU",artikel]) # schreibt alles in einer Zeile von der output-Datei


      ### Canberra Times Australia FUNK NICHT 
      elif line[1].startswith("http://www.canberratimes.com.au"):

        if htmlText.find(name="div", attrs={"class": "article__body"}):

          wholeText = htmlText.find(name="div", attrs={"class": "article__body"}).find_all(name="p")
          #wholeText = htmlText.find(name="div", attrs={"itemprop": "articleBody"}).find_all("p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"AU",artikel]) # schreibt alles in einer Zeile von der output-Datei



      ### Mercurry Australia
      elif line[1].startswith("http://www.themercury.com.au"):

        #if htmlText.find(name="div", attrs={"class": "tg-tlc-storybody cf"}):
        #  wholeText = htmlText.find(name="div", attrs={"class": "tg-tlc-storybody cf"}).find_all(name="p")
        if htmlText.find(name="div", attrs={"class": "content"}):
          wholeText = htmlText.find(name="div", attrs={"class": "content"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"AU",artikel]) # schreibt alles in einer Zeile von der output-Datei


      ### ABC Australia
      elif line[1].startswith("http://www.abc.net.au"):
        if htmlText.find(name="div", attrs={"class": "article section"}):
          wholeText = htmlText.find(name="div", attrs={"class": "article section"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"AU",artikel]) # schreibt alles in einer Zeile von der output-Datei



      ### The West Australia
      elif line[1].startswith("https://thewest.com.au"):
        if htmlText.find_all(name="p", attrs={"class": "css-1rgmj8p"}):
          wholeText = htmlText.find_all(name="p", attrs={"class": "css-1rgmj8p"})
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"AU",artikel]) # schreibt alles in einer Zeile von der output-Datei



      ### News Australia
      elif line[1].startswith("http://www.news.com.au"):
        if htmlText.find(name="div", attrs={"id": "story"}):
          wholeText = htmlText.find(name="div", attrs={"id": "story"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"AU",artikel]) # schreibt alles in einer Zeile von der output-Datei


      ################################################################ Germany News #######################################################

      ### Spiegel
      elif line[1].startswith("https://www.spiegel.de"):
        if htmlText.find(name="div", attrs={"class": "spArticleContent"}):
          wholeText = htmlText.find(name="div", attrs={"class": "SpArticleContent"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"DE",artikel]) # schreibt alles in einer Zeile von der output-Datei


     ############################################################ UK News ##################################################################

      ### Independent
      elif line[1].startswith("http://www.independent.co.uk"):
        if htmlText.find(name="div", attrs={"class": "text-wrapper"}):
          wholeText = htmlText.find(name="div", attrs={"class": "text-wrapper"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"UK",artikel]) # schreibt alles in einer Zeile von der output-Datei



      ### The Guardian
      elif line[1].startswith("https://www.theguardian.com"):
        if htmlText.find(name="div", attrs={"itemprop": "articleBody"}):
          wholeText = htmlText.find(name="div", attrs={"itemprop": "articleBody"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"UK",artikel]) # schreibt alles in einer Zeile von der output-Datei
    


      ### BBC News UK 
      elif line[1].startswith("http://feeds.bbci.co.uk/news/rss"):
        if htmlText.find(name="div", attrs={"property": "articleBody"}):
          wholeText = htmlText.find(name="div", attrs={"property": "articleBody"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"UK",artikel]) # schreibt alles in einer Zeile von der output-Datei
    

      ### Daily Express UK
      elif line[1].startswith("http://feeds.feedburner.com"):
        if htmlText.find(name="div", attrs={"data-type": "article-body"}):
          wholeText = htmlText.find(name="div", attrs={"data-type": "article-body"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"UK",artikel]) # schreibt alles in einer Zeile von der output-Datei


      ### Daily Mail UK
      elif line[1].startswith("http://www.dailymail.co.uk"):
        if htmlText.find(name="div", attrs={"class": "articleWide cleared"}):
          wholeText = htmlText.find(name="div", attrs={"class": "articleWide cleared"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"UK",artikel]) # schreibt alles in einer Zeile von der output-Datei


      ### Evening Standard UK
      elif line[1].startswith("https://www.standard.co.uk"):
        if htmlText.find(name="div", attrs={"class": "body-content"}):
          wholeText = htmlText.find(name="div", attrs={"class": "body-content"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"UK",artikel]) # schreibt alles in einer Zeile von der output-Datei
    

      ### Financial Time UK
      elif line[1].startswith("https://www.ft.com"):
        if htmlText.find(name="section", attrs={"itemprop": "articleBody"}):
          wholeText = htmlText.find(name="section", attrs={"itemprop": "articleBody"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"UK",artikel]) # schreibt alles in einer Zeile von der output-Datei



     ################################################## US News #########################################################################
      ### BBC News  US
      elif line[1].startswith("http://feeds.bbci.co.uk/news/world/us_and_canada"):
        if htmlText.find(name="div", attrs={"property": "articleBody"}):
          wholeText = htmlText.find(name="div", attrs={"property": "articleBody"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"US",artikel]) # schreibt alles in einer Zeile von der output-Datei


      # ### NPR US
      elif line[1].startswith("http://www.npr.org/"):
        if htmlText.find(name="div", attrs={"id": "storytext"}):
          wholeText = htmlText.find(name="div", attrs={"id": "storytext"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"US",artikel]) # schreibt alles in einer Zeile von der output-Datei



      ### Reuters US + World + Politics
      elif line[1].startswith("http://feeds.reuters.com"):
        if htmlText.find(name="div", attrs={"class": "StandardArticleBody_body_1gnLA"}):
          wholeText = htmlText.find(name="div", attrs={"class": "StandardArticleBody_body_1gnLA"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"US",artikel]) # schreibt alles in einer Zeile von der output-Datei

     

      ### New York Times US + World
      elif line[1].startswith("http://rss.nytimes.com"):
        if htmlText.find(name="div", attrs={"class": "story-body story-body-1"}):
          wholeText = htmlText.find(name="div", attrs={"class": "story-body story-body-1"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"US",artikel]) # schreibt alles in einer Zeile von der output-Datei

      
      ### CNN US + World
      elif line[1].startswith("http://rss.cnn.com"):
        if htmlText.find(name="div", attrs={"class": "l-container"}):
          wholeText = htmlText.find(name="div", attrs={"class": "l-container"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"US",artikel]) # schreibt alles in einer Zeile von der output-Datei

    

      ### Associated Press US + World + Politics
      elif line[1].startswith("http://hosted2.ap.org"):
        if htmlText.find(name="div", attrs={"class": "articleBody"}):
          wholeText = htmlText.find(name="div", attrs={"class": "articleBody"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"US",artikel]) # schreibt alles in einer Zeile von der output-Datei

      

      ### Washington Post US + World + Politics
      elif line[1].startswith("http://feeds.washingtonpost.com/rss"):
        if htmlText.find(name="div", attrs={"id": "article-body"}):
          wholeText = htmlText.find(name="div", attrs={"id": "article-body"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"US",artikel]) # schreibt alles in einer Zeile von der output-Datei

      

      ### FOX News US + Worls + Politics
      elif line[2].startswith("http://feeds.foxnews.com"):
        if htmlText.find(name="div", attrs={"class": "article-body"}):
          wholeText = htmlText.find(name="div", attrs={"class": "article-body"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"US",artikel]) # schreibt alles in einer Zeile von der output-Datei

     


      ### MSNBC US
      elif line[1].startswith("http://www.msnbc.com"):
        if htmlText.find(name="section", attrs={"itemprop": "articleBody"}):
          wholeText = htmlText.find(name="section", attrs={"itemprop": "articleBody"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"US",artikel]) # schreibt alles in einer Zeile von der output-Datei




      ### CBS US + World + Politics 
      elif line[1].startswith("https://www.cbsnews.com"):
        if htmlText.find(name="div", attrs={"class": "content-primary article-page default"}):
          wholeText = htmlText.find(name="div", attrs={"class": "content-primary article-page default"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"US",artikel]) # schreibt alles in einer Zeile von der output-Datei



      
      ### ABC News US + World + Politics + International
      elif line[1].startswith("http://abcnews.go.com"):
        if htmlText.find_all(name="p", attrs={"itemprop": "articleBody"}):
          wholeText = htmlText.find_all(name="p", attrs={"itemprop": "articleBody"})
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"US",artikel]) # schreibt alles in einer Zeile von der output-Datei

    


       ### Wallstreet Journal US
      elif line[1].startswith("https://www.wsj.com"):
        if htmlText.find(name="div", attrs={"id": "article_sector"}):
          wholeText = htmlText.find(name="div", attrs={"id": "article_sector"}).find_all(name="p")
          extractedText = []
        
          # Jeder gefundene Tag wird einzeln abgelesen
          for zeile in wholeText:
            tagText = zeile.get_text() 

            # hier werden leere Zeilen, tabs und returns aus dem Tag geloescht
            tagText = tagText.replace("\r", "").replace("\n", "")
          
            # hier wird jeder Tag zu einer Liste hinzugefuegt
            extractedText.append(tagText)

          artikel=" ".join(extractedText) # joint alle Elemente aus der Liste zu einem grossen Sting (Separated mit " ")
       
          writer.writerow([line[0],line[2],"US",artikel]) # schreibt alles in einer Zeile von der output-Datei

# schliesst die Dateien
  inputFile.close()
  outputFile.close()

def main():
  if len(sys.argv) == 3:
    text_extract(sys.argv[1])
  else:
    print("Wrong parameters: python3 Converter.py /path/to/website_downloads_YYYY-MM-DD.csv website_downloads_YYYY-MM-DD")
    return

if __name__ == "__main__":
  main()
