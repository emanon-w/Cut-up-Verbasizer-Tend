import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=1200, height=720,x_pos=0,y_pos=0)

with dpg.window(label="Demo", width=1200, height=720, horizontal_scrollbar=True) as w:
    demo.show_demo()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window(w, True)
dpg.start_dearpygui()
dpg.destroy_context()