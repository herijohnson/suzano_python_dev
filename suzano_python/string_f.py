nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("nome: {1} idade: {0}".format(idade, nome))

print("nome: {nome}, idade: {idade}".format(nome = nome, idade = idade))

print("nome: {nome}, idade: {idade}".format(**dados))

print(f"nome:  {nome} idade: {idade} saldo: {saldo:.2f}")