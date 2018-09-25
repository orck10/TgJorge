import json
from urllib.parse import *
from urllib.request import *

from recursos import *

class PostResultado:

    def __init__(self, bodyRequest, usuario, senha):
        recursos = Recursos()
        
        self.data = bodyRequest
        self.data = self.data.encode('UTF-8')

        self.headers = {'Content-Type':'application/json','nomeUsuario':usuario,'senha':senha}
        self.url = recursos.uri()+"/PersistirTestes.action"

        self.request = Request(self.url, self.data, self.headers)
        self.js = urlopen(self.request).read().decode()
        self.dic = json.loads(self.js)
        print(self.dic['error'])
        
        
    def postar(self): 
        return self.dic
