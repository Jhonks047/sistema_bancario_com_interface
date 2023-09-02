from tkinter import *
#Configurações da Janela principal
janela = Tk()
janela.title("Testando janelas")
janela.geometry("600x300")
janela.config(bg="#5294ff")
janela.iconphoto(False, PhotoImage(file="nox_logo21.png"))
janela.resizable(width=False, height=False)

#Label
ola = Label(janela, width=60, text="ÁREA", font=("Calibri 15 bold"), fg="#9a36ff", bg="#c891ff")
welcome = Label(janela, width=20, text="Seja muito bem vindo!", font=("Arial 12"), fg="#cffff2", bg="#009e67")

#Grid
ola.grid(row=0, column=0)
welcome.grid(row=1, column=0, pady=10)

janela.mainloop()