import numpy as np
from collections import Counter

Samples = []
SampleItem = ''

# Extract FASTA formatted strings and turn them into list items
with open('rosalind_cons.txt') as f:
    for i, line in enumerate(f.readlines()):
        if not line.startswith('>'):
            SampleItem += line.rstrip('\n')
            if i == 169:
                Samples.append(SampleItem)
        else:
            if SampleItem != '':
                Samples.append(SampleItem)
                SampleItem = ''
            else:
                pass

# Make a numpy array from that list
dnaMatrix = np.asarray([list(x) for x in Samples])
print(dnaMatrix.shape)

genes = np.array(list('ACGT'))

P = np.array([(dnaMatrix == g).sum(axis=0) for g in genes])
print(P)
#c = genes[P.argmax(axis=0)]
#c = ''.join(c)

#print(c)
#for i, g in enumerate(genes):
#    print '%s:' % g, ' '.join(map(str, P[i]))

'''
m = len(dnaMatrix[0,:]) #number of DNA strains
n = len(dnaMatrix[:,]) #DNA strains length

a = []
c = []
g = []
t = []
cons_items = []

for i in range(0,m):
    a.append(list(dnaMatrix[:, i]).count('A'))
    c.append(list(dnaMatrix[:, i]).count('C'))
    g.append(list(dnaMatrix[:, i]).count('G'))
    t.append(list(dnaMatrix[:, i]).count('T'))
    cons_items.append(Counter(A=a[i], C=c[i], G=g[i], T=t[i]).most_common(1))

# Make a list of Counter.most_common tuples
cons_items = [x for y in cons_items for x in y]
cons_keys = [k for k,v in cons_items]

print("".join(str(k) for k in cons_keys))
print()
# Print profile matrix
print('A:', " ".join(str(k) for k in a))
print('C:', " ".join(str(k) for k in c))
print('G:', " ".join(str(k) for k in g))
print('T:', " ".join(str(k) for k in t))

with open('cons_output.txt', 'w') as fout:
    print("".join(str(k) for k in cons_keys), file=fout)
    print('A:', " ".join(str(k) for k in a), file=fout)
    print('C:', " ".join(str(k) for k in c), file=fout)
    print('G:', " ".join(str(k) for k in g), file=fout)
    print('T:', " ".join(str(k) for k in t), file=fout)'''