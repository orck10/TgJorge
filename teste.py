from tkinter import *

x = 0

root = Tk()

root.title("Tela de Login")
root.geometry("400x300")

botoes = []

while x < 5:
    botao = Button(root, width = 20, text=(x+1))
    botoes.append(botao)
    x = x+1

x = 0

while x < 5:
    botoes[x].pack()
    x = x+1

root.mainloop()
