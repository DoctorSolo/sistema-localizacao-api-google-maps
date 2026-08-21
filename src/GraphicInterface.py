import customtkinter as ctk
import theme_config

from tkintermapview import TkinterMapView
from src.Local import Local
from PIL import Image


class GraphicInterface:
    def __init__(self):
        ctk.set_appearance_mode(theme_config.CONFIG_THEME_APLICATION)
        ctk.set_default_color_theme(theme_config.CONFIG_THEME_BUTTON)

        self.__interface()
    # END
    
    
    # This functions check if number
    def __validate_number(self, p) -> bool:
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
        container_coordenates.pack(side="left", padx=10, pady=10)
        
        container_button = ctk.CTkFrame(window)
        container_button.pack(padx=10, pady=10)
        
        container_map = ctk.CTkFrame(window)
        container_map.pack(side="right", padx=10, pady=10)
        
        container_output = ctk.CTkFrame(window)
        container_output.pack(side="bottom", padx=10, pady=10)
        
        map = self.__generate_map(container_map)
        out = self.__output(container_output)
        
        latitude, longitude = self.__create_empty_space(window, container_coordenates)
        
        enter_button = ctk.CTkButton(
            container_button, text="ENTER", command=lambda: self.__inset_value(map, latitude, longitude, out)
        )
        enter_button.pack(padx=10, pady=10)
        
        window.mainloop()
    # END
    
    
    # This function generate a title for a window
    def __generate_title(self, frame: ctk.CTkFrame):
        img = ctk.CTkImage(Image.open("assets/lupa.png"), size=(100, 100))
        
        title = ctk.CTkLabel(
            frame,
            image=img,
            text="Enter the coordinate value below!",
            pady=10,
            compound="left",
            font=("Arial", 30, "bold"),
            text_color="#FFFFFF"
        )
        title.image = img
        title.pack(padx=10, pady=10)
    # END
    
    
    def __output(self, frame: ctk.CTkFrame, text=""):
        output = ctk.CTkLabel(frame, text=text)
        output.grid(padx=10, pady=10)
        return output
    # END
    
    
    def __generate_map(self, frame: ctk.CTkFrame, latitude=-14.2350, longitude=-51.9253):
        map_widget = TkinterMapView(frame, width=600, height=400, corner_radius=0)
        map_widget.pack(padx=10, pady=10)
        
        map_widget.set_position(latitude, longitude)
        map_widget.set_zoom(4)
        return map_widget
    # END
    
    
    def __update_map(self, map_widget: TkinterMapView, latitude, longitude):
        map_widget.set_position(latitude, longitude)
        map_widget.set_zoom(15)
        map_widget.set_marker(latitude, longitude, text="Local Found!")
    # END
    
    
    def __inset_value(self, map_widget: TkinterMapView, latitude, longitude, output):
        if not latitude.get() or not longitude.get():
            output["text"] = "Fill both the field!"
            return
        
        lat = float(latitude.get())
        long = float(longitude.get())
        local = Local(lat, long)
        local.mapa()
        
        self.__update_map(map_widget, lat, long)
        
        output["text"] = local.pesquisa["Endereço"]
    # END
    
    
    # Create a coordinate space
    def __create_empty_space(self, window: ctk.CTk, container: ctk.CTkFrame):
        validate = (window.register(self.__validate_number), '%P')
        
        self.__generate_title(container)
        
        description_latitude = ctk.CTkLabel(container, text="Put here a latitude:")
        description_latitude.pack(pady=10, padx=30)
        
        latitude = ctk.CTkEntry(
            container, validate="key", validatecommand=validate
        )
        latitude.pack(pady=10, padx=30)
        
        description_longitude = ctk.CTkLabel(container, text="Put here a longitude:")
        description_longitude.pack(pady=10, padx=30)
        
        longitude = ctk.CTkEntry(
            container, validate="key", validatecommand=validate
        )
        longitude.pack(pady=10, padx=30)
        
        return latitude, longitude
    # END
    
    
    
    
    