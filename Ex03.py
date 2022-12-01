# Создайте программу для игры в ""Крестики-нолики"".

import random

pole = ['|', ' ', '|', ' ', '|', ' ', '|', '|', ' ', '|', ' ', '|', ' ', '|', '|', ' ', '|', ' ', '|', ' ', '|']

def print_pole():
    print(pole[0], pole[1], pole[2], pole[3], pole[4], pole[5], pole[6])
    print(pole[7], pole[8], pole[9], pole[10], pole[11], pole[12], pole[13])
    print(pole[14], pole[15], pole[16], pole[17], pole[18], pole[19], pole[20])


round = 0
ochered = random.randint(1, 2)
print(f'Чей ход: {ochered}')
player1 = 1
player2 = 2
end_game = False

""""win_res = [[1, 3, 5],
           [8, 10, 12],
           [15, 17, 19],
           [1, 8, 15],
           [3, 10, 17],
           [5, 12, 19],
           [1, 10, 19],
           [5, 10, 15]]"""

def get_result():
    winner = ''
    if pole[1] == 'x' and pole[3] == 'x' and pole[5] == 'x':
         winner = player1
    if pole[8] == 'x' and pole[10] == 'x' and pole[12] == 'x':
        winner = player1
    if pole[15] == 'x' and pole[17] == 'x' and pole[19] == 'x':
        winner = player1
    if pole[1] == 'x' and pole[8] == 'x' and pole[15] == 'x':
        winner = player1
    if pole[3] == 'x' and pole[10] == 'x' and pole[17] == 'x':
        winner = player1
    if pole[5] == 'x' and pole[12] == 'x' and pole[19] == 'x':
        winner = player1
    if pole[1] == 'x' and pole[10] == 'x' and pole[19] == 'x':
        winner = player1
    if pole[5] == 'x' and pole[10] == 'x' and pole[15] == 'x':
        winner = player1


    if pole[1] == '0' and pole[3] == '0' and pole[5] == '0':
        winner = player2
    if pole[8] == '0' and pole[10] == '0' and pole[12] == '0':
        winner = player2
    if pole[15] == '0' and pole[17] == '0' and pole[19] == '0':
        winner = player2
    if pole[1] == '0' and pole[8] == '0' and pole[15] == '0':
        winner = player2
    if pole[3] == '0' and pole[10] == '0' and pole[17] == '0':
        winner = player2
    if pole[5] == '0' and pole[12] == '0' and pole[19] == '0':
        winner = player2
    if pole[1] == '0' and pole[10] == '0' and pole[19] == '0':
        winner = player2
    if pole[5] == '0' and pole[10] == 'x' and pole[15] == '0':
        winner = player2

    return winner

while end_game == False:
    round +=1
    print_pole()
    print(f'Раунд: {round}')
    print(f'Чей ход: {ochered}')
    hod1 = int(input("Введите координату символа (1-я строка: 1, 3, 5, 2-я строка: 8, 10, 12, 3-я строка: 15, 17, 19): "))
    if ochered == player1:
        hod2 = input("Введите символ 'x': ")
        ind = hod1
        pole[ind] = hod2
        ochered = player2
    else:
        hod2 = input("Введите символ '0': ")
        ind = hod1
        pole[ind] = hod2
        ochered = player1

    winner = get_result()
    if winner != '':
        print_pole()
        print(winner)
        end_game = True
    else:
        end_game = False



