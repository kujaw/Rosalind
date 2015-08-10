__author__ = 'kujaw'

import time
start = time.perf_counter()
start2 = time.process_time()

with open('rosalind_revc.txt', 'r') as f:
    st = str(f.read())
    st = st.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
    print(st)

print("Timer:  ", time.perf_counter() - start)
print("Timer2: ", time.process_time() - start2)