import tkinter as tk
from tkinter import *
from tkintermapview import TkinterMapView
from src.Local import Local


class InterfaceGrafica:

    def __init__(self) -> None:
        pass

    def validade_numero(self, P):
        if P == "" or P == "-":
            return True
        try:
            float(P)
            return True
        except ValueError:
            return False

    def Interface(self):
        janela = Tk()
        janela.title("Buscar Localização")

        validade = (janela.register(self.validade_numero), "%P")

        titulo = Label(
            janela, text="Digite em baixo o valor das coordenadas", pady=10
        )
        titulo.grid(column=0, row=0, columnspan=2)

        try:
            img = PhotoImage(file="imagens/lupa.png")
            imagem_dec = Label(janela, image=img)
            imagem_dec.image = img
            imagem_dec.grid(column=2, row=0, rowspan=3, padx=10, pady=10)
        except Exception:
            pass

        txt_latitude = Label(janela, text="Informe aqui o valor da latitude: ")
        txt_latitude.grid(column=0, row=1)

        entrada_latitude = Entry(
            janela, validate="key", validatecommand=validade
        )
        entrada_latitude.grid(column=1, row=1, pady=10, padx=30)

        txt_longitude = Label(janela, text="Informe aqui o valor da longitude: ")
        txt_longitude.grid(column=0, row=2)

        entrada_longitude = Entry(
            janela, validate="key", validatecommand=validade
        )
        entrada_longitude.grid(column=1, row=2, pady=10)

        saida = Label(janela, text="")
        saida.grid(column=0, row=5, columnspan=3, padx=10, pady=10)

        # Substituição do HtmlFrame pelo TkinterMapView
        map_widget = TkinterMapView(janela, width=600, height=400, corner_radius=0)
        map_widget.grid(column=0, row=6, columnspan=3, padx=10, pady=10)
        
        # Posição inicial padrão (ex: Brasil)
        map_widget.set_position(-14.2350, -51.9253)
        map_widget.set_zoom(4)

        def insere_valor():
            if not entrada_latitude.get() or not entrada_longitude.get():
                saida["text"] = "Preencha ambos os campos!"
                return

            lat = float(entrada_latitude.get())
            long = float(entrada_longitude.get())
            local0 = Local(lat, long)
            local0.mapa()

            # Atualiza o centro do mapa e adiciona um marcador
            map_widget.set_position(lat, long)
            map_widget.set_zoom(15)
            map_widget.set_marker(lat, long, text="Local Encontrado")

            saida["text"] = local0.pesquisa()

        enter = Button(janela, text="ENTER", command=insere_valor)
        enter.grid(column=0, row=4, columnspan=2, pady=10)

        janela.mainloop()