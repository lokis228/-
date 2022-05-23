
# -Зробив завдання на пайтоні
# Завдання 1. A[0], A[2], A[4],
n = int(input('Довжина масиву (max = 100): '))
m = list(map(int, input('Числа: ').split()))
result = []
if len(m) != n:
    print('Помилка')
    exit(0)
for i in range(n):
    if i % 2 != 0:
        continue
    else:
        result.append(m[i])
print('Результат: ', end='')
for i in range(len(result)):
    print(result[i], end=' ')
# Завдання 2. Вивести парні елементи
n = int(input('Довжина масиву (max = 100): '))
m = list(map(int, input('Числа: ').split()))
result = []
if len(m) != n:
    print('Помилка')
    exit(0)
for i in range(n):
    if m[i] % 2 != 0 or m[i] == 0:
        continue
    else:
        result.append(m[i])
print('Результат: ', end='')
for i in range(len(result)):
    print(result[i], end=' ')
# Завдання 3. Кількість позитивних елементів
n = int(input('Довжина масиву (max = 100): '))
m = list(map(int, input('Числа: ').split()))
result = 0
if len(m) != n:
    print('Помилка')
    exit(0)
for i in range(n):
    if m[i] >= 0:
        result += 1
    else:
        continue
print('Результат:', result)
# Завдання 4. Кількість елементів, більших за попередній
n = int(input('Довжина масиву (max = 100): '))
m = list(map(int, input('Числа: ').split()))
result = 0
if len(m) != n:
    print('Помилка')
    exit(0)
for i in range(n-1):
    if m[i+1] > m[i]:
        result += 1
    else:
        continue
print('Результат:', result)
# Завдання 5. Чи є два елементи з однаковими знаками
n = int(input('Довжина масиву (max = 100): '))
m = list(map(int, input('Числа: ').split()))
if len(m) != n:
    print('Помилка')
    exit(0)
for i in range(n-1):
    for j in range(i+1, n):
        if m[i] == m[j]:
            print('YES')
            exit(0)
        else:
            continue
print('NO')
# Завдання 6. Кількість елементів великих обох сусідів
n = int(input('Довжина масиву (max = 100): '))
m = list(map(int, input('Числа: ').split()))
result = 0
if len(m) != n:
    print('Помилка')
    exit(0)
for i in range(1, n-1):
    if m[i] > m[i+1] and m[i] > m[i-1]:
        result += 1
    else:
        continue
print(result)
# Завдання 7. Переставити елементи у зворотному порядку
n = int(input('Довжина масиву (max = 100): '))
m = list(map(int, input('Числа: ').split()))
if len(m) != n:
    print('Помилка')
    exit(0)
for i in range(n//2):
    m[i], m[n-1-i] = m[n-1-i], m[i]

print('Результат: ', end='')
for i in range(len(m)):
    print(m[i], end=' ')
# Завдання 8. Переставити сусідні елементи
n = int(input('Довжина масиву (max = 35): '))
m = list(map(int, input('Числа: ').split()))
if len(m) != n:
    print('Помилка')
    exit(0)
for i in range(0, n-1, 2):
    m[i], m[i+1] = m[i+1], m[i]
print('Результат: ', end='')
for i in range(len(m)):
    print(m[i], end=' ')
# Завдання 9. Циклічне зрушення вправо
n = int(input('Довжина масиву (max = 35): '))
m = list(map(int, input('Числа: ').split()))
a = []
if len(m) != n:
    print('Помилка')
    exit(0)
a.append(m[n-1])
for i in range(n-1):
    a.append(m[i])
print('Результат: ', end='')
for i in range(len(a)):
    print(a[i], end=' ')
# Завдання 10. Максимум у масиві
n = int(input('Довжина масиву (max = 35): '))
m = list(map(int, input('Числа: ').split()))
if len(m) != n:
    print('Помилка')
    exit(0)
for i in range(n-1):
    if m[i+1] > m[i]:
        a = m[i+1]
    else:
        continue
print('Результат:', a)
# Завдання 11. Кількість різних елементів у монотонному масиві
# Завдання 12. Шеренга
# Завдання 13. Подвійний переворот
# Завдання 14. Суперсдвиг
# Завдання 14. Суперсдвиг
# 
#
#
#
#
#
#
