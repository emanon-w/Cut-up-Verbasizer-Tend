import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Verbasizer Tendiano', width=1200, height=720)

with dpg.font_registry():
    default_font = dpg.add_font("Font\\times.ttf",20)
    grassetto_font= dpg.add_font("Font\\times-new-roman-bold.otf",20)

with dpg.theme() as global_theme:

    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 140, 23), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (55,55,55), category=dpg.mvThemeCat_Core)
    with dpg.theme_component(dpg.mvInputText):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (40, 155, 213), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)

#window
with dpg.window(label="Verbasizer", width=1280, height=720,) as w:
    dpg.bind_font(grassetto_font)
    dpg.add_text("Benvenuti nel Verbasizer")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="Inserisci la prima frase:")
    dpg.add_input_text(label="Inserisci la seconda frase:")
    dpg.add_input_text(label="Inserisci la terza frase:")
    dpg.add_input_text(label="Inserisci la quarta frase:")
    dpg.add_input_text(label="Inserisci la quinta frase:")
    dpg.add_text()
    dpg.load_image("")

    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

#Corrado bastardo ha offerto un drink a Giorgio quindi non può usare questo programma