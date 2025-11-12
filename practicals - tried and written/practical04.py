'''
Implementing a real-time undo/redo system for a text editing application using a Stack data
structure. The system should support the following operations:
• Make a Change: A new change to the document is made.
• Undo Action: Revert the most recent change and store it for potential redo.
• Redo Action: Reapply the most recently undone action.
• Display Document State: Show the current state of the document after undoing or
redoing an action
'''

class TextEditor:
    def __init__(self):
        self.document = ""
        self.undo_stack = []
        self.redo_stack = []
    
    # make new change
    def makechange(self , text):
        self.undo_stack.append(self.document)
        self.document += text
        self.redo_stack.clear()
        print("changes made ", text)
    
    def undo(self):
        if not self.undo_stack:
            print("Cannot undo ! undo stack is empty")
        else:
            data = self.undo_stack.pop()
            self.redo_stack.append(self.document)
            self.document = data
            print("Undo performed")
    
    def redo(self):
        if not self.redo_stack:
            print("No change availabe to redo")
        else:
            data = self.redo_stack.pop()
            self.undo_stack.append(self.document)
            self.document = data
            print("Redo performed")
    
    def displaydocument(self):
        print("Current document = ",self.document)

te = TextEditor()
te.makechange("Namaste ")
te.displaydocument()

te.makechange("Bharat ")
te.displaydocument()

te.undo()
te.displaydocument()

te.redo()
te.displaydocument()
