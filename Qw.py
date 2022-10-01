import sqlite3
import re


# 1 Задан массив целых чисел. Написать функцию нахождения максимального элемента в массиве


some_list1 = [1, 27, 3, 9, 48, 1]


def biggest_int(item: list):
    result = 0
    for i in item:
        if result < i:
            result = i
    return result

assert biggest_int(some_list1) == 48, True

# 2 Реализовать функцию сортировки пузырьком

some_list2 = [6, 5, 3, 3, 8, 1]


def buble_sort(item: list):
    for j in range(len(item)):
        for i in range(0, len(item) - 1):
            if item[i] > item[i + 1]:
                item[i], item[i + 1] = item[i + 1], item[i]
    return item


assert buble_sort(some_list2) == [1,3,3,5,6,8]

# 3 Это задача на знание БД и SQL
# Products(id, name, price)
# Tags(id, name)
# ProductTags(product_id, tag_id)

"Select pr.* from Products pr JOIN ProductTags prTg on prTg.product_id = pr.id GROUP BY pr.id HAVING COUNT(*) > 10"


# 4 Задан упорядоченный по возрастанию массив.
# Реализовать алгоритм бинарного поиска для нахождения значения в массиве.
# Вернуть номер элемента или уведомить что такого элемента нет.

some_list3 = [1,2,3,4,5,6,7]


def bin_searching(item: list, search_item: int):
    low = 0
    high = len(item) - 1
    search_res = False
    while low <= high and not search_res:
        mid = (low+high)//2
        guess = item[mid]
        if guess == search_item:
            search_res = True
            return search_res
        elif guess > search_item:
            high = mid-1
        else:
            low = mid + 1
    return search_res

assert bin_searching(some_list3, 5), True
assert bin_searching(some_list3, 2), True
assert bin_searching(some_list3, 99) == False


# 5 Реализовать класс 2-х мерный вектор

class Vector2D:
    def __init__(self):
        self._x = 4
        self._y = 5


    def __repr__(self):
        return f"Vector x: {self._x}, Vector y: {self._y}"

    def __add__(self, other):
        return (self._x + other._x), (self._y + other._y)

    def __sub__(self, other):
        return (self._x + self._y) - (other._x + other._y)

    def __mul__(self, other):
        return (self._x + self._y) * other

examp = Vector2D()
examp2 = Vector2D()
assert str(examp) == "Vector x: 4, Vector y: 5", True
examp + examp2
assert  (8,10) , True
assert examp - examp2 == 0, True
assert examp * 5 == 45, True
# Can deal with it by means of init and setters/getters, but wanted to use this way
# 6  Проверить является ли строка палиндромом

def is_pali(some_string: str):
    forwards = ''.join(re.findall(r'[a-z]+', some_string.lower()))
    backwords = forwards[::-1]
    return forwards == backwords

assert is_pali('Abccba') == True
assert is_pali('Not pali for sure') == False