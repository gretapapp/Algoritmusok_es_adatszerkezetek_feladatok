def bricksGame(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return arr[0] + arr[1]
    if n == 3:
        return arr[0] + arr[1] + arr[2]

    max_scores = [0] * n
    max_scores[n-1] = arr[n-1]
    max_scores[n-2] = arr[n-2] + arr[n-1]
    max_scores[n-3] = arr[n-3] + arr[n-2] + arr[n-1]

    for i in range(n-4, -1, -1):
        max_scores[i] = max(arr[i] + min(max_scores[i+2], max_scores[i+3], max_scores[i+4] if i+4 < n else 0),
                            arr[i] + arr[i+1] + min(max_scores[i+3], max_scores[i+4] if i+4 < n else 0, max_scores[i+5] if i+5 < n else 0),
                            arr[i] + arr[i+1] + arr[i+2] + min(max_scores[i+4] if i+4 < n else 0, max_scores[i+5] if i+5 < n else 0, max_scores[i+6] if i+6 < n else 0))

    return max_scores[0]

# Beolvasás és kiíratás
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(bricksGame(arr))