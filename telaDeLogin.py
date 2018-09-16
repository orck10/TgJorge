import json
from tkinter import *
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from recursos import *

class TelaDeLogin:
    
    def __init__(self, parent,master=None):
        super (TelaDeLogin, self).__init__()
        
        self.parent = parent

        self.parent.title("Tela de Login")
        self.parent.geometry("400x300")
        
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
  
        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)
  
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()
  
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def abrirTela(self):
        self.retorno = ""
        self.parent.mainloop()   
        return self.retorno
        
        
    def fecharJanela(self):
        self.parent.destroy()
    
    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()

        recursos = Recursos()
        
        url = recursos.uri()+'/AtualicarApp.action'
        post_fields = {'nomeUsuario': usuario, 'senha': senha}     

        request = Request(url, urlencode(post_fields).encode())
        js = urlopen(request).read().decode()

        dic = json.loads(js)
        print(dic['error'])

        

        if dic['error'] == "true":
            self.mensagem["text"] = dic['type']
        else:
            self.retorno = dic
            self.fecharJanela()
=======
import json
from tkinter import *
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from recursos import *

class TelaDeLogin:
    
    def __init__(self, parent,master=None):
        super (TelaDeLogin, self).__init__()
        
        self.parent = parent

        self.parent.title("Tela de Login")
        self.parent.geometry("400x300")
        
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
  
        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)
  
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()
  
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def abrirTela(self):
        self.retorno = ""
        self.parent.mainloop()   
        return self.retorno
        
        
    def fecharJanela(self):
        self.parent.destroy()
    
    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()

        recursos = Recursos()
        
        url = recursos.uri()+'/AtualicarApp.action'
        post_fields = {'nomeUsuario': usuario, 'senha': senha}     

        request = Request(url, urlencode(post_fields).encode())
        js = urlopen(request).read().decode()

        dic = json.loads(js)
        print(dic['error'])

        

        if dic['error'] == "true":
            self.mensagem["text"] = dic['type']
        else:
            self.retorno = dic
            self.fecharJanela()
