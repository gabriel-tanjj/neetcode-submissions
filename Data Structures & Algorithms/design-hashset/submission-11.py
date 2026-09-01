class MyHashSet:

    def __init__(self):
        self.hash_set = [False] * (1_000_001)

    def add(self, key: int) -> None:
        self.hash_set[key] = True

    def remove(self, key: int) -> None:
        self.hash_set[key] = False

    def contains(self, key: int) -> bool:
        return self.hash_set[key]