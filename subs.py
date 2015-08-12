with open('rosalind_subs.txt', 'r') as f:
    genome, repeat = f.read().split()

repeat_indices = []
n = 0

while len(genome[n:]) >= len(repeat):
    if repeat not in genome[n:]:
        break
    else:
        repeat_indices.append(genome[n:].index(repeat) + n + 1)
        n += genome[n:].index(repeat) + 1

print(repeat_indices)