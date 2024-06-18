"""
 Desafio Classificador de nível de Herói
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


                