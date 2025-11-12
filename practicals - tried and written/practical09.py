'''
Design and implement a hash table of fixed size. Use the division method for the hash
function and resolve collisions using linear probing. Allow the user to perform the following
operations:
• Insert a key
• Search for a key
• Delete a key
• Display the table
'''
class HashTable:
    def __init__(self , size=10):
        self.size = size
        self.hashtable = [None]*size
        self.Deleted = "<Deleted>"
    
    def hashfunction(self , key):
        return key % self.size

    def insert(self , key):
        hashindex = self.hashfunction(key)
        originalhashindex = hashindex
        while self.hashtable[hashindex] not in (None , self.Deleted):
            if self.hashtable[hashindex] == key:
                print("key {0} already exist in table".format(key))
                return
            hashindex = (hashindex + 1) % self.size
            if hashindex == originalhashindex:
                print("Hash Table is full . cannot insert")
                return
        self.hashtable[hashindex] = key # inserted key after finding empty slot
        print(f" key {key} inserted successfully at index {hashindex}")

    def search(self , key):
        hashindex = self.hashfunction(key)
        originalhashindex = hashindex
        while self.hashtable[hashindex] is not None:
            if self.hashtable[hashindex] == key:
                print("key {0} exists at index {1}".format(key , hashindex))
                return hashindex
            hashindex = (hashindex + 1) % self.size # for linear probing
            if hashindex == originalhashindex:
                break
        print("key {0} does not exist in table".format(key))
        return None
    
    def delete(self , key):
        keypresentindex = self.search(key)
        if keypresentindex == None:
            print("Key does not exist for deleting")
        else:
            self.hashtable[keypresentindex] = self.Deleted
            print(f"key {key} deleted from index {keypresentindex}")
    
    def display(self):
        print("-----HashTable-----")
        for i , key in enumerate(self.hashtable):
            print("index {0} : {1},".format(i , key))




ht = HashTable(10)

ht.display()
ht.insert(1)
ht.insert(2)
ht.insert(3)
ht.insert(4)
ht.insert(10)
ht.insert(25)
ht.insert(36)
ht.insert(6)
ht.insert(12)
ht.display()

ht.delete(12)
ht.delete(11)
ht.delete(10)
ht.delete(25)
ht.display()
