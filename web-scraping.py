import requests #ottenere informazioni dal web?
import xml.etree.ElementTree as ET #XML Parser

res = requests.get("https://www.ansa.it/sito/ansait_rss.xml") #sito RSS
stringa = ET.fromstring(res.text)   #prende il testo ottenuto dalla requests e lo "parsa" cioè dà una struttura agli oggetti
                                    #solitamente ad albero
channel = stringa.find("channel")   #trova il primo elemento con il tag "channel"
notizie = set() #come una lista ma senza duplicati
notizie2 = set()
for notizia in channel.findall("item"): #findall trova tutti gli elementi con il tag "item"
    if len(notizie) == 10: #numero massimo di notizie
        break
    notizie.add(notizia.find("title").text) #l'ansa mette i titoli in questa classe
    notizie.add(notizia.find("description").text) #l'ansa mette i sotto-titoli in questa classe

print("\n".join(notizie))