#############################################
# GUI Tkinter Calculator By: Finn Lestrange #
#############################################

# Importing Tkinter and Math Library #

from tkinter import *
from math import *

# Making the window#
window = Tk();
window.title('Calculator');
window.resizable(0, 0);                 # Makes the window not resizable #

 
# Variables # 
total = ''
problemnew = StringVar()                # StringVar() is needed to create a Tkinter variable, this is called a constructor #
problem = ''

# Defining Functions for the buttons #
 
def buttonpress(press):                 # Takes the value of the button pressed and assignes it to variable 'press' #
    global problem, problemnew          # Declaring the global variables, 'problem' and 'problemnew' #
    problem = problem + str(press)      # Makes 'problem' = to problem + whatever button was pressed #
    problemnew.set(problem)             # Sets the entry 'box' to the value of 'problem' #
 
def enter():
    global problem, problemnew, total   # Declaring the global variables, 'problem' and 'problemnew' # 
    total = str(eval(problem))          # Sets 'total' to a string using eval which allows python to run functions inside itself #
    problemnew.set(total)               # Sets the entry box to total #
    problem = ""                        # Clears the current value of 'problem' #

def clear2():
    global problem, problemnew          # Declaring the global variables, 'problem' and 'problemnew' #
    problem = ''                        # Clears the current equation #
    problemnew.set("")                  # Clears the entry box #

def squareroot():
    global problemnew                   # Declaring the global variable 'problemnew' #
    sqrt = float(box.get())**.5         # Takes the square root of the number in the entry box #
    problemnew.set(sqrt)                # Sets the entry box to the square root of the number enterd #

def square():
    global problemnew                   # Declaring the global variable 'problemnew' #
    square = float(box.get())**2        # Squares the number currently in the entery box #
    problemnew.set(square)              # Sets the entry box to the square of the number entered #

def memoryplus():
    global problemnew, memoryadd        # Declaring global variables 'problemnew' and 'memoryadd' #
    memoryadd = problemnew.get()        # Setting 'memoryadd' to the number in the box #

def memoryget():
    global problemnew, memoryadd        # Declaring global variables 'problemnew' and 'memoryadd' #
    problemnew.set(memoryadd)           # Setting the entry box to the value of the variable 'memoryadd' #

def memoryclear():
    global memoryadd                    # Declaring global variable 'memoryadd' #
    memoryadd = ''                      # Setting 'memoryadd' to a blank string to clear the current value #
    
    
    
# Creating the elements, buttons, entry box, etc. #

box = Entry(window, textvariable=problemnew); 
clear = Button(window, text='CE', command=clear2 );
zero = Button(window, text='0', command=lambda: buttonpress('0') );
one = Button(window, text='1', command=lambda: buttonpress('1') );
two = Button(window, text='2', command=lambda: buttonpress('2') );
three = Button(window, text='3', command=lambda: buttonpress('3') );
four = Button(window, text='4', command=lambda: buttonpress('4') );
five = Button(window, text='5', command=lambda: buttonpress('5') );
six = Button(window, text='6', command=lambda: buttonpress('6') );
seven = Button(window, text='7', command=lambda: buttonpress('7') );
eight = Button(window, text='8', command=lambda: buttonpress('8') );
nine = Button(window, text='9', command=lambda: buttonpress('9') );
divide = Button(window, text='/', command=lambda: buttonpress('/') );
multiply = Button(window, text='*', command=lambda: buttonpress('*') );
subtract = Button(window, text='-', command=lambda: buttonpress('-') );
add = Button(window, text='+', command=lambda: buttonpress('+') );
decimal = Button(window, text='.', command=lambda: buttonpress('.') );
pi = Button(window, text='π', command= lambda: buttonpress('3.14159265359'));
sqrtbutton = Button(window, text='√', command=squareroot);
squarebutton = Button(window, text="x²", command=square);
memoryplusbutton = Button(window, text='M+', command=memoryplus);
memorygetbutton = Button(window, text='M', command=memoryget);
memoryclearbutton = Button(window, text='MC', command=memoryclear);
enter = Button(window, text='Enter', command=enter );

# Drawing the Elements using a grid #

box.grid(row=0, column=1)
clear.grid(row=0, column=4);
zero.grid(row=4, column=0);
one.grid(row=1, column=0);
two.grid(row=1, column=1);
three.grid(row=1, column=2);
four.grid(row=2, column=0);
five.grid(row=2, column=1);
six.grid(row=2, column=2);
seven.grid(row=3, column=0);
eight.grid(row=3, column=1);
nine.grid(row=3, column=2);
divide.grid(row=0, column=3);
multiply.grid(row=1, column=3);
subtract.grid(row=2, column=3);
add.grid(row=3, column=3);
decimal.grid(row=4, column=1);
pi.grid(row=1, column=4);
sqrtbutton.grid(row=2, column=4);
squarebutton.grid(row=3, column=4);
memoryplusbutton.grid(row=1, column=5);
memorygetbutton.grid(row=2, column=5);
memoryclearbutton.grid(row=3, column=5);
enter.grid(row=5, column=3);

clear2()
    





        
        
    

    

    
    
    

