__author__ = 'kujaw'


with open('rosalind_fib.txt', 'r') as f:
    data = str(f.read().rstrip()).split(' ')

n = int(data[0])   # months
k = int(data[1])   # rabbit pairs produced
i = 1

prev = 1
cur = 1

for i in range(2, n):
        prev, cur = cur, cur + prev * k

print(cur)