import dearpygui.dearpygui as dpg
import random

dpg.create_context()
dpg.create_viewport(title='Cut-up Verbasizer', width=1280, height=720, x_pos=0, y_pos=0,
                    min_width=600, min_height=600)

#font
with dpg.font_registry():
    default_font = dpg.add_font("Font\\times.ttf",20)
    grassetto_font= dpg.add_font("Font\\times-new-roman-bold.otf",20)

#theme
with dpg.theme() as global_theme:

    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (105, 140, 123), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (100,100,100), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6, category=dpg.mvThemeCat_Core)

    with dpg.theme_component(dpg.mvInputText):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (50,50,50), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6, category=dpg.mvThemeCat_Core)

    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,(205,205,205), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text,(255,255,255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (55,55,55), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6, category=dpg.mvThemeCat_Core)

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
    risultato = dpg.add_text(" ".join(lista_parole), before=ultima_barra)
    lista_risultati.append(risultato)
    dpg.set_value(operazione, risultato)

def Elimina_Risultati(_,__):
    for res in lista_risultati:
        dpg.delete_item(res)
    lista_risultati.clear()

#window
with dpg.window(label="Cut-up Verbasizer", width=1200, height=720, horizontal_scrollbar=True) as w:
    dpg.bind_font(grassetto_font)

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

        with dpg.tooltip("svuota"):
            dpg.add_text("Svuota le caselle di testo.")
        with dpg.tooltip("elimina risultati"):
            dpg.add_text("Elimina i testi risultati dal Cut up")

    with dpg.child_window(width=1000, height=200, menubar=False):
        operazione = dpg.add_text("")


    ultima_barra = dpg.add_separator()
    dpg.add_spacer()

    width, height, channels, data = dpg.load_image("Immagini\\Bowie.jpg") #immagine Bowie
    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")
    dpg.add_image("texture_tag")
    dpg.add_text("David Bowie alle prese con il cut-up.")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window(w,True)
dpg.start_dearpygui()
dpg.destroy_context()

#Corrado infame in data 09 Luglio 2023 alle ore 01:41 ha offerto un drink a Giorgio Licuria anziché 
#al sottoscritto quindi non può usare questo programma. 

#Dedicato a Edamame