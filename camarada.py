import json

class Camarada():
    def __init__(self):
        try:
            with open("memoria.json", 'r') as mj:
                self.memory = json.load(mj)
        except:    
            with open('memoria.json', 'w', encoding="utf8") as mj:
                dici = {"Olá": "Adeus",
                "Adeus": "Nunca mais volte!"}
                json.dump(dici, mj, indent=2, ensure_ascii=False)
            with open("memoria.json", 'r') as mj:
                self.memory = json.load(mj)


Camarada()