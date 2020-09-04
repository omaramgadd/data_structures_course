import sys
import threading


def compute_height(n, parents):
    q = []
    levels = [None] * n
    max_height = 0
    root = parents.index(-1)  # index of -1
    q.append(root)  # add the index of -1
    levels[root] = 1
    while len(q) != 0:
        current = q.pop(0)  # index of first element in the list
        for index, child in enumerate(parents):
            if child == current:
                q.append(index)
                levels[index] = levels[current] + 1
                max_height = max(max_height, levels[index])
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()
