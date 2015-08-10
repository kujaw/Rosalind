from operator import ne
from time import perf_counter

start1 = perf_counter()

with open('rosalind_hamm.txt') as f:
    a,b = f.read().split()
    d_H = sum(map(ne, a, b))
print(d_H)

print('Timer1:', perf_counter()-start1)
start2 = perf_counter()

with open('rosalind_hamm.txt') as f:
    a,b = f.readlines()
    d_H = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            d_H += 1
print(d_H)

print('Timer2:', perf_counter()-start2)
start3 = perf_counter()

print(sum(map(str.__ne__, *open('rosalind_hamm.txt').read().split())))

print('Timer3:', perf_counter()-start3)