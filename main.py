# QUESTAO DONA MONICA OLIMPIADA

# while True:
#     M = int(input())
#     A = int(input())
#     B = int(input())
#
#     if (40 <= M <= 110 and 1 <= A < M and 1 <= B < M and A != B):
#
#         C = M - (A + B)
#
#         maior_AB = int((A + B + abs(A - B)) / 2)
#         maior_dos_tres = int((maior_AB + C + abs(maior_AB - C)) / 2)
#         print(maior_dos_tres)
#         break
#
#     else:
#         continue


# QUESTAO 1020 BEECROWD
# while True:
#   N = float(input())
#   if(0 <= N <= 1000000.00):
#     nota_cem = int(N/100)
#     notas_cinquenta = int((N % 100)/50)
#     notas_vinte = int(((N % 100) % 50) / 20)
#     notas_dez = int((((N % 100) % 50) % 20) / 10)
#     notas_cinco = int(((((N % 100) % 50) % 20) % 10) / 5)
#     notas_dois = int((((((N % 100) % 50) % 20) % 10) % 5) / 2)
#
#     centavos = round(N - int(N), 2)
#
#     moedas_um = int((((((N % 100) % 50) % 20) % 10) % 5) % 2)
#     moedas_cinquenta = int(centavos / 0.50)
#     moedas_vinte_cinco = int(round((centavos % 0.50), 2) / 0.25)
#     moedas_dez = int((round((centavos % 0.50), 2) % 0.25) / 0.10)
#     moedas_cinco = int(((round((centavos % 0.50), 2) % 0.25) % 0.10) / 0.05)
#     moedas_um_cen = int(round((((((centavos % 0.50) % 0.25) % 0.10) % 0.05) / 0.01), 0))
#     break
#
#   continue
#
#
# print("NOTAS:")
# print("{} nota(s) de R$ 100.00".format(nota_cem))
#
# print("{} nota(s) de R$ 50.00".format(notas_cinquenta))
#
# print("{} nota(s) de R$ 20.00".format(notas_vinte))
#
# print("{} nota(s) de R$ 10.00".format(notas_dez))
#
# print("{} nota(s) de R$ 5.00".format(notas_cinco))
#
# print("{} nota(s) de R$ 2.00".format(notas_dois))
#
#
# print("MOEDAS:")
# print("{} moeda(s) de R$ 1.00".format(moedas_um))
#
# print("{} moeda(s) de R$ 0.50".format(moedas_cinquenta))
#
# print("{} moeda(s) de R$ 0.25".format(moedas_vinte_cinco))
#
# print("{} moeda(s) de R$ 0.10".format(moedas_dez))
#
# print("{} moeda(s) de R$ 0.05".format(moedas_cinco))
#
# print("{} moeda(s) de R$ 0.01".format(moedas_um_cen))
#
# print (centavos)


# numeros = input("Digite os números separados por espaço: ").split()
# lista_numeros = [int(numero) for numero in numeros]
# print(lista_numeros)
#
# numeros = input("Digite os números separados por espaço: ").split()
# lista_numeros = list(map(int, numeros))
# print(lista_numeros)


# QUESTAO SOMA OLIMPIADA/3051 BEECROWD - NAO DEU CERTO

#
# while True:
#     valor = input().split()
#     n = int(valor[0])
#     k = int(valor[1])
#     if (1 <= n and n <= 500000) and (0 <= k and k <= 1000000):
#         break
#     else:
#         continue
#
# numeros = input().split()
# lista_numeros = list(map(int, numeros))
#
# soma = 0
# aux = 0
#
# for j in range(0, len(lista_numeros)):
#     for i in range(j, len(lista_numeros)):
#         soma = soma + lista_numeros[i]
#         if (soma == k):
#             aux += 1
#         if (soma > k):
#             break
#     soma = 0
#
# print(aux)



# calcada imperial
# n = int(input())
# lista = []
#
# for i in range (n):
#     numero = int(input())
#     lista.append(numero)
#
# print(lista)
#
#
# aux = 0
# aux2 = len(lista)
#
# for i in range (0, aux2, +1):
#     if (lista[i] == n):
#         aux += 1
#         i += 1
#         print("cheguei aqui")
#
#     else:
#         for j in range (i+2, aux2-2):
#             if (lista[i] + lista[j] == n):
#                 print("cheguei aquiiiii")
#                 aux += 2
#                 i += 1
#                 lista.pop(j)
#                 lista.pop(j)
#                 aux2 = len(lista)
#                 break
#
# print(aux)


