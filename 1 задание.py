# Дан массив целых чисел. Напишите функцию, которая получает данный массив в качестве аргумента и сортирует его по возрастанию

def mysort(data):
    dat = data[:]

    for i in range(len(dat) - 1):
        for j in range(len(dat) - 1 - i):
            if dat[j] > dat[j + 1]:
                dat[j], dat[j + 1] = dat[j + 1], dat[j]

    return dat
