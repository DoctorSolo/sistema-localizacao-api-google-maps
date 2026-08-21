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
        
        # 1. Painel principal da esquerda (container pai)
        left_panel = ctk.CTkFrame(window, fg_color="transparent")
        left_panel.pack(side="left", fill="both", expand=True, padx=5, pady=10)
        
        # 2. Container de coordenadas (fica no topo do painel esquerdo)
        container_coordenates = ctk.CTkFrame(left_panel)
        container_coordenates.pack(side="top", fill="both", expand=True, padx=5, pady=5)
        
        # 3. Container de saída (fica embaixo do de coordenadas)
        container_output = ctk.CTkFrame(left_panel)
        container_output.pack(side="bottom", fill="both", expand=True, padx=5, pady=5)
        
        # 4. Container do mapa (painel da direita)
        container_map = ctk.CTkFrame(window)
        container_map.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        
        map = self.__generate_map(container_map)
        out = self.__output(container_output)
        
        self.__create_empty_space(window, container_coordenates, map, out, container_output)
        
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
        title.pack(fill="both", expand=True, padx=10)
    # END
    
    
    def __output(self, frame: ctk.CTkFrame, text=""):
        output = ctk.CTkLabel(
            frame, 
            text=text, 
            wraplength=500,
            pady=10,
            compound="left",
            font=("Arial", 15, "bold"),
            text_color="#FFFFFF"
            )
        output.pack(pady=100, padx=10)
        return output
    # END
    
    
    def __generate_map(self, frame: ctk.CTkFrame, latitude=-14.2350, longitude=-51.9253):
        map_widget = TkinterMapView(frame, width=600, height=720, corner_radius=0)
        map_widget.pack(fill="both", expand=True, padx=10, pady=10)
        
        map_widget.set_position(latitude, longitude)
        map_widget.set_zoom(4)
        return map_widget
    # END
    
    
    def __update_map(self, map_widget: TkinterMapView, latitude, longitude):
        map_widget.set_position(latitude, longitude)
        map_widget.set_zoom(15)
        map_widget.set_marker(latitude, longitude, text="Local Found!")
    # END
    
    
    def __inset_value(self, container: ctk.CTkFrame, map_widget: TkinterMapView, latitude, longitude, output: ctk.CTkLabel):
        if not latitude.get() or not longitude.get():
            output.destroy()
            self.__output(container, "Fill both the field!")
            return
        
        lat = float(latitude.get())
        long = float(longitude.get())
        local = Local(lat, long)
        local.mapa()
        
        self.__update_map(map_widget, lat, long)
        
        output.destroy()
        self.__output(container, local.pesquisa())
    # END
    
    
    # Create a coordinate space
    def __create_empty_space(self, window: ctk.CTk, container: ctk.CTkFrame, map: TkinterMapView, out, out_container):
        validate = (window.register(self.__validate_number), '%P')
        
        self.__generate_title(container)
        
        description_latitude = ctk.CTkLabel(container, text="Put here a latitude:")
        description_latitude.pack(padx=5)
        
        latitude = ctk.CTkEntry(
            container, validate="key", validatecommand=validate
        )
        latitude.pack()
        
        description_longitude = ctk.CTkLabel(container, text="Put here a longitude:")
        description_longitude.pack(padx=5)
        
        longitude = ctk.CTkEntry(
            container, validate="key", validatecommand=validate
        )
        longitude.pack()
        
        enter_button = ctk.CTkButton(
            container, text="ENTER", command=lambda: self.__inset_value(out_container, map, latitude, longitude, out)
        )
        enter_button.pack(padx=10, pady=30)
    # END
    
    