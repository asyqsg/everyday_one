from collections import defaultdict
import random
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = defaultdict(set) #{{}}
        self.data = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.table[val].add(len(self.data))
        self.data.append(val)
        return len(self.table[val]) == 1


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.table[val]:
            return False
        self.data[(i := self.table[val].pop())] = self.data[-1]
        self.table[(last := self.data.pop())].discard(len(self.data))
        i < len(self.data) and self.table[last].add(i)
        return True



    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.data)

