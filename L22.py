# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
import random
n1 = int(input('Введите кол-во элементов первого множества: '))
n2 = int(input('Введите кол-во элементов второго множества: '))
list1 = [random.randint(1,11) for _ in range(n1)]
list2 = [random.randint(1,11) for _ in range(n2)]
print(f'Список 1: {list1}')
print(f'Список 2: {list2}')
list1=set(list1)
list2=set(list2)
print(f'Множество 1: {list1}')
print(f'Множество 2: {list2}')
n_inter = list1.intersection(list2)
print(sorted(n_inter))
