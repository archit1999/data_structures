parent = lambda i: (i+1)//2 - 1
left_child = lambda i: 2*(i+1) -1
right_child = lambda i: 2*(i+1)
cmp = 0


def shift_up(a, i):                 # max_heap
    if i > 0 and a[i] > a[parent(i)]:
        a[parent(i)], a[i] = a[i], a[parent(i)]
        shift_up(a, a[parent[i]])


def shift_down(a, i, n):
    global cmp
    max_index = i

    if left_child(i) < n and a[left_child(i)] > a[max_index]:
        cmp += 1
        max_index = left_child(i)

    if right_child(i) < n and a[right_child(i)] > a[max_index]:
        cmp += 1
        max_index = right_child(i)

    if i != max_index:
        a[i], a[max_index] = a[max_index], a[i]
        shift_down(a, max_index, n)


def build_heap(a, n):
    for i in range(n//2, 0, -1):
        shift_down(a, i-1, n)


def extract_max(a, n):
    a[0], a[-1] = a[-1], a[0]
    temp = a[-1]
    del a[-1]
    n -= 1
    shift_down(a, 0, n)
    return temp, n


n = 8                           # int(input())
a = [4, 7, 2, 3, 1, 5, 8, 6]    # list(map(int, input().split()))
print(a)
build_heap(a, n)
for i in range(2):
    x, n = extract_max(a, n)
print(x, cmp)
print(a)
