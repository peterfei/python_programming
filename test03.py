#-*- coding:utf-8-*-
import  random
def bubble_sort(seq):
    n = len(seq)
    for i in range(n-1):
        print(seq)
        for j in range(n-1-i):
            if seq[j]>seq[j+1]:
                seq[j],seq[j+1] = seq[j+1],seq[j]
        print(seq)


if __name__=='__main__':
    seq = list(range(10))
    random.shuffle(seq)
    bubble_sort(seq)
