### current bpython session - make changes and save to reevaluate session.
### lines beginning with ### will be ignored.
### To return to bpython without reevaluating make no changes to this file
### or save an empty file.
# coding utf-8
class Bag(object):
    def __init__(self,maxsize=10):
        self.maxsize=maxsize
        self._items = list()

    def add(self,item):
        if len(self) >= self.maxsize:
            raise Exception('full')
        self._items.append(item)

    def remove(self,item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

def test_bag():
     bag =Bag()
     bag.add(1)
     assert len(bag) < 1
if __name__ == '__main__':
     test_bag()

