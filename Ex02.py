# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# варинт человек против человека

import random

player1 = 1
player2 = 2
score1 = 0
score2 = 0
sweets = 100
round = 0
ochered = random.randint(1, 2)
print(f'Чей ход: {ochered}')

while sweets > 28:
    round +=1
    print(f'Раунд: {round}')
    print(f'Чей ход: {ochered}')
    hod = int(input("Введите число конфет: "))
    print(f'Сколько конфет забрал: {hod}')
    sweets = sweets - hod
    print(f'Осталось конфет: {sweets}')
    if ochered == player1:
        score1 += hod
        ochered = player2
    else:
        score2 += hod
        ochered = player1
else:
    round += 1
    print(f'Раунд: {round}')
    print(f'Чей ход: {ochered}')
    hod = sweets
    print(f'Сколько конфет забрал: {hod}')
    print(f'Победитель: {ochered}')

print(f'Счет первого игрока: {score1}')
print(f'Счет второго игрока: {score2}')



# варинт человек против бота

import random

player_man = 1
player_bot = 2
score1 = 0
score2 = 0
sweets = 100
round = 0
ochered = random.randint(1, 2)
print(f'Чей ход: {ochered}')

while sweets > 28:
    round +=1
    print(f'Раунд: {round}')
    print(f'Чей ход: {ochered}')
    if ochered == player_man:
        hod = int(input("Введите число конфет: "))
        print(f'Сколько конфет забрал: {hod}')
        sweets = sweets - hod
        print(f'Осталось конфет: {sweets}')
        score1 += hod
        ochered = player_bot
    else:
        hod = random.randint(1, 28)
        print(f'Сколько конфет забрал: {hod}')
        sweets = sweets - hod
        print(f'Осталось конфет: {sweets}')
        score2 += hod
        ochered = player_man
else:
    round += 1
    print(f'Раунд: {round}')
    print(f'Чей ход: {ochered}')
    hod = sweets
    print(f'Сколько конфет забрал: {hod}')
    print(f'Победитель: {ochered}')

print(f'Счет игрока: {score1}')
print(f'Счет бота: {score2}')

# варинт человек против ИИ

import random

player_man = 1
player_robot = 2
score1 = 0
score2 = 0
sweets = 100
round = 0
ochered = random.randint(1, 2)
print(f'Чей ход: {ochered}')

while sweets > 28:
    round +=1
    print(f'Раунд: {round}')
    print(f'Чей ход: {ochered}')
    if ochered == player_man:
        hod = int(input("Введите число конфет: "))
        print(f'Сколько конфет забрал: {hod}')
        sweets = sweets - hod
        print(f'Осталось конфет: {sweets}')
        score1 += hod
        ochered = player_robot
    else:
        if sweets in range(75, 100):
            hod = random.randint(1, 15)
        elif sweets in range(37, 75):
            hod = random.randint(1, 7)
        elif sweets in range(28, 37):
            hod = random.randint(1, 3)
            print(f'Сколько конфет забрал: {hod}')
            sweets = sweets - hod
            print(f'Осталось конфет: {sweets}')
            score2 += hod
            ochered = player_man
else:
    round += 1
    print(f'Раунд: {round}')
    print(f'Чей ход: {ochered}')
    hod = sweets
    print(f'Сколько конфет забрал: {hod}')
    print(f'Победитель: {ochered}')

print(f'Счет игрока: {score1}')
print(f'Счет робота: {score2}')








