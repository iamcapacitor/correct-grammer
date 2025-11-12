'''
Create a Student Record Management System using linked list
• Use a singly/doubly linked list to store student data (Roll No, Name, Marks).
• Perform operations: Add, Delete, Update, Search, and Sort.
• Display records in ascending/descending order based on marks or roll number
'''
class studentnode:
    def __init__(self , rollno , name , marks ):
        self.rollno = rollno
        self.name = name
        self.marks = marks
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addstudent(self , rollno , name , marks):
        newstudent = studentnode(rollno , name , marks)
        if self.head == None:
            self.head = newstudent
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newstudent
        print("Student Recored added successfully!")
    
    def deletestudent(self , rollno):
        current = self.head
        prev = None 
        while current:
            if current.rollno == rollno:
                if prev:
                    prev.next = current.next # handles and between node deletion case
                else:
                    self.head = current.next # handles head deletion case
                print(f"Student with roll no ={rollno} deleted")
                return
            prev = current
            current = current.next
        print(f"Student with rollno = {rollno} not found")

    def updatestudent(self , rollno , newname , newmarks):
        current = self.head
        while current:
            if current.rollno == rollno:
                current.name = newname
                current.marks = newmarks
                print("Student details updated successfully")
                return
            current = current.next
        print("Student not found for updation")
    
    def searchstudent(self , rollno):
        current = self.head
        while current:
            if current.rollno == rollno:
                print(f" Student with roll no = {rollno} found:")
                print(f"name = {current.name}\nrollno = {current.rollno}\nmarks={current.marks}")
                return
            current = current.next
        print("Student Not found")
    
    def displaystudents(self , sortby="rollno",ascending=True):
        students = []
        current = self.head
        while current:
            students.append((current.rollno , current.name , current.marks))
            current = current.next
        
        if sortby == "rollno":
            students.sort(key= lambda x :x[0], reverse= not ascending)
        elif sortby == "marks":
            students.sort(key= lambda x :x[2], reverse= not ascending)
        
        if not students:
            print("No record to display")
            return
        print("---------Student record------------")
        for s in students:
            print(f"Name : {s[1]} , Roll no : {s[0]} , Marks: {s[2]}")
        
# Menu driven program--------------------------------
if __name__ == "__main__":
    system = LinkedList()
    while True:
        print("\n------Student Record Management-------")
        print("1. Add student")
        print("2. delete student")
        print("3. update student")
        print("4. Search student")
        print("5. Display all student")
        print("6. Exit")
        choice = input("Enter choice = ")
        if choice == '1':
            name = input("Enter name :")
            rollno = int(input("Enter roll no :"))
            marks = int(input("Enter marks :"))
            system.addstudent(rollno ,name , marks)
        elif choice == '2':
            rollno = int(input("Enter roll no to delete :"))
            system.deletestudent(rollno)
        elif choice == '3':
            rollno = int(input("Enter roll no to update :"))
            newname = input("Enter new name :")
            newmarks = int(input("Enter new marks :"))
            system.updatestudent(rollno ,newname , newmarks)
        elif choice == '4':
            rollno = int(input("Enter roll-no to Search Student :"))
            system.searchstudent(rollno)
        elif choice == '5':
            sortby = input("Sort by (rollno / marks) :")
            ascending = bool(int(input("ascending order (1 or 0):")))
            system.displaystudents(sortby , ascending)
        elif choice == '6':
            print("Ok stopping system--------------------")
            break
        else:
            print("Please Enter valid number")
        

    



    
