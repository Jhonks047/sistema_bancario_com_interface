from tkinter import *
#Configurações da Janela principal
janela = Tk()
janela.title("Testando janelas")
janela.geometry("900x600")
janela.config(bg="#bbfaef")
janela.iconphoto(False, PhotoImage(file="nox_logo21.png"))
janela.resizable(width=False, height=False)

contador = 0
def message():
    global contador
    if (contador % 2) == 0:
        contador_text["text"] = f"Número par: {contador}"
        contador_text["fg"] = "#005eff"
    else:
        contador_text["text"] = f"Número ímpar: {contador}"
        contador_text["fg"] = "#ff1500"
    contador += 1
    
    
def obter():
    nome = entrada.get()
    name_digitado["text"] = nome
    
    entrada.delete(0,END)
    
    pass



#Label
ola = Label(janela, width=90, text="ÁREA DE LOGIN", font=("Calibri 15 bold"), fg="#9a36ff", bg="#c891ff")
welcome = Label(janela, width=90, height=2, text="Seja muito bem vindo ao sistema bancário NSX", font=("Arial 12 bold"), fg="#cffff2", bg="#009e67")
contador_text = Label(janela, width=20, height=2, text="Apenas testando!", fg="#d454ff", bg="#430059")
name = Label(janela, width=10, text="Nome:")
name_digitado = Label(janela, text="INDEFINIDO")

#Button
botao = Button(janela, command=message, width=10, height=2, text="CLIQUE AQUI", relief="groove", fg="#04ff00", bg="#044003")
atualizar = Button(janela, command=obter, width=20, height=2, text="Atualizar Label", relief="groove", fg="#04ff00", bg="#044003")

#Entry
entrada = Entry(janela, width=10, )


#Place
ola.pack()
welcome.pack()
botao.place(x=40, y=90)
atualizar.place(x=40, y=160)
contador_text.place(x=120, y=90)
name.place(x=40, y=130)
entrada.place(x=120, y=130)
name_digitado.place(x=200, y=130)


janela.mainloop()