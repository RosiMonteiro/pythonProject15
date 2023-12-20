from abc import ABC, abstractmethod

class Lutador(ABC):
    @abstractmethod
    def atacar(self):
        pass

    @abstractmethod
    def defender(self):
        pass

    @abstractmethod
    def obterVida(self):
        pass

class Superman(Lutador):
    def __init__(self):
        self._vida = 100

    def atacar(self):
        return 20

    def defender(self):
        return 5

    def obterVida(self):
        return self._vida

class MulherMaravilha(Lutador):
    def __init__(self):
        self._vida = 100

    def atacar(self):
        return 15

    def defender(self):
        return 8

    def obterVida(self):
        return self._vida

def combate(personagem1, personagem2):
    rodada = 1
    while personagem1.obterVida() > 0 and personagem2.obterVida() > 0:
        print("\nRodada", rodada)
        acao = input("Escolha a ação (A - atacar, D - defender): ").upper()
        if acao == "A":
            dano = personagem1.atacar() - personagem2.defender()
            if dano > 0:
                personagem2._vida -= dano
                print("Dano causado:", dano)
            else:
                print("Ataque falhado.")
        elif acao == "D":
            dano = personagem2.atacar() - personagem1.defender()
            if dano > 0:
                personagem1._vida -= dano
                print("Dano causado:", dano)
            else:
                print("Ataque falhado.")
        else:
            print("Ação inválida.")
        print("Vida de", personagem1.__class__.__name__, ":", personagem1.obterVida())
        print("Vida de", personagem2.__class__.__name__, ":", personagem2.obterVida())
        rodada += 1
    if personagem1.obterVida() > 0:
        print("\nO vencedor é", personagem1.__class__.__name__)
    elif personagem2.obterVida() > 0:
        print("\nO vencedor é", personagem2.__class__.__name__)
    else:
        print("\nEmpate")

if __name__ == '__main__':
    heroi1 = Superman()
    heroi2 = MulherMaravilha()
    combate(heroi1, heroi2)