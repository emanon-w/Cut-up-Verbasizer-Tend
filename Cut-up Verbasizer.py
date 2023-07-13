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
numero_stringa = 5

#funzioni/callback
def Cancella_tutto (sender, app_data):
    print(f"sender is: {sender}")
    print(f"app_data is: {app_data}")
    dpg.set_value(input_text1,"")
    dpg.set_value(input_text2,"")
    dpg.set_value(input_text3,"")
    dpg.set_value(input_text4,"")
    dpg.set_value(input_text5,"")

def New_Line(sender1, app_data1):
    print(f"sender is: {sender1}")
    print(f"app_data is: {app_data1}")
    global numero_stringa
    global nuovo_testo
    global inserisci
    numero_stringa += 1
    nuovo_testo = dpg.add_input_text(label="Inserisci qui la nuova frase:", before=spaziatore) #stessa posizione before=spaziatore del rigo sopra, add_same_line non va 
    print(numero_stringa)
    return numero_stringa

#Da scrivere - Delete_Line
def Delete_Line(sender2, app_data2):
    print(f"sender is: {sender2}")
    print(f"app_data is: {app_data2}")
    #dpg.delete_item(con l'indice -1 nella lista delle frasi)



def Cut_up(sender3,app_data3):
    print(f"sender is: {sender3}")
    print(f"app_data is: {app_data3}")

    frase1 = dpg.get_value(input_text1)
    frase2 = dpg.get_value(input_text2)
    frase3 = dpg.get_value(input_text3)
    frase4 = dpg.get_value(input_text4)
    frase5 = dpg.get_value(input_text5)

    taglio1 = frase1.split()
    taglio2 = frase2.split()
    taglio3 = frase3.split()
    taglio4 = frase4.split()
    taglio5 = frase5.split()

    Verbasize = taglio1 + taglio2 + taglio3 + taglio4 + taglio5
    random.shuffle(Verbasize)
    dpg.add_text(" ".join(Verbasize), before=fine)


#window
with dpg.window(label="Cut-up Verbasizer", width=1200, height=720) as w:
    dpg.bind_font(grassetto_font)

    dpg.add_text("Benvenuti nel Verbasizer. Inserisci le frasi negli spazi sottostanti per iniziare:")
    dpg.add_separator()
    dpg.add_spacer()

#button
   
    with dpg.group(horizontal=True):
        button2= dpg.add_button(label="Aggiungi nuova riga", callback=New_Line)
        button3= dpg.add_button(label="Elimina riga", callback =Delete_Line)

    with dpg.group(horizontal=True):   
        input_text1 = dpg.add_input_text(label="Inserisci qui la prima frase:", default_value="")
        dpg.add_spacer()

    with dpg.group(horizontal=True):
        input_text2 = dpg.add_input_text(label="Inserisci qui la seconda frase:", default_value="")
        dpg.add_spacer()

    with dpg.group(horizontal=True):
        input_text3 = dpg.add_input_text(label="Inserisci qui la terza frase:", default_value="")
        dpg.add_spacer()

    with dpg.group(horizontal=True):
        input_text4 = dpg.add_input_text(label="Inserisci qui la quarta frase:", default_value="")
        dpg.add_spacer()

    with dpg.group(horizontal=True):
        input_text5 = dpg.add_input_text(label="Inserisci qui la quinta frase:", default_value="")
        dpg.add_spacer()
    
    dpg.add_separator()
    spaziatore = dpg.add_spacer()

    with dpg.group(horizontal=True):
        button4= dpg.add_button(label="Cancella Tutto", callback=Cancella_tutto)
        button1= dpg.add_button(label="Realizza il cut-up",callback=Cut_up)
    
    
    
  
    fine = dpg.add_separator()
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