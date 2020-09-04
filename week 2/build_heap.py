def down(i, pair, tree, n):
    min_index = i
    l = 2 * i + 1
    if l >= n:
        return
    if tree[l] < tree[min_index]:
        min_index = l
    r = 2 * i + 2
    if r >= n:
        hi = float('inf')
    else:
        hi = tree[r]
    if hi < tree[min_index]:
        min_index = r
    if i != min_index:
        pair.append((i, min_index))
        tree[i], tree[min_index] = tree[min_index], tree[i]
        down(min_index, pair, tree, n)


def build_heap(tree, n):
    pair = []
    for i in reversed(range(n // 2)):
        down(i, pair, tree, n)
    return pair


def main():
    n = int(input())
    tree = list(map(int, input().split()))
    swaps = build_heap(tree, n)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
