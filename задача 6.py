f = open('27.txt')
n = int(f.readline())
mas = []
for i in range(n):
    mas.append(int(f.readline()))
f = [0] * n
p = [0] * n
for j in range(3):
    for i in range(3 + j, (n // 2) + j, 3):
        f[j] += (mas[i] + mas[-i + (2 * j)]) * (i - j)
    f[j] += mas[(n // 2) + j] * (n // 2)
for j in range(3):
    for i in range((n // 6)):
        p[j] += mas[(i * 3) + j]
for i in range(n - 3):
    p[i + 3] = p[i] - mas[i] + mas[((n // 2) + i) % n]
for i in range(n - 3):
    f[i + 3] = f[i] - (p[i + 3] - p[i - 3]) * 3
print(min(f))
