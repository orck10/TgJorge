#appVersao1.1-Está versão foi retirada as classes BolaVerde, BolaVermelha e BolaRoxa,
#que foram substituidas pela classe Bola que agora recebe como parametro
#uma string com o nome da cor
#Quase terminado

import json
import time
import pygame, sys

from pygame.locals import *

from tkinter import *
from urllib.parse import urlencode
from urllib.request import Request, urlopen


from torre import *
from fases import *
from telaDeMudanca import *
from telaDeLogin import *
from selecaoDeCrianca import *
from telaDeVerificacao import *
from postResultados import *

def main():
    #fazer login
    root = Tk()
    
    usuario = TelaDeLogin(root)
    try:
        prof = usuario.abrirTela()
        jsonC = prof['criancas']
        print(prof)
    except:
        return False
    
    while True:
        crianca = TelaDeSelecao(jsonC).abrirTela()
        if(crianca == ""):
            print("sair")
            break

        #verificar se é essa criaça mesmo que vai fazer o teste
        fazer = TelaDeVerificacao(crianca).abrirTela()
        if fazer==True:
            #cria lista de resultados
            resultados = []

            #chama a classe fases
            f = Fases()
            #seta as estradas referentes a fase
            b1, b2, b3, m, i, fase = f.faseExemplo()

            #seta as tentativa igual a zero
            tentativas = 0
            #variavel para saber se resultado da fase foi positivo
            x = 0

            #variavel que chama a tela do jogo, recebe os parametro da fase
            tela = Tela(fase)
            e = Torre(b1, b2, b3, m, i, fase)
            #a fase roda enquanto o jogador não consegue resultsdo positivo ou o numero
            #de tentativas for menor que 3
            while (x < 1) and (tentativas < 3) :
                tela.telaDeMudanca()
                x = e.jogoTorre()
                tentativas += 1

            #adiciona a lista de resultados o resultado obtido na fase de teste
            #em forma de tupla
            
            #Fase1
            b1, b2, b3, m, i, fase= f.fase1()

            tentativas = 0
            x = 0

            tela = Tela(fase)
            e = Torre(b1, b2, b3, m, i, fase)
            while (x < 1) and (tentativas < 3) :
                tela.telaDeMudanca()
                x = e.jogoTorre()
                tentativas += 1

            #adiciona a lista de resultados o resultado obtido na fase de teste
            #em forma de tupla    
            resultados.append((tentativas, x))

            #fase2
            b1, b2, b3, m, i, fase= f.fase2()

            tentativas = 0
            x = 0

            tela = Tela(fase)
            e = Torre(b1, b2, b3, m, i, fase)
            while (x < 1) and (tentativas < 3) :
                tela.telaDeMudanca()
                x = e.jogoTorre()
                tentativas += 1
                
            resultados.append((tentativas, x))

            #fase3
            b1, b2, b3, m, i, fase= f.fase3()

            tentativas = 0
            x = 0

            tela = Tela(fase)
            e = Torre(b1, b2, b3, m, i, fase)
            while (x < 1) and (tentativas < 3) :
                tela.telaDeMudanca()
                x = e.jogoTorre()
                tentativas += 1
                
            resultados.append((tentativas, x))

            #fase4
            b1, b2, b3, m, i, fase= f.fase4()

            tela = Tela(fase)
            tentativas = 0
            x = 0

            e = Torre(b1, b2, b3, m, i, fase)
            while (x < 1) and (tentativas < 3) :
                tela.telaDeMudanca()
                x = e.jogoTorre()
                tentativas += 1
                
            resultados.append((tentativas, x))

            #fase5
            b1, b2, b3, m, i, fase= f.fase5()

            tentativas = 0
            x = 0

            tela = Tela(fase)
            e = Torre(b1, b2, b3, m, i, fase)
            while (x < 1) and (tentativas < 3) :
                tela.telaDeMudanca()
                x = e.jogoTorre()
                tentativas += 1
                
            resultados.append((tentativas, x))

            #fase6
            b1, b2, b3, m, i, fase= f.fase6()

            tentativas = 0
            x = 0

            tela = Tela(fase)
            e = Torre(b1, b2, b3, m, i, fase)
            while (x < 1) and (tentativas < 3) :
                tela.telaDeMudanca()
                x = e.jogoTorre()
                tentativas += 1
                
            resultados.append((tentativas, x))

            #fase7
            b1, b2, b3, m, i, fase= f.fase7()

            tentativas = 0
            x = 0

            tela = Tela(fase)
            e = Torre(b1, b2, b3, m, i, fase)
            while (x < 1) and (tentativas < 3) :
                tela.telaDeMudanca()
                x = e.jogoTorre()
                tentativas += 1
                
            resultados.append((tentativas, x))

            #fase8
            b1, b2, b3, m, i, fase= f.fase8()

            tentativas = 0
            x = 0

            tela = Tela(fase)
            e = Torre(b1, b2, b3, m, i, fase)
            while (x < 1) and (tentativas < 3) :
                tela.telaDeMudanca()
                x = e.jogoTorre()
                tentativas += 1
                
            resultados.append((tentativas, x))

            #fase9
            b1, b2, b3, m, i, fase= f.fase9()

            tentativas = 0
            x = 0

            tela = Tela(fase)
            e = Torre(b1, b2, b3, m, i, fase)
            while (x < 1) and (tentativas < 3) :
                tela.telaDeMudanca()
                x = e.jogoTorre()
                tentativas += 1
                
            resultados.append((tentativas, x))

            #fase10
            b1, b2, b3, m, i, fase= f.fase10()

            tentativas = 0
            x = 0

            tela = Tela(fase)
            e = Torre(b1, b2, b3, m, i, fase)
            while (x < 1) and (tentativas < 3) :
                tela.telaDeMudanca()
                x = e.jogoTorre()
                tentativas += 1
                
            resultados.append((tentativas, x))

            #fase11
            b1, b2, b3, m, i, fase= f.fase11()

            tela = Tela(fase)
            tentativas = 0
            x = 0

            e = Torre(b1, b2, b3, m, i, fase)
            while (x < 1) and (tentativas < 3) :
                tela.telaDeMudanca()
                x = e.jogoTorre()
                tentativas += 1
                
            resultados.append((tentativas, x))
            
            #fase12
            b1, b2, b3, m, i, fase= f.fase12()

            tentativas = 0
            x = 0

            tela = Tela(fase)
            e = Torre(b1, b2, b3, m, i, fase)
            while (x < 1) and (tentativas < 3) :
                tela.telaDeMudanca()
                x = e.jogoTorre()
                tentativas += 1
                
            resultados.append((tentativas, x))

            #motrar tela de aviso antes de fechar
            fase = f.telaDeFechamento()
            tela = Tela(fase)
            tela.telaDeMudanca()

            #fecha a tela do jogo e dpois printa a tabela de resultados
            e.sair()
            print (json.dumps(resultados))
            print (prof['usuario']['nome'],prof['usuario']['senha'])
            data = int(round(time.time() * 1000))
            respostaJson = "{\"cricanca\" : \""+crianca+"\",\"resultados\":"+json.dumps(resultados)+", \"data\":"+str(data)+"}"
            print (respostaJson)

            print(PostResultado(respostaJson,prof['usuario']['nome'],prof['usuario']['senha']).postar())

            while(PostResultado(respostaJson,prof['usuario']['nome'],prof['usuario']['senha']).postar()['error']=='true'):
                print("Falhou")
            
            main()
            break
            
        elif fazer == None:
            print("Fechar")
            break
        else:
            print("Voltar")
main()
