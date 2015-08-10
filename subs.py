#genome = 'GATATATGCATATACTT'
#repeat = 'ATAT'

f = open('rosalind_subs.txt', 'r')
data = f.read().split('\n')
f.close()
genome = str(data[0])
repeat = str(data[1])

repeat_indices = []
n = 0
while len(genome[n:]) >= len(repeat):
    if repeat not in genome[n:]:
        break
    else:
        print('Position of repeat in genome:', genome[n:].index(repeat) + n + 1)
        repeat_indices.append(genome[n:].index(repeat) + n + 1)
        n += genome[n:].index(repeat) + 1

print(repeat_indices)