def listDivisors (N):
    # initialization of the list of divisors  L = []
    L = []
    # We browse throught the integers: 1 2 3 ... N
    for i in range (1, N + 1):
        # we test if the integer i is a divisor of N and we add it to the list of divisors L
        if N% i == 0:
            L. append (i)
    return L
# We test the algorithm
print ("The list of divisors of 18 is :", listDivisors (18))
# Displays: The list of divisors of 18 is : [1, 2, 3, 6, 9, 18]

from tkinter import *
 
# method that performs the action
def action ():
    
    # retrieve the value of the edit control
    N = int (entryNumber1.get ())
    lblDivisors ['text'] = 'The  divisors  of  N    :    '
    
    # find the divisors s of n by going through all the integers from 1 to n
    for i in range (1, N + 1):
        if ( N%i == 0 ):
            lblDivisors ['text'] = lblDivisors ['text'] + "   " + str(i) + "   "

# Creation of the main window
fen = Tk ()
fen.geometry ("400x175")

# input field for the integer N with the associated label
lblnumber1 = Label (fen, text = "Enter the value of N")
lblnumber1.place (x = 10, y = 20)
entryNumber1 = Entry (fen)
entryNumber1.place (x = 200, y = 20)

# Label which gets the result
lblDivisors = Label (fen, text = "The divisors of N : ")
lblDivisors.place (x = 10, y = 50)

# validation button
Validate = Button (fen, text = "Validate", width = 20, command = action)
Validate.place (x = 200, y = 90)

fen.mainloop ()
