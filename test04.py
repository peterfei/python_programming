#-*- coding:utf-8 -*-
import random
def select_sort(seq):
    print(seq)
    n = len(seq)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if seq[j]<seq[min_idx]:
                min_idx = j
        if min_idx !=i:
            seq[i],seq[min_idx] = seq[min_idx],seq[i]
    print(seq)

if __name__ == '__main__':
    seq = list(range(10))
    random.shuffle(seq)
    select_sort(seq)
