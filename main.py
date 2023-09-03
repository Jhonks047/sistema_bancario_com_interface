from tkinter import *

#Configurações da Janela principal
janela_principal = Tk()
janela_principal.title("Sistema bancário NSX")
janela_principal.geometry("900x600")
janela_principal.config(bg="#bbfaef")
janela_principal.iconphoto(False, PhotoImage(file="nox_logo21.png"))
janela_principal.resizable(width=False, height=False)

def menu_principal():
    global top
    top = Label(janela_principal, width=90, height=2, text="Seja muito bem vindo ao sistema bancário NSX", font=("Arial 12 bold"), fg="#cffff2", bg="#009e67")
    deposit_button = Button(janela_principal, command=deposito, width=90, height=2, text="DEPÓSITO", font="Calibri 12 bold", relief="groove", fg="#04ff00", bg="#044003")
    top.place(x=0, y=0)
    deposit_button.place(x=0, y=180)


#Configurar tela de depósito
def deposito():
    top["text"] = "Área de Depósito"
    top["font"] = "Calibri 12 bold"
    top["fg"] = "#32ff00"
    top["bg"] = "#0e4700"
    top.place(x=0, y=0)
    voltar_button = Button(janela_principal, command=menu_principal, width=10, height=3, text="Voltar", relief="groove", fg="#ffffff", bg="#690000")
    voltar_button.place(x=0, y=544)


#   Janela Looping
menu_principal()
janela_principal.mainloop()
