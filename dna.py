__author__ = 'kujaw'

import time
start = time.perf_counter()
start2 = time.process_time()

with open('rosalind_dna.txt', 'r') as f:
    words = list(f.read())
    print(words.count('A'), words.count('C'), words.count('G'), words.count('T'))
    # print(*map(words.count, "ACGT"))

print("Timer:  ", time.perf_counter() - start)
print("Timer2: ", time.process_time() - start2)