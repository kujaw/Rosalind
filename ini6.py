__author__ = 'kujaw'
'''
dict = {}
bwords = []
a = open('rosalind_ini6.txt')

for line in a:
    bwords.append(line)

a.close()

print(bwords)

for i in bwords:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

for key in dict:
    print(key, dict[key])
'''
with open('rosalind_ini6.txt', 'r') as f:
    from collections import Counter
    for k, v in Counter(str(f.readlines()).split()).items(): print(k, v)