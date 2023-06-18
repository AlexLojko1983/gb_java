import random

n = int(input('Введите длину массива: '))
list_1 = [random.randint(1, 50) for _ in range(n)]
# print(list_1)


def heapsort(list_1: list, n, i):
    max_el = i

    left = i * 2 + 1
    right = i * 2 + 2
    if left < n and list_1[left] > list_1[i]:
        max_el = left
    if right < n and list_1[right] > list_1[max_el]:
        max_el = right
    if max_el != i:
        list_1[i], list_1[max_el] = list_1[max_el], list_1[i]
        heapsort(list_1, n, max_el)


for i in range(n, -1, -1):
    heapsort(list_1, n, i)

for i in range(n-1, 0, -1):
    list_1[i],list_1[0] = list_1[0],list_1[i]
    heapsort(list_1, i, 0)

print(list_1)
