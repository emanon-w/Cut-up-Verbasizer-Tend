import dearpygui.dearpygui as dpg
import random
import requests
import xml.etree.ElementTree as ET
import math


dpg.create_context()
dpg.create_viewport(title='Cut-up Verbasizer', width=1280, height=720, x_pos=0, y_pos=0,
                    min_width=600, min_height=600)

#font
with dpg.font_registry():
    default_font = dpg.add_font("Font\\times.ttf",20)
    grassetto_font= dpg.add_font("Font\\Montserrat-Bold.ttf",20)

#theme
with dpg.theme() as global_theme:

    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (105, 140, 123), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (100,100,100), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 10)

    with dpg.theme_component(dpg.mvInputText):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (50,50,50), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6, category=dpg.mvThemeCat_Core)

    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,(205,205,205), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text,(255,255,255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (55,55,55), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6, category=dpg.mvThemeCat_Core)
    with dpg.theme_component(dpg.mvWindowAppItem):
        ()

dpg.bind_theme(global_theme)

#variabili
lista_frasi = []
lista_risultati = []

#funzioni/callback
def Cancella_tutto (_, __):
    for frasi in lista_frasi:
        dpg.set_value(frasi, "")

def Aggiungi_Riga(_, __):
    frasi = dpg.add_input_text(label="Inserisci qui la nuova frase:", before = spaziatore)
    lista_frasi.append(frasi)

def Elimina_Riga(_, __): 
    if len(lista_frasi) > 5:
        dpg.delete_item (lista_frasi.pop())

def Cut_up(_,__):
    global risultato
    lista_parole = []
    for frasi in lista_frasi:
        parole = dpg.get_value(frasi)
        taglio = parole.split()
        lista_parole.extend(taglio)
    random.shuffle(lista_parole)
    risultato = dpg.add_text(" ".join(lista_parole), before=barra_secondaria, wrap=1000, bullet=True)
    lista_risultati.append(risultato)

def Elimina_Risultati(_,__):
    for res in lista_risultati:
        dpg.delete_item(res)
    lista_risultati.clear()

def notizie(_,__):
    res = requests.get("https://www.ilpost.it/feed") #sito RSS
    stringa = ET.fromstring(res.text)

    channel = stringa.find("channel")
    notizie = set()

    for notizia in channel.findall("item"):
        if len(notizie) == 2 * len(lista_frasi):
            break
        notizie.add(notizia.find("title").text)

    notizie = list(notizie)
    notizie_per_riga = len(notizie) // len(lista_frasi)
    
    for i, frasi in enumerate(lista_frasi):
        dpg.set_value(frasi, ' '.join(notizie[i * notizie_per_riga:i * notizie_per_riga + notizie_per_riga]))

#window
with dpg.window(label="Cut-up Verbasizer", width=1280, height=720, horizontal_scrollbar=True) as w:
    dpg.bind_font(grassetto_font)

    dpg.add_spacer()
    dpg.add_text("Benvenuti nel Verbasizer. Inserisci le frasi negli spazi sottostanti per iniziare:")
    dpg.add_separator()
    dpg.add_spacer()

    with dpg.group(horizontal=True):
        button2= dpg.add_button(label="Aggiungi nuova riga", callback = Aggiungi_Riga)
        button3= dpg.add_button(label="Elimina riga", callback = Elimina_Riga)

    dpg.add_separator()

    for i in range(5):
        frasi = dpg.add_input_text(label="Inserisci qui la frase:")
        lista_frasi.append(frasi)
        dpg.add_spacer()

    dpg.add_separator()
    spaziatore = dpg.add_spacer()

    with dpg.group(horizontal=True):
        button4= dpg.add_button(label="Cancella Tutto", callback=Cancella_tutto, tag="svuota")
        button5= dpg.add_button(label="Elimina risultati", callback=Elimina_Risultati, tag="elimina risultati")
        button1= dpg.add_button(label="Realizza il cut-up",callback=Cut_up)
        button6= dpg.add_button(label="Carica notizie dai giornali", callback=notizie)
        with dpg.tooltip("svuota"):
            dpg.add_text("Svuota gli elementi presenti nelle caselle di testo.")
        with dpg.tooltip("elimina risultati"):
            dpg.add_text("Elimina i testi risultati dal Cut up")

    with dpg.child_window(width=1050, height=250, menubar=True, horizontal_scrollbar=True):
            barra_secondaria = dpg.add_spacer()
  
    dpg.add_spacer()
    ultima_barra = dpg.add_separator()
    dpg.add_spacer()
    
    with dpg.item_handler_registry():
        dpg.add_item_visible_handler(user_data=w)

    width, height, channels, data = dpg.load_image("Immagini\\Bowie.jpg") #immagine Bowie
    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")
    dpg.add_image("texture_tag")
    dpg.add_text("David Bowie mentre utilizza il Cut-up per scrivere le proprie canzoni negli anni '70")
    dpg.add_spacer()


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window(w,True)
dpg.start_dearpygui()
dpg.destroy_context()

#Corrado infame in data 09 Luglio 2023 alle ore 01:41 ha offerto un drink a Giorgio Licuria anziché 
#al sottoscritto quindi non può usare questo programma. 

#Dedicato a Edamame