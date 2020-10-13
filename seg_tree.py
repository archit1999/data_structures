# generalized segment tree for any function
# author:- Archit K Mishra

import math

"""
    functions:
        1)main
        2)create segment tree
        3)operation on which to make segment tree like addition of sub-array or min element
"""


def parent(i): return (i+1)//2 - 1              # 0 - based


def left_child(i): return 2*i + 1               # 0 - based


def right_child(i): return 2*i + 2              # 0 - based


def mid(seg_start, seg_end): return seg_start + (seg_end - seg_start) // 2


def op(a, b): return a + b


def create(s_tree, a, n, seg_curr, seg_start, seg_end, func):  # func is the operation on which seg_tree is to be formed

    if seg_start == seg_end:
        s_tree[seg_curr] = a[seg_start]
        return s_tree[seg_curr]

    else:
        s_tree[seg_curr] = func(create(s_tree, a, n, left_child(seg_curr), seg_start, mid(seg_start, seg_end), func),
                                create(s_tree, a, n, right_child(seg_curr), mid(seg_start, seg_end) + 1, seg_end, func))
        return s_tree[seg_curr]


arr_len = 7  # int(input())
arr = [6, 1, 5, 4, 5, 1, 6]        # list(map(int, input().split()))

ht = int(math.ceil(math.log2(arr_len)))         # ht of required tree
max_size = 2 * int(2 ** ht) - 1                 # size of the seg_tree

seg_tree = [0] * max_size
create(seg_tree, arr, len, 0, 0, arr_len-1, op)
print(arr)
print(seg_tree)
