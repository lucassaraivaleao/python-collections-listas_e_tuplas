# idades = [39, 30, 27, 18]
# idades.extend([27, 19])

# print(idades)

# # antigamente_fazíamos assim:

# idades_no_ano_que_vem = []
# for idade in idades:
#     idades_no_ano_que_vem.append(idade+1)
# print(idades_no_ano_que_vem)

# print()
# # Agora...
# idades = [39, 30, 27, 18]
# idades.extend([27, 19])

# print(idades)

# idades_no_ano_que_vem = [(idade+1) for idade in idades]
# print(idades_no_ano_que_vem)

# # verificando idades > que 21
# idades_maior_que_21 = [(idade) for idade in idades if idade > 21]
# print(idades_maior_que_21)

# # utilizando funções

# def proximo_ano(idade):
#     return idade+1
# idades_maior_que_21 = [proximo_ano(idade) for idade in idades if idade > 21]
# print(idades_maior_que_21)

# Problemas mutabilidade de listas
def faz_processamento_de_visualizacao(lista = None):
    if lista == None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
