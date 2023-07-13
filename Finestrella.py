import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Proviamo la finestrella', width=1200, height=720, x_pos=0, y_pos=0) 

with dpg.window(label = "Finestrella", horizontal_scrollbar=True) as w:
    ()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window(w,True)
dpg.start_dearpygui()
dpg.destroy_context()