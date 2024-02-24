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
    def __init__(self, nome, ano, motores, cameras, peso):
        self.motores = motores
        self.cameras = cameras
        self.ano = ano
        self.nome = nome
        self.peso = peso

    def __repr__(self):
        return self.nome
    
class Drones:
    def __init__(self):
        self.drones = list()

    def __repr__(self):
        result = str(self.drones)
        return result

    def add(self, other):
        self.drones.append(other)

    def exibir(self, nome):
        drone = None
        for item in self.drones:
            if item.nome == nome:
                drone = item
        if drone != None:
            return print(
                "\nNome: {}\nAno de fabricação: {}\nQuantidade de motores: {}\nQuantidade de câmeras: {}\nPeso(em kg): {}".format(drone.nome, drone.ano, drone.motores, drone.cameras, drone.peso)
            )
        return print('\nDrone não encontrado')

    def tabela(self):
        if len(self.drones) == 0:
            return print("\nNão há drones")
        return print("Tabela:"), [print("\nNome: {}\nAno de fabricação: {}\nQuantidade de motores: {}\nQuantidade de câmeras: {}\nPeso(em kg): {}".format(drone.nome, drone.ano, drone.motores, drone.cameras, drone.peso)) for drone in self.drones]

    def rank(self):
        if len(self.drones) == 0:
            return print("\nNão há drones")
        
        if len(self.drones) == 1:
            return print("\nRank"), print("1 - {} ({})".format(self.drones[0].nome, self.drones[0].ano))
        
        copia = self.drones.copy() #cria uma variavel com todos os drones para eu poder mexer, sem afetar a lista original
        resultado = list() # o resultado será uma lsita com os drones, em ordem do mais novo para o mais velho
        
        for _ in range(len(copia)):
            maisNovo = copia[0] # pega o primeiro drone da lista e assume que ele é o mais novo
            for drone in copia[1:]: # percorre a lista apartir do segundo drone e encontra o drone mais novo dentro da lista, remove ele da copia e adiciona no resultado
                if drone.ano > maisNovo.ano: 
                    maisNovo = drone
            copia.remove(maisNovo)
            resultado.append(maisNovo)
        return print("\nRank:"),[print("{} - {} ({})".format(indice+1, resultado[indice], resultado[indice].ano)) for indice in range(len(resultado))]
    
    def deletar(self, other):
        if other not in self.drones:
            return print("Drone não encontrado")
        self.drones.remove(other)
        return print("{} deletado com sucesso!".format(other))

### Testes Drones ###
    
harpia001 = Drone("harpia001", 2017, 4, 1, 3)
harpia = Drone("harpia", 2020, 4, 1, 1)
icarus = Drone("icarus", 2021, 3, 2, 2)
pegasus = Drone("pegasus", 2023, 5, 3, 1)

drones = Drones()
drones.add(harpia001)
drones.add(harpia)
drones.add(icarus)
drones.add(pegasus)

print(drones)

drones.exibir("harpia")
drones.exibir("pegasus")
drones.exibir("kaua")

drones.rank()

drones.tabela()

drones.deletar(harpia)
print(drones)
    