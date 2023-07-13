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

class CutUp:

    def __init__(self):
        self.lista_input_text = []
        self.text = None

    def Aggiungi_Input_Text(self, input_text):
        self.lista_input_text.append(input_text)

    def Cancella_tutto (self, _, __):
        for input_text in self.lista_input_text:
            dpg.set_value(input_text, "")

    def New_Line(self, _, __):
        nuovo_input_text = dpg.add_input_text(label="Inserisci qui la nuova frase:", before=spaziatore) #stessa posizione before=spaziatore del rigo sopra, add_same_line non va 
        self.lista_input_text.append(nuovo_input_text)

    def Delete_Line(self, _, __):
        if len(self.lista_input_text) > 5:
            dpg.delete_item(self.lista_input_text.pop())

    def Cut_up(self, _, __):
        parole = []

        for input_text in self.lista_input_text:
            testo = dpg.get_value(input_text)
            parole += testo.split()

        random.shuffle(parole)
        if self.text is not None:
            dpg.delete_item(self.text)
        self.text = dpg.add_text(" ".join(parole), before=fine)

cut_up = CutUp()

#window
with dpg.window(label="Cut-up Verbasizer", width=1200, height=720) as w:
    dpg.bind_font(grassetto_font)

    dpg.add_text("Benvenuti nel Verbasizer. Inserisci le frasi negli spazi sottostanti per iniziare:")
    dpg.add_separator()
    dpg.add_spacer()

#button
   
    with dpg.group(horizontal=True):
        button2= dpg.add_button(label="Aggiungi nuova riga", callback=cut_up.New_Line)
        button3= dpg.add_button(label="Elimina riga", callback =cut_up.Delete_Line)

    for _ in range(5):
        with dpg.group(horizontal=True):
            input_text = dpg.add_input_text(label="Inserisci qui la frase:", default_value="")
            cut_up.Aggiungi_Input_Text(input_text)
            dpg.add_spacer()

    dpg.add_separator()
    spaziatore = dpg.add_spacer()

    with dpg.group(horizontal=True):
        button4= dpg.add_button(label="Cancella Tutto", callback=cut_up.Cancella_tutto)
        button1= dpg.add_button(label="Realizza il cut-up",callback=cut_up.Cut_up)


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

#Dedicato a Edamame<3

#Cose da fare:
#Aggiunegre una barra di scorrimento orizzontale
#Allineare le barre di input testo 