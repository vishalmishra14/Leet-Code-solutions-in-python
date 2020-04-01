class LRU:

    def __init__(self, N):
        self.N = N
        self.cache = []

    def get (self, keyc):
        value = 0
        for n in self.cache:
            if keyc != -1:
                if n[0] == keyc:
                    value = n[1]
                    self.cache.pop(self.cache.index(n))
                    break
                else:
                    return -1
            else:
                self.cache.pop(0)
        return value

    def set(self, value):
        if len(self.cache) == self.N:
            self.get(-1)
            self.cache.append(value)
        else:
            self.cache.append(value)
        return self.cache


if __name__ == '__main__':
    print("Please enter the number of test cases to run:")
    T = int(input())

    for _ in range(T):
        print("Please enter the size of the cache:")
        cache1 = int(input())
        lru = LRU(cache1)
        print("Please enter the number of queries to run: (q < 10000)")
        z = int(input())
        for _ in range(z):
            print("Please enter you query:")
            query = input().split(' ')
            if query[0].lower() == 'get':
                key = lru.get(query[1])
                print(f"Returned key {key}")
            else:
                s = lru.set([query[1], query[2]])
                print(s)

# Example:
# Input:
# 2 = T (Number of Test cases)
# 2 = N (Size of the cache)
# 2 = Q (Number of queries)
# SET 1 2 GET 1
# 2 = N (Size of the cache)
# 7 = Q (Number of queries)
# SET 1 2 SET 2 3 SET 1 5 SET 4 5 SET 6 7 GET 4 GET 1
# Output:
# 2
# 5 -1