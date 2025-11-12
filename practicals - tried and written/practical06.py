'''
A call center receives incoming calls, and each call is assigned a unique customer ID. The
calls are answered in the order they are received. Your task is to simulate the call queue of a
call center using a queue data structure.
• addCall(customerID, callTime): Add a call to the queue with the customer ID and the call time (in minutes).
• answerCall(): Answer and remove the first call from the queue.
• viewQueue(): View all calls currently in the queue without removing them.
• isQueueEmpty(): Check if the queue is empty.
'''
from collections import deque
class callcenter:
    def __init__(self):
        self.q = deque([])

    def addCall(self , customerId, callTime):
        obj = {"customerId":customerId , "callTime" : f"{callTime} m"}
        self.q.append(obj)
        print(f"call with id {obj['customerId']} added successfully in queue")
    
    def answerCall(self):
        if self.q:
            obj = self.q.popleft()
            print(f"Call with id {obj['customerId']} has been answered , waited for {obj['callTime']}")
        else:
            print("No calls Available to Answer")
        
    def viewQueue(self):
        if self.q:
            print("Pending calls in queue------------------------------")
            for obj in self.q:
                print(obj)
            print("------------------------------------")
        else:
            print("Queue is empty")
    
    def isQueueEmpty(self):
        if self.q:
            print("Queue is not Empty")
        else:
            print("Queue is Empty")
    
# Making menu to drive the code---------------------------------------
if __name__ == "__main__":
    callc = callcenter()
    while(True):
        print("---Call center Queue---")
        print("1. Add call")
        print("2. Answer next call")
        print("3. View Call queue")
        print("4. Check if queue is empty")
        print("5. Exit")
        option = input("Enter number =")
        if option == '1':
            id = input("Enter customer id =")
            ct = input("Enter calltime in minutes =")
            callc.addCall(id , ct)
        elif option == '2':
            callc.answerCall()
        elif option == '3':
            callc.viewQueue()
        elif option == '4':
            callc.isQueueEmpty()
        elif option == '5':
            break
        else:
            print("Please Enter valid number")
