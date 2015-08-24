from operator import ne

with open('rosalind_hamm.txt') as f:
    a,b = f.read().split()
    d_H = sum(map(ne, a, b))
print(d_H)