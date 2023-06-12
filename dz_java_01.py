# Дано целое число N из отрезка [1; 1000]. Также даны N целых чисел Ai из отрезка [1; 1000000].
# Требуется для каждого числа Ai вывести количество различных делителей этого числа.
# В этой задаче несколько верных решений, попробуйте найти наиболее оптимальное.
# Для полученного решения укажите сложность в О-нотации.


import random, math

n = int(input('Введите число от 1 до 1000: '))
list_1 = [random.randint(1, 1000000) for _ in range(n)]


# print(list_1)


def divider(num=int):
    list_2 = [1]
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            list_2.append(i)
            list_2.append(num // i)
    return list_2


res = {}
for i in list_1:
    # print(divider(i))
    res.update({i: len(set(divider(i)))})
print(res)
