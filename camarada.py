import json
from keyword import issoftkeyword

class Camarada():
    def __init__(self):
        try:
            banco_de_dados = open("memoria.json", 'r')
        except:    
            banco_de_dados = open('memoria.json', 'w')
            banco_de_dados.write('''{"Olá": "Adeus",
            "Adeus": "Nunca mais volte!"}''')
            #banco_de_dados.close()
            banco_de_dados = open("memoria.json", 'r')
        self.memoria = json.load(banco_de_dados)

    def pega_frases(self, frase=None):
        return frase

    def processa_dados(self, dados):
        if dados in self.memoria:
            return self.memoria[dados]
        else:
            return 'Não entendi'

#Camarada()
