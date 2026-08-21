import customtkinter as ctk
import theme_config

from tkintermapview import TkinterMapView
from PIL import Image
from src.Local import Local


class GraphicInterface:
    def __init__(self):
        ctk.set_appearance_mode(theme_config.CONFIG_THEME_APLICATION)
        ctk.set_default_color_theme(theme_config.CONFIG_THEME_BUTTON)

        self.__interface()
    
    
    # This functions check if number
    def __validate_number(self, p: str) -> bool:
        if p == "" or p == "-":
            return True
        try:
            float(p)
            return True
        except ValueError:
            return False
    # END
    
    # This functions create a window
    def __interface(self):
        window = ctk.CTk()
        window.title(theme_config.CONFIG_TITLE)
        window.geometry(theme_config.CONFIG_SIZE_CONFIG)
        
        
        container_coordenates = ctk.CTkFrame(window)
        container_coordenates.pack(padx=10, pady=10)
        
        self.__create_empty_space(window, container_coordenates)
        
        window.mainloop()
    # END
    
    # Create a coordinate space
    def __create_empty_space(self, window: ctk.CTk, container: ctk.CTkFrame):
        validate = (window.register(self.__validate_number), '%P')
        
        title = ctk.CTkLabel(
            container,
            text="Enter the coordinate value below.",
            pady=10,
            compound="center",            # Configure position
            font=("Arial", 100, "bold"),# Configure font
            text_color="#FFFFFF"      # Configure title color
        )
        title.pack(pady=10, padx=10)
        
        img = ctk.CTkImage(Image.open("assets/lupa.png"), size=(50, 50))
        img_label = ctk.CTkLabel(
            container,
            image=img
        )
        img_label.image = img
        img_label.pack(compound="right", padx=10, pady=10)
        
        description = ctk.CTkLabel(container, text="Put here the values of coordinates:")
        description.pack(pady=10)
        
        latitude = ctk.CTkEntry(
            container, validate="key", validatecommand=validate
        )
        latitude.pack(pady=10, padx=10)
        
        longitude = ctk.CTkEntry(
            container, validate="key", validatecommand=validate
        )
        longitude.pack(pady=10, padx=10)
        
        output = ctk.CTkLabel(container, text="")
        output.pack(padx=10, pady=10)
        
        map_widget = TkinterMapView(container, width=600, height=400, corner_radius=0)
        map_widget.pack(padx=10, pady=10)

        # Initial Position (ex: Brasil)
        map_widget.set_position(-14.2350, -51.9253)
        map_widget.set_zoom(4)

        def __insert_value():
            if not latitude.get() or not longitude.get():
                output["text"] = "Fill both the field!"
                return

            lat = float(latitude.get())
            long = float(longitude.get())
            local0 = Local(lat, long)
            local0.mapa()

            # Atualiza o centro do mapa e adiciona um marcador
            map_widget.set_position(lat, long)
            map_widget.set_zoom(15)
            map_widget.set_marker(lat, long, text="Local Encontrado")

            output["text"] = local0.pesquisa()["Endereço"]

        enter = ctk.CTkButton(container, text="ENTER", command=__insert_value)
        enter.pack(pady=10)