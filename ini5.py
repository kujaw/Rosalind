__author__ = 'kujaw'


with open('rosalind_ini5.txt','r') as f:
    o = open('output.txt', 'w')
    o.write(''.join(f.readlines()[1::2]))