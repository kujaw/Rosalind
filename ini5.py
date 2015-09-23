__author__ = 'kujaw'


with open('rosalind_ini5.txt','r') as f:
    o = open('ini5-output', 'w')
    o.write(''.join(f.readlines()[1::2]))