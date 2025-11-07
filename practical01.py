'''
Write a Python program to manage the borrowing records of books in a library. Implement
the following functionalities:
1. Compute the average number of books borrowed by all library members.
2. Find the book with the highest and lowest number of borrowings in the library.
3. Count the number of members who have not borrowed any books (denoted by a
borrow count of 0).
4. Display the most frequently borrowed book (i.e., the mode of borrow counts).
After performing, determine the time and Space complexity of each operation
'''
borrowlist = [5,0,3,5,2,0,3,5]

class library:
    def __init__(self , borrowlist):
        self.borrowlist = borrowlist

    # 1. to find avegare number of borrowing
    def findaverageborrow(self):
        total = 0
        for b in self.borrowlist:
            total += b
        avg = int(total/len(self.borrowlist))
        print("average borrow = {0}".format(avg)) # .format method
        return avg
    
    # 2. find book with highest and lowest borrowing
    def highlowborrowing(self):
        high = self.borrowlist[0]
        low = self.borrowlist[0]
        for count in self.borrowlist:
            if count < low:
                low = count
            if count > high:
                high = count
        print(f"hightest borrow count = {high}") # f-string method
        print(f"lowest borrow count = {low}")
    
    def notborrowedcount(self):
        notborrowed = self.borrowlist.count(0)
        print("not borrowed members count = %d" % notborrowed) # % operator method like used in c
        return notborrowed
    pass
        
l = library(borrowlist)
l.findaverageborrow()
l.highlowborrowing()
l.notborrowedcount()