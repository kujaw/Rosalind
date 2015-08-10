from time import perf_counter

start = perf_counter()

f = open('rosalind_gc.txt')
raw_samples = f.readlines()
f.close()
samples = {}
cur_key = ''

for line in raw_samples:
    if line[0] == '>':
        cur_key = line[1:].rstrip()
        samples[cur_key] = ' '
    else:
        samples[cur_key] += line.rstrip()

for s_id, s in samples.items():
    samples[s_id] = float((s.count('G') + s.count('C'))*100/(len(s)-1))
    print(s_id, samples[s_id], len(s), s)


sVal=list(samples.values())
sKey=list(samples.keys())
print(sKey[sVal.index(max(sVal))])
print('%.6f' % max(sVal))
'''
(s_id, gc) = max(list(samples.items()), key = lambda item:item[1])
print(s_id)
print(gc, '%')
'''
print('Timer:', perf_counter() - start)