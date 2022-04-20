#importa o App, Builder (GUI)
#Cria o nosso aplicativo
#Cria a função build

from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI

    def on_start(self):
        self.root.ids["Moeda1"].text = f"Dólar R${self.pegar_cotacao('USD')}"
        self.root.ids["Moeda2"].text = f"Euro R${self.pegar_cotacao('EUR')}"
        self.root.ids["Moeda3"].text = f"Biticoin R${self.pegar_cotacao('BTC')}"
        self.root.ids["Moeda4"].text = f"Ethereum R${self.pegar_cotacao('ETH')}"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao


MeuAplicativo().run()
