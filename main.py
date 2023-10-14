import random
import tkinter as tk
import os
from tkinter import PhotoImage, messagebox

pasta = os.path.dirname(__file__)
result = None

def caraOuCoroa():
    global result
    x = random.randint(1, 2)
    if x == 1:
        result = 'Cara'
        mensagem_var.set("Cara")
    else:
        result = 'Coroa'
        mensagem_var.set("Coroa")
    
    # atualiza a imagem
    if result == 'Coroa':
        imagem_label.configure(image=coroa)
        imagem_label.image = coroa
    else:
        imagem_label.configure(image=cara)
        imagem_label.image = cara

janela = tk.Tk()

janela.minsize(200, 160)

# cria um botao
botao = tk.Button(janela, text="RODAR", command=caraOuCoroa)
botao.pack()

mensagem_var = tk.StringVar()

# exibe uma mensagem de resultado
resultado = tk.Label(janela, textvariable=mensagem_var)
resultado.pack()

# carrega uma imagem padrao
imagem_vazia = PhotoImage()  
imagem_label = tk.Label(janela, image=imagem_vazia)
imagem_label.image = imagem_vazia
imagem_label.pack()

# local da imagem
coroa = PhotoImage(file=os.path.join(pasta, "coroa.png"))
cara = PhotoImage(file=os.path.join(pasta, "cara.png"))

# loop
janela.mainloop()