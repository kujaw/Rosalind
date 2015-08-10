__author__ = 'kujaw'

import time
start = time.perf_counter()
start2 = time.process_time()

with open('rosalind_rna.txt', 'r') as f:
    rna = str(f.read())
    print(str.replace(rna, 'T', 'U'))

print("Timer:  ", time.perf_counter() - start)
print("Timer2: ", time.process_time() - start2)