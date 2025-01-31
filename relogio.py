from tkinter import *
import tkinter
from datetime import datetime

#cores#

cor1 = "#1C1C1C"  # preta
cor2 = "#FFFAFA"  # branca
cor3 = "#228B22"  # verde
cor4 = "#eb463b"  # vermelho
cor5 = "#008080"  # ciano
cor6 = "#3080f0"  # azul  

fundo = cor1
cor = cor2

janela = Tk()
janela.title("Relogio")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)


def relogio():
    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S") 
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")
    
    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + " " + str(dia) + " / " + str(mes) + " / " + str(ano))

            
l1 = Label(janela, text="",font=("Arial 80"), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, text="",font=("Arial 20"), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)



relogio()
janela.mainloop()

