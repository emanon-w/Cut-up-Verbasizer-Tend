import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=1200, height=720,x_pos=0,y_pos=0)

def popup():
    with dpg.popup():
        dpg.add_text("Cazzo")

with dpg.window(width=1200,height=720) as w:
    b = dpg.add_button(label="Right Click...")
    t = dpg.add_text("<None>")
    with dpg.popup(t, tag="__demo_popup1"):
        dpg.add_text("Aquariam")
        dpg.add_separator()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window(w, True)
dpg.start_dearpygui()
dpg.destroy_context()