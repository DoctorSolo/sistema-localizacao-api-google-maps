<h1 align=center>Geocode Aplication</h1>

This code returns a geographic location to the user based on a provided coordinate. Users can utilize it to check nearby commercial locations, tourist attractions, and routes.

##

<h3 align=center>Pré-Requisitos</h3>

É necessário que instale as seguintes bibliotecas:

- `tkinter`
- `pywebview`
- `geopy`
- `folium`

Recomendo digitar o seguinte comando para instalar todas as dependencias:

```
pip install -r requeriments.txt
```

Também é importante que o python tenha no mínimo a versão 3.x.

##

<h3 align=center>Instalação</h3>

Caso tenha o git instalado então use esse comando em seu terminal de preferencia para clonar meu projeto.

```
git clone https://github.com/DoutorSolo/projeto-de-localizacao.git
```

##

<h3 align=center>Usos</h3>

Este projeto tem duas opções de uso, se for do seu interesse usar uma interface então nevege até `aplicacao.py` que é onde ela sera executada, o user precisara informar duas informações, a latitude e longitude, depois de informar clique em `enter` e sera informada na janela princial informações do local, além disso uma outra janela sera criada com o mapa da região.
A outra opção é a sem interface gráfica, nevegue até `AplicacaoSemInterface.py`, o user precisara informar uma unica linha com a cordenada separa por virgula, por exemplo: `48.858844, 2.294351`. Ao digitar nesse formato o terminal vai informar qual estruturas estão localizadas nesse ponto.

##

<h3 align=center>Principais Metodos e Funções</h3>

Este codigo possui alguns metodos mais relevantes para o projeto como a função `def pesquisa(self):` que retorna as informações da cordenada como estruturas, rua, numero, cep. Outra função importante é `def map(self): que gera o mapa da região.
Estas duas funções são o esqueleto do projeto, a recomendação é não mudar.

##

<h3 align=center>Exemplos de Uso</h3>

Supondo que a cordenada escolhida seje `48.858844, 2.294351`, a saída vai ser `Tour Eiffel, 5, Avenue Anatole France, Quartier du Gros-Caillou, Paris 7e Arrondissement, Paris, Île-de-France, France métropolitaine, 75007, France`.
