MOD = 10 ** 9

#A és B mátrix szorzása
def matrix_mult(A, B, size):
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
    return result

#Mátrix hatványozása
def matrix_pow(matrix, power, size):
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    base = matrix
    while power:
        if power % 2 == 1:
            result = matrix_mult(result, base, size)
        base = matrix_mult(base, base, size)
        power //= 2
    return result

#Az n-edik elem kiszámítása
def compute_an(k, b, c, n):
    if n <= k:
        return b[n - 1] % MOD

    T = [[0] * k for _ in range(k)]
    for i in range(k):
        T[0][i] = c[i]
    for i in range(1, k):
        T[i][i - 1] = 1

    T_n_k = matrix_pow(T, n - k, k)

    an = 0
    for i in range(k):
        an = (an + T_n_k[0][i] * b[k - i - 1]) % MOD

    return an

#Beolvasás
C = int(input())
results = []

for _ in range(C):
    k = int(input())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    n = int(input())
    results.append(compute_an(k, b, c, n))

#Kiírás
for result in results:
    print(result)