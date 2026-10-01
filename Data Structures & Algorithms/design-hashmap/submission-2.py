#create the nodes for the linked list
class Node():
    def __init__(self, key = -1, value = -1, next = None):
        self.value = value
        self.key = key
        self.next = next



class MyHashMap:
    #make a hashing function that returns the index to place the key values


    def hash(self, key):
        index = key % len(self.map)
        return index


    def __init__(self):
    #create a hashmap of size 1000 then place a dummy node at the start of it
        self.map = []
        for i in range(1000):
            self.map.append(Node())


    def put(self, key: int, value: int) -> None:
        #we just put a random node anywhere we want
        #so we need to put a ptr at the index where we want to insert the key.values
        index = self.hash(key) #find the current index from our key
        curr = self.map[self.hash(key)] #this will be on the dummy node, because when we do arr[index] we start on the 0th spot and because the array is empty when we map it curr is on the 0th node which is the dummy node. 
        while curr.next != None: #check the node in front of us
            if curr.next.key == key:    
                #override the value
                curr.next.value = value
                return 
            #then if its not in the linked list then just move the ptr
            curr = curr.next
            #add another node to prepare
        #if we hit NULL, we can insert a new Node at the end
        curr.next = Node(key, value)
    def get(self, key: int) -> int:
        index = self.hash(key)
        #get the value of a node, we just need access to the node behind of one we want to get the value of. start at the node ahead of dummy node again,
        curr = self.map[index].next 
        while curr != None:
            if curr.key == key: #then just return that value
                return curr.value
            #move the ptr
            curr = curr.next
        return -1
    def remove(self, key: int) -> None:
        index = self.hash(key)
        curr = self.map[index] #start at the dummy node, incase the first node we want to remove is the head
        #then the one we want to remove we must need access to the one behind it
        while curr and curr.next!= None:
            if curr.next.key == key:
                curr.next = curr.next.next #set the dangling pointer to the node after the one we want to remove.
                return
            curr = curr.next
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)