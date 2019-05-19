import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)

class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return "Item({})".format(self.name)

q = PriorityQueue()
list = [1,2,3,4,5]
# for i in list:
#     q.push(i,)
q.push(Item('foo'),1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'),1)

print q._queue

q.pop()
print q._queue

q.pop()
print q._queue

q.pop()
print q._queue

# a = (1,"name")
# b = (2,"age")
# print a<b
# print a[1]