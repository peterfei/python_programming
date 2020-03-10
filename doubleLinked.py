#codeing utf-8
class Node(object):
    def __init__(self,data,Next=None,Previous=None):
        self.data = data
        self.next = Next
        self.previous = Previous

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def getData(self):
        return self.data

    def setData(self,newData):
        self.data = newData


    def setNext(self,newNext):
        self.next = newNext

    def setPrevious(self,newPrevious):
        self.previous = newPrevious

class LinkedList(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head==None

    def insertFirst(self,data):
        newNode = Node(data)
        if self.head:
            self.head.setPrevious(newNode)
        newNode.setNext(self.head)
        self.head = newNode

    def insertLast(self,data):
        newNode = Node(data)
        current = self.head
        while current.getNext()!=None:
            current = current.getNext()
        current.setNext(newNode)
        current.setPrevious(current)

    def getAllData(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.getData())
            current = current.getNext()
        return elements


if __name__ == "__main__":
    myList = LinkedList()
    myList.insertFirst(1)
    myList.insertFirst(12)
    myList.insertFirst(32)
    myList.insertFirst(32)
    myList.insertFirst(32)
    myList.insertLast(2)
    print(myList.getAllData())
