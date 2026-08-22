import customtkinter as ctk
import theme_config
import webbrowser

from tkintermapview import TkinterMapView
from src.SearchLocal import SearchLocal
from src.AIAgent_Gemini import AIAgent_Gemini
from src.AIAgent_Ollama import AIAgent_Ollama
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
        
        top_container = ctk.CTkFrame(window, fg_color='transparent')
        top_container.pack(side="top", fill="both", expand=True)
        
        bottom_container = ctk.CTkFrame(window, fg_color='transparent')
        bottom_container.pack(side="bottom", fill="x", expand=False)
        
        # 1. Painel principal da esquerda (container pai)
        left_panel = ctk.CTkFrame(top_container, fg_color="transparent")
        left_panel.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        # 2. Description Container (Pather)
        description_container = ctk.CTkFrame(left_panel, fg_color='transparent')
        description_container.pack(side='bottom', fill='both', expand=True)
        
        # 2. Container de coordenadas (fica no topo do painel esquerdo)
        container_coordenates = ctk.CTkFrame(left_panel)
        container_coordenates.pack(side="top", fill="x", expand=False, padx=5, pady=5)
        
        self.__description_container(description_container)
        
        # 3. Container de saída (fica embaixo do de coordenadas)
        container_output = ctk.CTkScrollableFrame(description_container)
        container_output.pack(side="bottom", fill="both", expand=True, padx=5, pady=5)
        
        # 4. Container do mapa (painel da direita)
        container_map = ctk.CTkFrame(top_container)
        container_map.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        
        map = self.__generate_map(container_map)
        out = self.__output(container_output)
        
        self.__create_empty_space(container_coordenates, map, out, container_output)
        
        self.__footer(window, bottom_container)
        
        window.mainloop()
    # END
    
    
    def __description_container(self, container: ctk.CTkFrame):
        description = ctk.CTkLabel(
            container,
            text='Description:',
            anchor='w',
            font=('Arial', 30, 'bold'),
            text_color='#FFFFFF'
        )
        description.pack(side="top", anchor='w', expand=False, padx=(20, 0))
    # END
    
    
    # This function generate a title for a window
    def __generate_title(self, frame: ctk.CTkFrame):
        img = ctk.CTkImage(Image.open("assets/lupa.png"), size=(50, 50))
        
        title = ctk.CTkLabel(
            frame,
            image=img,
            text="Enter the coordinate value below!",
            compound='left',
            font=("Arial", 30, "bold"),
            text_color="#FFFFFF"
        )
        title.image = img
        title.pack(fill="both", expand=True, padx=(10, 10))
    # END
    
    
    def __output(self, frame: ctk.CTkScrollableFrame, serch: str = ""):
        if not serch:
            text = ""
        else:
            try:
                ai_agent = AIAgent_Ollama()
                text = ai_agent.generate_response(serch)
            except Exception:
                try:
                    ai_agent = AIAgent_Gemini()
                    text = ai_agent.generate_response(serch)
                except Exception:
                    # If both failed
                    text = serch
        
        output = ctk.CTkLabel(
            frame, 
            text=text,
            wraplength=500,
            font=("Arial", 15, "bold"),
            text_color="#FFFFFF"
            )
        output.pack(pady=100, padx=10, fill="both", expand=True)
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
            return
        
        lat = float(latitude.get())
        long = float(longitude.get())
        local = SearchLocal(lat, long)
        
        self.__update_map(map_widget, lat, long)
        
        output.destroy()
        self.__output(container, local.search_summary())
    # END
    
    
    # Create a coordinate space
    def __create_empty_space(self, container: ctk.CTkFrame, map: TkinterMapView, out, out_container):
        validate = (container.register(self.__validate_number), '%P')
        
        self.__generate_title(container)
        
        lat_and_long_space = ctk.CTkFrame(container, fg_color='transparent')
        lat_and_long_space.pack(expand=True, pady=10)
        
        lat_space = ctk.CTkFrame(lat_and_long_space, fg_color='transparent')
        lat_space.pack(expand=True, side='left', padx=5)
        
        long_space = ctk.CTkFrame(lat_and_long_space, fg_color='transparent')
        long_space.pack(expand=True, side='right', padx=5)
        
        description_latitude = ctk.CTkLabel(lat_space, text="Put here a latitude:")
        description_latitude.pack(padx=5, expand=True)
        
        description_longitude = ctk.CTkLabel(long_space, text="Put here a longitude:")
        description_longitude.pack(padx=5, expand=True)
        
        latitude = ctk.CTkEntry(
            lat_space, validate="key", validatecommand=validate
        )
        latitude.pack(expand=True)
        
        longitude = ctk.CTkEntry(
            long_space, validate="key", validatecommand=validate
        )
        longitude.pack(expand=True)
        
        enter_button = ctk.CTkButton(
            container,
            text="ENTER",
            compound = "left",                  # Define the position
            font = ("Arial", 25, "bold"),   # Configure font here
            text_color = "#000000",             # Text title color
            command=lambda:
                self.__inset_value(out_container, map, latitude, longitude, out)
        )
        enter_button.pack(expand=True, pady=(10, 15))
    # END
    
    
    # <--------------->
    #     FOOTER
    # <--------------->
    
    
    def __footer(self, window, frame):
        footer = ctk.CTkFrame(frame)
        footer.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.__signature(footer)
        self.__exit_button(window, footer)
    # END
    
    
    def __open_github(self, event) -> None:
        webbrowser.open('https://github.com/DoctorSolo')
    
    
    def __signature(self, container: ctk.CTkFrame) -> None:
        signature = ctk.CTkLabel(
            container,
            text=f'Autor: @DoctorSolo',
            font=('Arial',12,'italic','underline'),
            text_color='#04C4FF',
            cursor='hand2'
        )
        signature.bind("<Button-1>", self.__open_github)
        signature.pack(side='right', padx=30, pady=15)
        
    
    def __exit_button(self, window: ctk.CTk, frame: ctk.CTkFrame) -> None:
        exit_button = ctk.CTkButton(frame,
                                     text="Exit",
                                     font=("Arial", 25, "bold"),
                                     text_color="#000000",
                                     command=window.destroy,
                                     #fg_color="#431580"
                                     )
        exit_button.pack(side='left', padx=30, pady=15)