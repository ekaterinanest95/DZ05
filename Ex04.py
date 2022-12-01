# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


# data = open('file02.txt', 'r+') # код для удаления данных из файла
# data.seek(0)
# data.truncate()
# data.close()


with open('file02.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Введите текст, необходимый для сжатия: '))
with open('file02.txt', 'r') as file:
    text = file.readline()
    new_text = text.split()

print(text)


def file_encod(txt):
    result = ''
    prev_symb = ''
    count = ''
    if not txt:
        return ''

    for symb in txt:
        if symb != prev_symb:
            result += str(count) + prev_symb
            count = 1
            prev_symb = symb
        else:
            count += 1
    else:
        result += str(count) + prev_symb
    return result

new_text = file_encod(text)

with open('file05.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{new_text}')

print(new_text)