# 1047 BEECROWD - NAO CONSEGUI RESOLVER (DA CERTO MAS A PLATAFORMA NAO ACEITA)
# valores = input().split()
#
# inicio_hora = int(valores[0])
# inicio_minuto = int(valores[1])
# termino_hora = int(valores[2])
# termino_minuto = int(valores[3])
#
#
# def calcular_hora(inicio_hora, termino_hora):
#     if (inicio_hora == termino_hora):
#         duracao_horas = 24
#     elif (termino_hora < inicio_hora ):
#         duracao_horas = (24 - inicio_hora ) + termino_hora
#     else:
#         duracao_horas = termino_hora - inicio_hora
#     return duracao_horas
#
#
# if (inicio_hora == termino_hora and inicio_minuto == termino_minuto):
#     duracao_horas = 24
#     duracao_minuto = 0
#
# elif (inicio_minuto == termino_minuto and inicio_hora != termino_hora):
#     duracao_minuto = 0
#
#     duracao_horas = calcular_hora(inicio_hora, termino_hora)
#
# elif (inicio_minuto < termino_minuto and termino_hora > inicio_hora):
#     duracao_minuto = termino_minuto - inicio_minuto
#     duracao_horas = calcular_hora(inicio_hora, termino_hora)
#
# elif (inicio_minuto < termino_minuto and termino_hora < inicio_hora):
#     duracao_minuto = 60 - (termino_minuto - inicio_minuto)
#     duracao_horas = calcular_hora(inicio_hora, termino_hora)
#
# else:
#     duracao_minuto = (60 - inicio_minuto) + termino_minuto
#     duracao_horas = calcular_hora(inicio_hora, termino_hora)
#     duracao_horas -= 1
#
#
#
# print ("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(duracao_horas, duracao_minuto))

#1101




# k = 0
# while True:
#     if k == 1:
#         break
#
#     soma = 0
#     j = 0
#     while True:
#         nota = float(input())
#
#         if nota < 0 or nota > 10:
#             print("nota invalida")
#         else:
#             soma += nota
#             j += 1
#             if j == 2:
#                 break
#     print("media = {:.2f}".format(soma/2))
#
#
#     while True:
#         condicao = int(input("novo calculo? (1-sim 2-nao)"))
#
#         if condicao != 1 and condicao != 2:
#             continue
#         else:
#             if condicao == 1:
#                 break
#             else:
#                 k = 1
#                 break




#1131 beecrowd nao aceita
# a posical 0 do vetor abaixo indica quantos grenais tiveram.
# lista = [0, "Inter:", 0, "Gremio:", 0, "Empates:", 0,]
#
# while True:
#     i, g = input().split()
#     i = int(i)
#     g = int(g)
#
#     lista[0] += 1
#
#     if i > g:
#         lista[2] += 1
#     elif g > i:
#         lista[4] += 1
#     else:
#         lista[6] += 1
#
#     opcao = input("Novo grenal (1-sim 2-nao)")
#
#     if opcao == "1":
#         continue
#     else:
#         break
#
#
# print("{} grenais".format(lista[0]))
# print("{}{}".format(lista[1], lista[2]))
# print("{}{}".format(lista[3], lista[4]))
# print("{}{}".format(lista[5], lista[6]))
#
# if lista[2] > lista[4]:
#     print("Inter venceu mais")
# elif lista[2] < lista[4]:
#     print("Gremio venceu mais")
# else:
#     print("Nao houve vencedor")







#Metodo de ordenacao BUBLE SORT
# lista = [int (i) for i in input().split()]
# n = len(lista)
#
# for i in range (n):
#     for j in range (n-1):
#         if lista[j] > lista[j+1]:
#             aux = lista[j]
#             lista[j] = lista[j+1]
#             lista[j + 1] = aux
#     n -= 1
#
# print(lista)


#SELECTION SORT


# lista = [int(i) for i in input().split()]
#
# n = len(lista)
#
# for i in range(n-1):
#     indice = i
#
#     for j in range(i + 1, n):
#         if lista[indice] > lista[j]:
#             indice = j
#
#     lista[i], lista[indice] = lista[indice], lista[i]
#
# print(lista)




#INSERT SORT
# lista = [int(i) for i in input().split()]
#
#
# for i in range(1, len(lista)):
#     elemento = lista[i]
#     j = i - 1
#
#     while elemento < lista[j] and j >= 0:
#         lista[j+1] = lista[j]
#         j -= 1
#
#     lista[j+1] = elemento
#
# print(lista)aaaaaaaaaaaa
print ("ola")




def insert_sort(lista):
    for i in range(1, len(lista)):
        j = i - 1

        while lista[j+1] < lista[j] and j >= 0:
            lista[j+1], lista[j] = lista[j], lista[j+1]
            j -= 1

    return lista


lista = [int(i) for i in input().split()]

print(lista)
print("ola")