from queue import Queue # This module implements queues (FIFO) for multiple thread programming. The python Queue object can be easily used to solve the multi-producer,
                        # multi-consumer problem, where messages must be exchanged safely between multiple threads. 
from threading import Thread # Ausführungsreihenfolge in der Abarbeitung eines Programmes - Funktionsaufruf. 
                             # Der Vorteil von Threads gegenüber Prozessen besteht darin, dass sich die Threads eines Prozesses denselben Speicherbereich für globale Variablen teilen. 
                             # Verändert ein Thread eine globale Variable, ist der neue Wert auch in dieser Variablen sofort für alle anderen Threads des Prozesses sichtbar.
import csv
import codecs # Module for encoders and decoders.
import logging # This module defines functions and classes which implement a flexible event logging systems for application and libraries.


writer_queue = Queue()  # job format: {"path": path, "line": ["some_url", "bla bla", "test123"]}
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) #Sets the threshold for this logger to logging.Debug. Logging messages which are less severe than logging.debug will be ignored. 


class Writer(Thread): # Die Klasse Writer erbt von Thread.
    # Der Konstruktor, wo alle Instanzattribute der Klasse angelegt werden.
    def __init__(self): # Das erste Element innerhalb der Parameterliste muss immer self sein. 
                        #Über den Parameter self erhält die Methode beim Aufruf eine Referenz auf das Objekt für welches sie aufgerufen wird.
        super(Writer, self).__init__()
        self.open_files = dict()

    def run(self):
        while True:
            job = writer_queue.get()
            #logger.debug("writer_queue size: %s", writer_queue.qsize())
            self.write(job["path"], job["line"])

    def write(self, path, line):
        try:
            if path in self.open_files:
                file = self.open_files[path]
            else:
                file = open(path, 'a', encoding="utf-8") # a for appending that means that all writes append to the end of the file.
                self.open_files[path] = file
            wr = csv.writer(file, quoting=csv.QUOTE_ALL) # Gibt an, ob und wann Spaltenwerte mit quotechar umschlossen werden sollen.
                                                        # Hier: Alle Spaltenwerte werden umschlossen mit "".
            wr.writerow([codecs.encode(str(e), 'unicode_escape').decode('utf-8') for e in line])
            file.flush() # Hier wird die Datei zwischengespeichet, ohne sie zu schließen
        except Exception as err:
            logger.error("Could not write to %s Error: %s", path, str(err))

# when reading this stuff later on...
# def read():
#     with open('./dump/test.csv', newline='', encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
#         for row in reader:
#             print([r.encode('utf-8').decode('unicode_escape') for r in row])or r in row])