from tkinter import *

# create action methode 
def action ():
    # retrieve the value of the first and second input field
    M = int (entryNumber1.get ())
    N = int (entryNumber2.get ())    
    
    S = M + N
    # display the sum in label result
    lblResult['text'] = "The Sum is : " + str(M)  + " + " +  str(N) +"  = " + str(S)
  
# creation of the main window
root = Tk ()
root.geometry ("400x175")

# Creation of the first edit control with the associated label
lblnumber1 = Label (root, text = "Enter the value of M :")
lblnumber1.place (x = 50, y = 20)
entryNumber1 = Entry (root)
entryNumber1.place (x = 200, y = 20)

# Creation of the 2nd input field with the associated label
lblnumber2 = Label (root, text = "Enter the value of N :")
lblnumber2.place (x = 50, y = 50)
entryNumber2 = Entry (root)
entryNumber2.place (x = 200, y = 50)

# Create a label to display result
lblResult = Label(root)
lblResult.place(x = 200 , y = 80)

# Creation of button that validates the action
Validate = Button (root, text = "Validate", command = action)
Validate.place (x = 200, y = 120, width = 165)
                
root.mainloop ()
