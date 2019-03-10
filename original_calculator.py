#####################################
# GUI Calculator By: Finn Lestrange #
#####################################

# Importing Tkinter #

from tkinter import *

# Making the window#
window = Tk();
window.title('Calculator');
window.resizable(0, 0);

 
# Variables # 
total = ''
press = ''
problemnew = StringVar()

# Defining Functions #
 
def buttonpress(press):
    global problem, problemnew
    problemnew = problem.get() + str(press)
    problem.insert(END, press)
 
def enter():
    global problem, problemnew
    total = str(eval(problemnew))
    problemnew.set(total)
    problem = ""
 
def clear2():
    global problem, problemnew
    problem.insert(0,"")

    
# Creating the elements #

problem = Entry(window, textvariable=problemnew); 
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
pi = Button(window, text='π', command= lambda: buttonpress('3.14159265359'))
enter = Button(window, text='Enter', command=enter );

# Drawing the Elements #

problem.grid(row=0, column=1)
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
pi.grid(row=1, column=4)
enter.grid(row=5, column=3);

clear2()
    





        
        
    

    

    
    
    

