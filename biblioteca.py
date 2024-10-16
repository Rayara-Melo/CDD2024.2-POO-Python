
class Pessoa:
    def __init__(self, nome, peso, idade): #TUDO QUE TEM sef É UM ATRIBUTO.
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.falando = False
        self.comendo = False
        self.dormindo = False

    def falar (self):
        if self.falando == False:
            if self.comendo == False:
                if self.dormindo == False:
                    print(f"{self.nome} está falando")
                    self.falando=True
                else:print("Não pode falar pois está comendo")
            else:
                print("Não pode falar pois está dormindo")
        else:
            print(f"{self.nome} já estava falando")

    def parafalar(self):
        if self.falando == False:
            print(f"{self.nome} parou de falar")
            self.falando=True

    def comer (self):
        if self.comendo == False:
            if self.falando == False:
                if self.dormindo == False:
                    print(f"{self.nome} está comendo")
                    self.comendo == True
                else:
                    print("Não pode comer pois está dormindo")
            else:
                print("Não pode comer pois está falando")
        else:
            print(f"{self.nome} já estava comendo")

    def paracomer(self):
        if self.comendo == False:
            print(f"{self.nome} parou de falar")
            self.falando=True

    def dormir (self):
        if self.dormindo == False:
            if self.falando == False:
                if self.comendo == False:
                    print(f"{self.nome} está dormindo")
                    self.dormindo == True
                else:
                    print("Não pode dormir pois está comendo")
            else:
                print("Não pode dormir pois está falando")
        else:
            print(f"{self.nome} já estava dormindo")

    def paradormir(self):
        if self.dormindo == False:
            print(f"{self.nome} parou de dormir")
            self.dormindo=True

class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"{self.nome} foi comer")

class Gato(Animal): #HERANÇA
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def miar(self):
        print(f"{self.nome} está miando")

class Vaca(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome,cor)

    def mugir (self):
        print(f"{self.nome} está mugindo")

class Cachorro(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome,cor)

    def latinho(self):
        print(f"{self.nome} está latinho")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)

    def pular(self):
        print(f"{self.nome} está pulando")

class Atleta:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.aposentado = False
        self.aquecido = False

    def aquecer (self):
        print(f"{self.nome} foi aquecer")
        self.aposentado = True

    def aposentar (self):
        print(f"{self.nome} está na rede...")
        self.aposentado = True

    def desaposentar (self):
        print(f"{self.nome} está desaposentar")
        self.aposentado = True

class Corredor(Atleta):
    def __int__(self, nome, peso):
        super().__int__(nome, peso)

    def correr(self):
        if self.aquecido == True:
            if self.aposentado == False:
                print(f"{self.nome} foi correr")
            else:
                print(f"{self.nome} não foi correr porque está aposentado")
        else:
            print(f"{self.nome} não pode correr porque não aqueceu")

class Nadador(Atleta):
    def __int__(self, nome, peso):
        super().__int__(nome,peso)

    def nadar(self):
        if self.aquecido == True:
            if self.aposentar == False:
                print(f"{self.nome} foi nadar")
            else:
                print(f"{self.nome} não foi nadar porque está aposentado")
        else:
            print(f"{self.nome} não foi nadar porque não está aquecido")

class Cilista(Atleta):
    def __int__(self, nome, peso):
        super().__int__(nome,peso)

    def bike(self):
        if self.aquecido == True:
            if self.aposentar() == False:
                print(f"{self.nome} foi andar de Bike")
            else:
                print(f"{self.nome} não foi nadar porque está aposentado")
        else:
            print(f"{self.nome} não foi nadar porque não está aquecido")

class Triatleta(Corredor, Nadador, Cilista):
    def __int__(self):
        super().__init__(Corredor, Nadador, Cilista)

def gravarTexto(texto):
    with open("registro.txt", "a") as arquivo:
        arquivo.write(f"{texto}\n")

def lerTexto(): #
    with open("registro.txt", "r") as arquivo2:
        txt = arquivo2.read()
        print(txt)

