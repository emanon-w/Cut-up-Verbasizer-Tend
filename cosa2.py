import dearpygui.dearpygui as dpg
import random

dpg.create_context()
dpg.create_viewport(title='Cut-up Verbasizer', width=1280, height=720, x_pos=0, y_pos=0,
                    min_width=500, min_height=500)

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
numero_frasi = 5
lista_frasi = []

#funzioni/callback
def Cancella_tutto (_, __):
    for frasi in lista_frasi:
        dpg.set_value(frasi, "")

def Aggiungi_Riga(_, __):
    global numero_frasi
    numero_frasi += 1
    testo = dpg.add_input_text(label="Inserisci qui la nuova frase:", before = spaziatore)
    lista_frasi.append(testo)
    print(numero_frasi)

def Elimina_Riga(_, __): 
    global numero_frasi
    if numero_frasi > 5:
        dpg.delete_item (lista_frasi.pop())
        numero_frasi -= 1
        print(numero_frasi)

def Cut_up(_,__):
    for frasi in range(numero_frasi):
        () 
        
    random.shuffle(lista_frasi)
    dpg.add_text((lista_frasi), before=ultima_barra)

#window
with dpg.window(label="Cut-up Verbasizer", width=1200, height=720) as w:
    dpg.bind_font(grassetto_font)

    dpg.add_text("Benvenuti nel Verbasizer. Inserisci le frasi negli spazi sottostanti per iniziare:")
    dpg.add_separator()
    dpg.add_spacer()

#button
    with dpg.group(horizontal=True):
        button2= dpg.add_button(label="Aggiungi nuova riga", callback = Aggiungi_Riga)
        button3= dpg.add_button(label="Elimina riga", callback = Elimina_Riga)

    for i in range(numero_frasi):
        frasi = dpg.add_input_text(default_value = "")
        dpg.add_spacer()

    dpg.add_separator()
    spaziatore = dpg.add_spacer()

    with dpg.group(horizontal=True):
        button4= dpg.add_button(label="Cancella Tutto", callback=Cancella_tutto)
        button1= dpg.add_button(label="Realizza il cut-up",callback=Cut_up)
  
    ultima_barra = dpg.add_separator()
    dpg.add_spacer()

#immagine Bowie
    width, height, channels, data = dpg.load_image("Immagini\\Bowie.jpg")
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