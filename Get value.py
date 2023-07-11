import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

def print_input_text():
    print(dpg.get_value("input_text"))

    print(dpg.get_value(input_text)) #aggiunto io

with dpg.window() as win1:
    dpg.add_input_text(tag="input_text")

    input_text = dpg.add_input_text(label="Maronn") #aggiunto io

    dpg.add_button(label="Button",callback=print_input_text)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()