import heapq

class PQ:
  def __init__(self):
      self._queue = []
      self._index = 0
  def push(self, item, priority):
      heapq.heappush(self._queue, (-priority, self._index, item))
      self._index += 1
  def pop(self):
      return heapq.heappop(self._queue)[-1]

class Item:
      def __init__(self, name):
           self.name = name
      def __repr__(self):
           return 'Item({!r})'.format(self.name)

q = PQ()
q.push(Item('test'), 1)
q.push(Item('bar'), 5)
q.push(Item('foo'), 4)
q.push(Item('car'), 1)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
