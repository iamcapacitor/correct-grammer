'''
Implement a hash table of size 10 and use the division method as a hash function. In case of
a collision, use chaining. Implement the following operations:
• Insert(key): Insert key-value pairs into the hash table.
• Search(key): Search for the value associated with a given key.
• Delete(key): Delete a key-value pair from the hash table

'''
class Hashtable:
    def __init__(self , size=10):
        self.size = size
        self.hashtable = [[] for _ in range(size)]
    
    def hashfunction(self , key):
        hashindex = key % self.size
        return hashindex
    
    def insert(self , key , value):
        hashindex = self.hashfunction(key)
        # check if key already exists and update
        for pair in self.hashtable[hashindex]:
            if pair[0] == key:
                pair[1] = value
                print(f"Updated key {key} with value {value}")
                return
        # Else insert new key-value pair
        self.hashtable[hashindex].append([key , value])
        print(f"Inserted key {key} with value {value}")
    
    def search(self , key):
        hashindex = self.hashfunction(key)
        for pair in self.hashtable[hashindex]:
            if pair[0] == key:
                return pair[1] # returning value
        print(f"Key-{key} Not found")
        return None
    def delete(self , key):
        hashindex = self.hashfunction(key)
        for i , pair in enumerate(self.hashtable[hashindex]):
            if pair[0] == key:
                del self.hashtable[hashindex][i]
                print(f"Successfully deleted key {key}")
                return
        print(f"Key {key} not found for deletion")
        
    def display(self):
        print("-----HashTable---------")
        for i, bucket in enumerate(self.hashtable):
            print(f"Index {i} = {bucket}")
        print("-----------------")

ht = Hashtable(10)

ht.display()
ht.insert(1,"apple")
ht.insert(2,"banana")
ht.insert(3,"cherry")
ht.insert(4,"guava")
ht.insert(5,"pineapple")
ht.insert(6,"litchi")
ht.insert(7,"mango")
ht.insert(8,"grapes")
ht.insert(10,"papaya")
ht.insert(20,"coconut")
ht.insert(30,"watermelon")

ht.display()

ht.search(20)

ht.delete(30)
ht.delete(5)
ht.display()

print(ht.search(6))
print(ht.search(20))
print(ht.search(10))
