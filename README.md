# Sistema de Criação de Heróis para RPG
Este projeto implementa um sistema de criação de heróis para um jogo de RPG em Python, usando o padrão de design Factory para criar heróis com qualquer combinação de raça e classe. Os jogadores podem escolher entre diferentes raças (Humano, Elfo, Orc) e classes (Guerreiro, Mago, Ladino), criando heróis únicos com habilidades e atributos distintos.

## Funcionalidades
- Criação de heróis com diferentes combinações de raça e classe.
- Definição de habilidades e atributos baseados na raça e classe escolhidas.
- Expansível para novas raças e classes.

## Estrutura do Código
O projeto segue a seguinte estrutura:

1. Classe Abstrata Raca: Define os atributos básicos de cada raça.
2. Classe Abstrata Classe: Define o método abstrato apresentar_habilidades, que será implementado nas classes concretas.
3. Classes Concretas de Raça e Classe: Raças como Humano, Elfo, e Orc; Classes como Guerreiro, Mago, e Ladino.
4. Classe Heroi: Combina Raca e Classe para criar o herói final com uma configuração de atributos e habilidades.
5. Factory HeroiFactory: Facilita a criação de heróis com qualquer combinação de raça e classe.

## Exemplo de Código
Aqui está um exemplo de uso do HeroiFactory diretamente no código, caso você queira instanciar um herói sem o input do usuário.

```python
from hero_factory import HeroiFactory


# Criar um herói chamado Legolas, da raça Elfo e classe Ladino
heroi = HeroiFactory.criar_heroi("Legolas", "Elfo", "Ladino")

# Exibir informações do herói
print(f"Herói criado: {heroi.nome}")
print(f"Raça: Elfo, Classe: Ladino")
print(heroi.atributos())
print(f"Habilidades: {heroi.apresentar_habilidades()}")
```

### Saída Esperada
```plaintext
Herói criado: Legolas
Raça: Elfo, Classe: Ladino
Força: 5, Inteligência: 8, Destreza: 9
Habilidades: Habilidade em furtividade e ataques rápidos.
```

## Estrutura de Expansão
Para adicionar novas raças ou classes, siga estas instruções:

### Nova Raça: Crie uma nova classe que herde de Raca e defina atributos específicos.

```python
class Anão(Raca):
    def __init__(self):
        super().__init__(forca=8, inteligencia=5, destreza=6)
```

### Nova Classe: Crie uma nova classe que herde de Classe e defina o método apresentar_habilidades.

```python
class Arqueiro(Classe):
    def apresentar_habilidades(self):
        return "Habilidade de combate à distância e precisão."
```

### Adicione a nova raça ou classe na HeroiFactory para que o sistema possa reconhecer essa nova combinação.

```python
class HeroiFactory:
    @staticmethod
    def criar_raca(raca_input):
        if raca_input == "Humano":
            return Humano()
        elif raca_input == "Elfo":
            return Elfo()
        elif raca_input == "Orc":
            return Orc()
        elif raca_input == "Anao":  # Nova raça adicionada aqui
            return Anao()
        else:
            raise ValueError("Raça inválida.")

    @staticmethod
    def criar_classe(classe_input):
        if classe_input == "Guerreiro":
            return Guerreiro()
        elif classe_input == "Mago":
            return Mago()
        elif classe_input == "Ladino":
            return Ladino()
        elif classe_input == "Arqueiro":  # Nova classe adicionada aqui
            return Arqueiro()
        else:
            raise ValueError("Classe inválida.")
```