class MultiListIterator:
    def __init__(self, list1, list2):
        self.lists = [list1, list2]
        self.list_index = 0
        self.item_index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.list_index >= len(self.lists):
            raise StopIteration
        if self.item_index >= len(self.lists[self.list_index]):
            self.list_index += 1
            self.item_index = 0
            return self.__next__()
        item = self.lists[self.list_index][self.item_index]
        self.item_index += 1
        return item

print("\nMulti-List Iterator:")
for item in MultiListIterator([1, 2], ['a', 'b', 'c']):
    print(item)