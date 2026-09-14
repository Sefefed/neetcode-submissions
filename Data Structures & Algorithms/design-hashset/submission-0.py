class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.table = [[] for i in range(self.size)]
    def add(self, key: int) -> None:
        bucket = key % self.size
        if key not in self.table[bucket]:
            self.table[bucket].append(key)
    def remove(self, key: int) -> None:
        bucket = key % self.size
        if key in self.table[bucket]:
            self.table[bucket].remove(key)
    def contains(self, key: int) -> bool:
        bucket = key % self.size
        return key in self.table[bucket]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)