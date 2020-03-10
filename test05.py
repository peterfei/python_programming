#-*- coding:utf-8 -*-
import random

def insertion_sort(seq):
    n = len(seq)
    print(seq)
    for i in range(1,n):
        value = seq[i]
        pos = i
        while pos > 0 and value < seq[pos-1]:
            seq[pos] = seq[pos-1]
            pos -=1
        seq[pos] = value
        print(seq)


def quick_sort(seq):
    #print(seq)
    n = len(seq)
    if n <=1:
        return seq
    pivot_value = seq[0]
    lesser = [item for item in seq[1:] if item <= pivot_value ]
    greater = [item for item in seq[1:] if item >= pivot_value]
    print("Sorted",quick_sort(lesser) + [pivot_value] + quick_sort(greater))
    return quick_sort(lesser) + [pivot_value] + quick_sort(greater)

if __name__ == '__main__':
    seq = list(range(10))
    random.shuffle(seq)
    print("Before:",seq)
    #insertion_sort(seq)
    L = quick_sort(seq)
    print('After:',L)
