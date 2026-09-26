class MyHashSet:

    def __init__(self):
        self.hashset = [False] * 1_000_001

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashset[key] = True

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashset[key] = False

    def contains(self, key: int) -> bool:
        if self.hashset[key] == True:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)