'''
Implement a real-time event processing system using a Queue data structure. The system
should support the following features:
• Add an Event: When a new event occurs, it should be added to the event queue.
• Process the Next Event: The system should process and remove the event that has
  been in the queue the longest.
• Display Pending Events: Show all the events currently waiting to be processed.
• Cancel an Event: An event can be canceled if it has not been processed.
'''
from collections import deque

class EventProcessingSystem:
    def __init__(self):
        self.events = deque()
    
    def addEvent(self,event):
        self.events.append(event)
        print("Event added successfully")
    
    def processEvent(self):
        if not self.events:
            print("No events available to process")
        else:
            event = self.events.popleft()
            print(f"Event \"{event}\" Processed successfully")
    
    def displayPending(self):
        if not self.events:
            print("No pending Events")
            print("Pending events = ",list(self.events))
        else:
            print("Pending events = ",list(self.events))
    
    def cancelEvent(self , event):
        if event in self.events:
            self.events.remove(event)
            print(f"Event {event} cancelled successfully")
        else:
            print(f" Event {event} not found")

# Menu driven program-----------------------------------------
ev = EventProcessingSystem()
while(True):
    print("-------------------------------------")
    print("1. Add Event")
    print("2. Process next Event")
    print("3. display pending Events")
    print("4. Cancel Event")
    print("5. exit")
    choice = input("Enter number = ")
    if choice == '1':
        event = input("Enter event name ")
        ev.addEvent(event)
    elif choice == '2':
        ev.processEvent()
    elif choice == '3':
        ev.displayPending()
    elif choice == '4':
        event = input("Enter event to cancel ")
        ev.cancelEvent(event)
    elif choice == '5':
        break
    else:
        print("Please Enter valid input")

