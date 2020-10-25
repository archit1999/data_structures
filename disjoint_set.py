# disjoint set based on given graph for finding the connected vertices
# author - Archit K Mishra


def find_parent(u, parent):                             # find top most parent of the given vertex
    while parent[u] != u:
        u = parent[u]
    return u


def merge(u, v, parent, rank):                          # add two roots of the tree into a single tree
    if u == v:
        return
    if rank[u] < rank[v]:
        parent[u] = v
    if rank[v] < rank[u]:
        parent[v] = u
    if rank[v] == rank[u]:
        parent[u] = v
        rank[v] += 1


def enter_edge(u, v, parent, rank):                     # add given vertex wrt to edge to suitable sets
    merge(find_parent(u, parent), find_parent(v, parent), parent, rank)


v, edges = map(int, input().split())                    # no. of vertices and edges
parent = [i for i in range(v)]                          # parent of ith vertex zero indexed
rank = [1 for i in range(v)]                            # height of ith vertex zero indexed

for i in range(edges):
    u, v = map(int, input().split())
    enter_edge(u-1, v-1, parent, rank)

# print(parent, rank)
