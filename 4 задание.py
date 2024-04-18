"""
Реализуйте алгоритм бинарного поиска. 
Функция должна принимать отсортированный список и элемент для поиска, 
и возвращать индекс этого элемента в списке, если он найден, или -1 в противном случае.
"""

def mysearch(data, elem):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        midVal = data[mid]
        if midVal == elem:
            return mid
        if midVal > elem:
            high = mid - 1
        else:
            low = mid + 1
    return -1