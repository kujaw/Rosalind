__author__ = 'kujaw'

import numpy as np
import time

start = time.perf_counter()

string = '''UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G'''

#sEncode =  string.split()
#sEncode = dict(zip(sEncode[0::2], sEncode[1::2]))

sEncode = dict(np.genfromtxt('s_encode.txt', dtype='str').reshape(64,2))

with open('rosalind_prot.txt') as f:
    rnaStr = str(f.read())

protStr = [rnaStr[i:i+3] for i in range(0, len(rnaStr)-3, 3)]
protStr = ''.join([sEncode[x] for x in rnaStr])

print(protStr)

print(time.perf_counter() - start)