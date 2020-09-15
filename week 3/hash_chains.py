class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.num = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.m = bucket_count
        # store all strings in one list
        self.table = [[] for _ in range(10 ** 5)]
        self.elems = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.m

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == 'check':
            if len(self.table[query.num]) != 0:
                self.elems.append(' '.join(reversed(self.table[query.num])))
            else:
                self.elems.append(' ')
            return
        ha = self._hash_func(query.s)
        if query.type == 'add':
            if query.s not in self.table[ha]:
                self.table[ha].append(query.s)
        elif query.type == 'del':
            if query.s in self.table[ha]:
                index = self.table[ha].index(query.s)
                self.table[ha].pop(index)
        else:
            self.elems.append('yes' if query.s in self.table[ha] else 'no')
        """
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.num)
        else:
            try:
                num = self.elems.index(query.s)
            except ValueError:
                num = -1
            if query.type == 'find':
                self.write_search_result(num != -1)
            elif query.type == 'add':
                if num == -1:
                    self.elems.append(query.s)
            else:
                if num != -1:
                    self.elems.pop(num)
        """
    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())
        print('\n'.join(self.elems))

if __name__ == '__main__':
    m = int(input())
    proc = QueryProcessor(m)
    proc.process_queries()
