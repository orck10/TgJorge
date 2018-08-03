from urllib.parse import *
from urllib.request import *

class PostResultado:

    def __init__(self, bodyRequest, usuario, senha):

        self.data = bodyRequest
        self.data = self.data.encode('ascii')

        self.headers = {'Content-Type':'application/json','nomeUsuario':usuario,'senha':senha}
        self.url = "http://localhost:8080/FrontTg/PersistirTestes.action"

        self.request = Request(self.url, self.data, self.headers)
        self.js = urlopen(self.request).read().decode()
        return self.js
        
        
