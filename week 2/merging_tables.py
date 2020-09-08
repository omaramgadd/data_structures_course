class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts  # row counts of tables
        self.max_row_count = max(row_counts)  # wont need it later
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables  # ranks starting from 1
        self.parents = list(range(n_tables))  # parents list

    def merge(self, dst, src):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)
        rank = self.ranks
        p = self.parents
        row_count = self.row_counts
        if src_parent == dst_parent:
            return False

        if rank[src_parent] > rank[dst_parent]:
            p[dst_parent] = p[src_parent]
            rank[src_parent] += rank[dst_parent]
            row_count[src_parent] += row_count[dst_parent]
            if row_count[src_parent] > self.max_row_count:
                self.max_row_count = row_count[src_parent]
        else:
            p[src_parent] = p[dst_parent]
            rank[dst_parent] += rank[src_parent]
            row_count[dst_parent] += row_count[src_parent]
            if row_count[dst_parent] > self.max_row_count:
                self.max_row_count = row_count[dst_parent]
        return True

    def get_parent(self, i):
        p = self.parents
        while p[i] != i:
            p[i] = p[p[i]]  # Skip one level
            i = p[i]  # Move to the new level
        return self.parents[i]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    maxo = []
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        maxo.append(db.max_row_count)
    for i in range(n_queries):
        print(maxo[i])

if __name__ == "__main__":
    main()
