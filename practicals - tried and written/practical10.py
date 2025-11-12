'''
Implement a hash table with extendible hashing. The hash table should dynamically expand
when the number of keys in a bucket exceeds a certain threshold.
Perform the following operations:
• Insert(key): Insert key-value pairs into the hash table
• Search(key): Search for the value associated with a given key
• Delete(key): Delete a key-value pair from the hash table
'''
# class Bucket:
#     def __init__(self , depth , size):
#         self.depth = depth
#         self.size = size
#         self.items = {} # dictionary for storing key-value pairs

#     def isFull(self):
#         return len(self.items) >= self.size
    
#     def insert(self, key , value):
#         self.items[key] = value

#     def delete(self , key):
#         if key in self.items:
#             del self.items[key]
    
#     def search(self , key):
#         return self.items.get(key , None)
    
# class ExtendibleHashTable:
#     def __init__(self , bucketsize = 2):
#         self.globaldepth = 1
#         self.bucketsize = bucketsize
#         self.directory = [Bucket(self.globaldepth , self.bucketsize) for _ in range(2)]
    
#     def insert(self , key , value):
