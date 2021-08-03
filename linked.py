class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,newNode):
        #head => John->None
        if self.head is None:
            self.head = newNode
        else:
            #head=>John->ben->None
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode


    def printlist(self):
        #head=>john->ben->mattew->None
        if self.head == None:
            print("list is empty")
            return
        currentNode = self.head
        while currentNode!=None:
            print(currentNode.data,end = " ")
            currentNode = currentNode.next
