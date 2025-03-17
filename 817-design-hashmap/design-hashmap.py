# Using Dictionary
# class MyHashMap:

#     def __init__(self):
#         self.hashmap = {}

#     def put(self, key: int, value: int) -> None:
#         self.hashmap[key] = value
        

#     def get(self, key: int) -> int:
#         if key in self.hashmap:
#             return self.hashmap[key]
#         else:
#             return -1
        

#     def remove(self, key: int) -> None:
#         if key in self.hashmap:
#             del self.hashmap[key]


class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        isKey = False
        if len(self.hashmap) == 0:
            self.hashmap.append([key, value])
        for i in range(len(self.hashmap)):
            if key == self.hashmap[i][0]:
                self.hashmap[i][1] = value
                isKey = True
                return
        if not isKey:
            self.hashmap.append([key, value])
        # print(self.hashmap)
    def get(self, key: int) -> int:
        for i in range(len(self.hashmap)):
            if key == self.hashmap[i][0]:
                return self.hashmap[i][1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.hashmap)):
            if key == self.hashmap[i][0]:
                self.hashmap.remove(self.hashmap[i])
                return

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)