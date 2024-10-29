from abc import ABC, abstractmethod

# Classe abstrata Raca
class Raca(ABC):
    def __init__(self, forca, inteligencia, destreza):
        self.forca = forca
        self.inteligencia = inteligencia
        self.destreza = destreza

# Classe abstrata Classe
class Classe(ABC):
    @abstractmethod
    def apresentar_habilidades(self):
        pass

# Classes concretas de Raca
class Humano(Raca):
    def __init__(self):
        super().__init__(forca=7, inteligencia=6, destreza=7)

class Elfo(Raca):
    def __init__(self):
        super().__init__(forca=5, inteligencia=8, destreza=9)

class Orc(Raca):
    def __init__(self):
        super().__init__(forca=9, inteligencia=4, destreza=6)

# Classes concretas de Classe
class Guerreiro(Classe):
    def apresentar_habilidades(self):
        return "Combate corpo a corpo."

class Mago(Classe):
    def apresentar_habilidades(self):
        return "Controle elemental."

class Ladino(Classe):
    def apresentar_habilidades(self):
        return "Furtividade e ataques letais."

# Classe Heroi que herda de Raca e Classe
class Heroi:
    def __init__(self, nome, raca, classe):
        self.nome = nome
        self.raca = raca
        self.classe = classe

    def apresentar_habilidades(self):
        return self.classe.apresentar_habilidades()

    def atributos(self):
        return f"Força: {self.raca.forca}, Inteligência: {self.raca.inteligencia}, Destreza: {self.raca.destreza}"

# Factory para criar heróis
class HeroiFactory:
    @staticmethod
    def criar_raca(raca_input):
        # Tratando string.
        raca_input = raca_input.lower()

        if raca_input == "humano":
            return Humano()
        elif raca_input == "elfo":
            return Elfo()
        elif raca_input == "orc":
            return Orc()
        else:
            raise ValueError("Raça inválida.")

    @staticmethod
    def criar_classe(classe_input):
        # Tratando string.
        classe_input = classe_input.lower()

        if classe_input == "guerreiro":
            return Guerreiro()
        elif classe_input == "mago":
            return Mago()
        elif classe_input == "ladino":
            return Ladino()
        else:
            raise ValueError("Classe inválida.")

    @staticmethod
    def criar_heroi(nome, raca_input, classe_input):
        raca = HeroiFactory.criar_raca(raca_input)
        classe = HeroiFactory.criar_classe(classe_input)
        return Heroi(nome, raca, classe)

# Driver Code
def main():
    print("Criação de Herói")

    while True:
        nome = input("Digite o nome do herói: ")
        raca_input = input("Escolha a raça (Humano, Elfo, Orc): ")
        classe_input = input("Escolha a classe (Guerreiro, Mago, Ladino): ")


        try:
            heroi = HeroiFactory.criar_heroi(nome, raca_input, classe_input)
            print(f"\nHerói criado: {heroi.nome}")
            print(f"Raça: {raca_input}, Classe: {classe_input}")
            print(heroi.atributos())
            print(f"Habilidades: {heroi.apresentar_habilidades()}")
            break
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()