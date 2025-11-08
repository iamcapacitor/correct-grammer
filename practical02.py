'''
In an e-commerce system, customer account IDs are stored in a list, and you are tasked with
writing a program that implements the following:
• Linear Search: Check if a particular customer account ID exists in the list.
• Binary Search: Implement Binary search to find if a customer account ID exists,
improving the search efficiency over the basic linear
'''
customer_id = [102,205,150,123,301,110,175]
sorted_id =   [102,110,123,150,175,205,301]

class searching:
    def linearsearch(self,list , target):
        for i in range(0,len(list)):
            if (list[i] == target):
                print(target , "found using linear search at index =", i)
                return i
        print(target , " Not found using linear search")
        return -1 # element not found
    
    def binarysearch(self , sortedlist , target):
        low = 0
        high = len(sortedlist) -1
        while(low < high):
            mid = int((low + high)/2)
            if(sortedlist[mid] == target):
                print(target , "found using binary search at index =", mid)
                return mid
            elif(target < sortedlist[mid]):
                high = mid-1
            elif(target > sortedlist[mid]):
                low = mid+1
        print(target , " Not found using binary search")                
        return -1

    
s = searching()
s.linearsearch(customer_id , 110)
s.binarysearch(sorted_id , 1500)