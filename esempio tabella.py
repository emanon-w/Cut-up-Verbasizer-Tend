import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=1200, height=720,x_pos=0,y_pos=0, max_width=1920, max_height=1080)

with dpg.window(label="Demo", width=1200, height=720, horizontal_scrollbar=True) as w:

    with dpg.table():

        # use add_table_column to add columns to the table,
        # table columns use slot 0
        dpg.add_table_column()
        dpg.add_table_column()
        dpg.add_table_column()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window(w, True)
dpg.start_dearpygui()
dpg.destroy_context()