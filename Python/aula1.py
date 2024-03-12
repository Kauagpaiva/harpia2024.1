class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = int(idade) # anos
        self.altura = float(altura) # cm

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += float(1/2)
        print("Agora {} tem {} anos e {} cm de altura".format(self.nome, self.idade, self.altura))

fulano = Pessoa("Fulano", 13, 176)
for _ in range(10):
    fulano.envelhecer()