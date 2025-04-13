salario = 2000

def salario_bonus(bonus):
    global salario

    lista_aux=lista.copy()
    lista_aux.append(2)
    print(f"lista aux = {lista_aux}")

    salario += bonus

    return salario

salario_com_bonus= salario_bonus(500)

print(salario_com_bonus)