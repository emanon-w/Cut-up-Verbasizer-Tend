import dearpygui.dearpygui as dpg

with dpg.handler_registry():
    dpg.create_context()
    dpg.create_window(title="Esempio", width=500, height=300)
    
    with dpg.handler_registry():
        dpg.create_text("Widget 1")
        dpg.layout.HAlignNext()  # Imposta l'allineamento orizzontale dei widget successivi

        dpg.create_button("Widget 2")
        dpg.layout.HAlignNext()

        dpg.create_slider_float("Widget 3")
        dpg.layout.HAlignNext()

        dpg.create_input_text("Widget 4")
        dpg.layout.HAlignNext()

    dpg.show_context()

dpg.destroy_context()
