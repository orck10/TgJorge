from tkinter import *
from functools import partial
import json

class TelaDeSelecao:
    def __init__(self,json):
        super(TelaDeSelecao, self).__init__()

        self.root = Tk()
        self.root.title("Tela de Seleção")
        self.root.geometry("400x300")
        
        self.json = json
        self.botoes = []

        self.espacao = Label(self.root)
        
        self.espacao.pack()
        for x in json:
            nome = x['nome']
            botao = Button(self.root, width = 20, text=nome)
            botao["command"] = partial(self.onClick, nome)
            self.botoes.append(botao)
            
        
        for b in self.botoes:
            b.pack()


    def abrirTela(self):
        self.retorno = ""
        self.root.mainloop()
        return self.retorno

    def fecharJanela(self):
        self.root.destroy()

    def onClick(self, nome):
        self.retorno = nome
        self.fecharJanela()
        
