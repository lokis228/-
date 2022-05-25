# -Зробив завдання python
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
#Результат:
Довжина масиву (max = 100): 6
Числа: 4 5 3 4 2 3
Результат: 4 3 2 
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
#Результат:
Довжина масиву (max = 100): 5
Числа: 1 2 3 4 5
Результат: 2 4 
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
#Результат:
Довжина масиву (max = 100): 5
Числа: 1 2 3 -1 -4
Результат: 3
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
#Результат:
Довжина масиву (max = 100): 5
Числа: 1 2 3 4 5
Результат: 4
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
#Результат:
Довжина масиву (max = 100): 5
Числа: 1 -3 4 -2 1
Результат: NO
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
#Результат:
Довжина масиву (max = 100): 5
Числа: 1 2 3 4 5
Результат: 0
Довжина масиву (max = 100): 5
Числа: 1 5 1 5 1
Результат: 2
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
#Результат:
Довжина масиву (max = 100): 6
Числа: 4 5 3 4 2 3
Результат: 3 2 4 3 5 4
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
#Результат:
Довжина масиву (max = 100): 6
Числа: 4 5 3 4 2 3
Результат: 5 4 3 3 2
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
#Результат:
Довжина масиву (max = 100): 6
Числа: 4 5 3 4 2 3
Результат: 3 4 5 3 4 2
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
#Результат:
Довжина масиву (max = 100): 3
Числа: 1 2 3
Результат: 3
# Завдання 11. Кількість різних елементів у монотонному масиві
n = int(input('Довжина масиву (max = 35): '))
m = list(map(int, input('Числа: ').split()))
a = 1
if len(m) != n:
    print('Помилка')
    exit(0)
for i in range(n-1):
    if m[i] != m[i+1]:
        a += 1
    else:
        continue
print(a)
# Результат:
Довжина масиву (max = 35): 5
Числа: 1 1 1 1 1
1
# Завдання 12. Шеренга
n = int(input())
a = list(input().split())
a = [int(i) for i in a]
a.sort()
a.reverse()
x = int(input())
for i in range(len(a)):
    if a[i] < x:
        print(i + 1);
        exit()
print(len(a) + 1)
# Результат:
8
165 163 160 160 157 157 155 154
162
3
# Завдання 13. Подвійний переворот
n, a, b, c, d = list(map(int, input('N, A, B, C, D: ').split()))
m = []
for i in range(n):
    m.append(i+1)
j = 0
for i in range(a-1, (b-a)//2+a):
    j += 1
    m[i], m[b-j] = m[b-j], m[i]
i = 0
for j in range(c-1, (d-c)//2+c):
    i += 1
    m[j], m[d-i] = m[d-i], m[j]
print(m)
# Результат:
N, A, B, C, D: 9 2 5 6 9
[1, 5, 4, 3, 2, 9, 8, 7, 6]
N, A, B, C, D: 9 3 6 5 8
[1, 2, 6, 5, 8, 7, 3, 4, 9]
# Завдання 14. Суперсдвиг

# Результат:

# Завдання 15. Кульки
_, *a, = map(int, input().split())
st = [(None, 0)]
count = 0
a.append(None)
for curr in a:
    if st[-1][0] == curr:
        st.append((curr, st[-1][1] + 1))
    else:
        if st[-1][1] > 2:
            while st[-1][0] == st[-2][0]:
                st.pop()
                count += 1
            st.pop()
            count += 1
        if st[-1][0] == curr:
            st.append((curr, st[-1][1] + 1))
        else:
            st.append((curr, 1))
    prev = st[-1][0]
print(count)
# Результат:
5 1 3 3 3 2
3
# Завдання 16. Побічна діагональ
n = int(input('n='))
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][n - i - 1] = 1
for i in range(n):
    for j in range(n - i, n):
        a[i][j] = 2
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
# Результат:
n= 4
0 0 0 1 
0 0 1 2 
0 1 2 2 
1 2 2 2 
# Завдання 17. Чи симетрична матриця?
n = int(input('n = '))
a = []
for i in range(n):
  row = input().split()
  for j in range(n): row[j] = int(row[j])
  a.append(row)
m = 0
for i in range(1, n):
  k = 0
  for j in range(i):
    if (a[i][j] == a[j][i]): k = k+1;
  if k == i: m = m+1
if (m == n-1): print('YES')
else: print('NO')
# Результат:
n = 3
0 1 2
1 5 3
2 3 4
YES
n = 3
0 0 0
0 0 0
1 0 0
NO
#Завдання 18. Змагання
ii = 0
res = 0
n, m = map( int, input( 'n, m = ').split() )
for i in range(n):
    a = map( int, input('-> ').split())
    a = list(a)
    summa = sum(a)
    if summa > res:
        res = summa
        ii = i
print(res)
print(ii)
# Результат:
n, m = 2 2
-> 5 4
-> 3 5
9
0
#19
#Завдання 20. Змагання – 3
sum = 0
res = 0
n, m = map( int, input( 'n, m = ').split() )
for i in range(n):
    s = 0
    mx = 0
    a = map(int, input('-> ').split())
    a = list(a)
    for j in a:
        s += j
        if mx < j:
            mx = j
    if mx > res:
        res, ii, sum = mx, i, s
    elif res == mx and s > sum:
        res, ii, sum = mx, i, s
print(ii)
# Результат:
n, m = 3 3
-> 1 2 7
-> 1 3 5
-> 4 1 6
0
