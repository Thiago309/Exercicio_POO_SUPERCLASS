class Tamagushi:

    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.dormir = False
        self.falar = False

    def comer(self, tipo):
        if self.comendo == True:
            print(f"{self.nome} já está comendo {tipo}.")
        else:
            self.comendo = True
            print(f"{self.nome} foi comer agora {tipo}.")


    def pararComer(self):
        if self.comendo == True:
            self.comendo = False
            print("Parei de comer.")
        else:
            print("Eu não estou comendo.")

    def dormir(self):
        if self.dormir == True:
            print(f"{self.nome} já está dormindo.")
        else:
            self.dormir = True
            print(f"{self.nome} foi dormir agora.")

    def acordar(self):
        if self.dormir == True:
            self.dormir = False
            print("Acordei !!!")
        else:
            print("Já estou acordado !")

    def falar(self):
        if self.comendo == False and self.dormir() == False:
            if self.falar == True:
                print(f"{self.nome} já está falando.")
            else:
                self.falar = True
                print(f"{self.nome} falou agora.")
        else:
            print("Não posso falar, estou comendo. Eu tenho educação, não sou cavalo pra comer de boca cheia !")

    def pararFalar(self):
        if self.falar == False:
            print("Eu não estou falando")
        else:
            self.falar = False
            print("Parei de falar")