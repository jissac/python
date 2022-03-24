from random import choice


class RandomizedSet:
    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        # print(self.list)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            # move the last element to the place idx of the element to delete
            last_element = self.list[-1]
            idx = self.dict[val]

            self.list[idx] = last_element
            self.dict[last_element] = idx

            # delete the last element
            # print(self.list)
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.list)


if __name__ == "__main__":
    nums = [
        "RandomizedSet",
        "insert",
        "remove",
        "insert",
        "getRandom",
        "remove",
        "insert",
        "getRandom",
    ]
    obj = RandomizedSet()
    param_1 = obj.insert(1)
    param_2 = obj.insert(2)
    param_3 = obj.remove(1)
    param_4 = obj.insert(3)
    print(param_1, param_2, param_3, param_4)

"""
# KEY INSIGHTS
- Hashmap provides Insert and Delete in average constant time, although has problems with GetRandom
- Array List has indexes and could provide Insert and GetRandom in average constant time, though has problems with Delete
- use the hashmap to store vale:index of the list
"""
