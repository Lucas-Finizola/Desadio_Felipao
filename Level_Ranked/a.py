"""
 Desafio Classificador de nível de Herói

**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões

## Objetivo

Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

Se XP for menor do que 1.000 = Ferro
Se XP for entre 1.001 e 2.000 = Bronze
Se XP for entre 2.001 e 5.000 = Prata
Se XP for entre 5.001 e 7.000 = Ouro
Se XP for entre 7.001 e 8.000 = Platina
Se XP for entre 8.001 e 9.000 = Ascendente
Se XP for entre 9.001 e 10.000= Imortal
Se XP for maior ou igual a 10.001 = Radiante

## Saída

Ao final deve se exibir uma mensagem:
"O Herói de nome **{nome}** está no nível de **{nivel}**"

Bons estudos 😉
"""

print("Bem vindo!\nVamos verificar seu rank")

nome = input("Digite o nome do seu Herói: ")
xp = int(input("Digite a quantidade de experiencia adquirida em sua jornada: "))
rank = "Ferro"

while True:
        if xp <1000:
            rank = "Ferro"
            break
        elif xp>1000 and xp<=2000:
            rank = "Bronze"
            break
        elif xp>2000 and xp<=5000:
            rank = "Prata"
            break
        elif xp>5000 and xp<=7000:
            rank = "Ouro"
            break
        elif xp>7000 and xp<=8000:
            rank = "Platina"
            break
        elif xp>8000 and xp<=9000:
            rank = "Ascendente"
            break
        elif xp>9000 and xp<=10000:
            rank = "Imortal"
            break
        elif xp>=10001:
            rank = "Radiante"
            break
            
print(f"O Herói de nome {nome} está no Rank {rank}")


                