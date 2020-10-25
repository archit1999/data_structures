parent = lambda i: (i+1)//2 - 1
left_child = lambda i: 2*(i+1) - 1
right_child = lambda i: 2*(i+1)


def shift_up(a, i, func):                 # max_heap

    if i > 0 and func(a[i], a[parent(i)]) == a[i]:
        a[parent(i)], a[i] = a[i], a[parent(i)]
        shift_up(a, a[parent[i]], func)


def shift_down(a, i, n, func):
    req_index = i

    if left_child(i) < n and func(a[left_child(i)], a[req_index]) == a[left_child(i)]:
        req_index = left_child(i)

    if right_child(i) < n and func(a[right_child(i)], a[req_index]) == a[right_child(i)]:
        req_index = right_child(i)

    if i != req_index:
        a[i], a[req_index] = a[req_index], a[i]
        shift_down(a, req_index, n, func)


def build_heap(a, n, func):
    for i in range(n//2, 0, -1):
        shift_down(a, i-1, n, func)


def extract_max(a, n, func):
    a[0], a[-1] = a[-1], a[0]           # put the top element to the last place
    temp = a[-1]                        # get this element in temp
    del a[-1]                           # del this element from array
    n -= 1                              # dec size of array
    shift_down(a, 0, n, func)           # the top element now has small element coz swapped above thus shift_down it
    return temp, n


n = 8                           # int(input())
a = [4, 7, 2, 3, 1, 5, 8, 6]    # list(map(int, input().split()))
build_heap(a, n, min)           # pass either max/ min function for the required heap or a customized funciton for any object can also be used

x, n = extract_max(a, n, min)
print(x)
print(a)
