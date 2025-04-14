def exibir_msg():
    print("Olá mundo")

def exibir_msg_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_msg_3(nome= "Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_msg()
exibir_msg_2(nome="Gui")
exibir_msg_3()
exibir_msg_3(nome="Chappie")