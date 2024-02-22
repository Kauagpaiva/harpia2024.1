def primo(numero): #Verifica se um número é primo
    resultado = True
    for x in range(2,numero):
        if numero%x == 0:
            resultado = False
    if numero < 2:
        resultado = False
    return resultado

#1- Faça um programa que diga se o primeiro e o último ítens de uma lista são iguais(deve funcionar para qualquer lista, ou seja, a quantidade de ítens não é fixa)
def comparar(lista): 
    if lista[0] == lista[-1]: return True

#2- Faça um programa que diga o maior divisor primo de um número dado como input
def divisor(numero):
    resultado = 1
    for valor in range(numero):
        if primo(valor):
            if numero%valor == 0:
                resultado = valor
    return resultado

#3- Diga se um número qualquer é um palíndromo
def palindromo(numero):
    if str(numero)[::-1] == str(numero):
        return True
    return False

#4- Dê a soma de todos os números primos menores que 1000
def somaPrimos():
    resultado = 0
    for numero in range(2,1001):
        if primo(numero):
            resultado += numero
    return resultado

#Implemente um modelo que descreva drones
#Requerimentos
#Deve conter os atributos: número de motores, quantidade de câmeras, ano de
#construção, nome do veículo, e no mínimo, mais 1 atributo de livre escolha
#Deve conter métodos para:
#◦ Exibir todos os drones em tabela
#◦ Exibir os drones individulmente
#◦ Rankear os robôs do mais novo para o mais antigo
#Deve conter outro método de livre escolha

class Drone:
    def __init__(self, motores, cameras, ano, nome, peso)
        self.motores = motores
        self.cameras = cameras
        self.ano = ano
        self.nome = nome
        self. peso = peso

    


    