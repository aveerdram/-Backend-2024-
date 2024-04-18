"""
Дан массив целых чисел A и массив целых чисел B, элементы из массива B уникальны и все элементы из массива B
также есть и в массиве A. Отсортируйте элементы массива A в таком же порядке, как в массиве B. Элементы, которые не
появляются в массиве B должны находится в конце списка и отсортированы по убыванию.

Пример: Массив A = [2, 4, 1, 3, 2, 4, 6, 7, 9, 2, 19] Массив B = [2, 1, 4, 3, 6, 9]

Ответ: отсортированный массив A = [2, 2, 2, 1, 4, 4, 3, 6, 9, 19, 7]
"""

def mydict(data):
    dict_to_sorting = dict()
    for i in range(len(B)):
        dict_to_sorting[B[i]] = i+1

    return dict_to_sorting

def mykey(x, B):
  dict_to_sorting = mydict(B)
  if x in B:
    return dict_to_sorting[x]

def mysort2(A, B):
  rest = []
  for x in A:
    if x not in B:
      A.remove(x)
      rest.append(x)

  A = sorted(A, key=lambda x: mykey(x, B))

  rest = sorted(rest, reverse=True)

  return A+rest