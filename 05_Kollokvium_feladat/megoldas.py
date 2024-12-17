class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

def range_update(bit1, bit2, l, r, value):
    bit1.update(l, value)
    bit1.update(r + 1, -value)
    bit2.update(l, value * (l - 1))
    bit2.update(r + 1, -value * r)

def prefix_sum(bit1, bit2, index):
    return bit1.query(index) * index - bit2.query(index)

def range_query(bit1, bit2, l, r):
    return prefix_sum(bit1, bit2, r) - prefix_sum(bit1, bit2, l - 1)

def process_test_case(n, commands):
    bit1 = FenwickTree(n)
    bit2 = FenwickTree(n)
    results = []
    for command in commands:
        if command[0] == 0:
            _, p, q, v = command
            range_update(bit1, bit2, p, q, v)
        elif command[0] == 1:
            _, p, q = command
            results.append(range_query(bit1, bit2, p, q))
    return results

T = int(input().strip())
results = []

for _ in range(T):
    N, C = map(int, input().strip().split())
    commands = []
    for _ in range(C):
        command = list(map(int, input().strip().split()))
        commands.append(command)
    results.extend(process_test_case(N, commands))

for result in results:
    print(result)