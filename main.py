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
    
    # Atualizar a imagem apenas quando necessário
    if result == 'Coroa':
        imagem_label.configure(image=coroa)
        imagem_label.image = coroa
    else:
        imagem_label.configure(image=cara)
        imagem_label.image = cara

root = tk.Tk()

root.minsize(200, 160)

# Criar um botão
botao = tk.Button(root, text="RODAR", command=caraOuCoroa)
botao.pack()

mensagem_var = tk.StringVar()

# Rótulo para exibir a mensagem
rotulo_mensagem = tk.Label(root, textvariable=mensagem_var)
rotulo_mensagem.pack()

# Carregar uma imagem padrão ou vazia
imagem_vazia = PhotoImage()  # imagem vazia
imagem_label = tk.Label(root, image=imagem_vazia)
imagem_label.image = imagem_vazia
imagem_label.pack()

# Carregar a imagem
coroa = PhotoImage(file=pasta + "\\coroa.png")
cara = PhotoImage(file=pasta + "\\cara.png")

# Iniciar o loop principal
root.mainloop()