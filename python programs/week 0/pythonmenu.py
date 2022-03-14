import time

"""
Introduction to Console Programming
Writing a function to print a menu
"""
#start adding menu
number1 = 0
number2 = 0
# Menu options in print statement
def print_menu1():
    print('1 -- Swap' )
    print('2 -- Matrix' )
    print('3 -- Animation' )
    print('4 -- Exit' )

    runOptions()


# Menu options as a dictionary
menu_options = {
    1: 'Swap',
    2: 'Matrix',
    3: 'Animation',
    4: 'Exit',

}

# Print menu options from dictionary key/value pair



def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()

def matrix():
    matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
    for row in matrix:
        for col in row:
            print(col, end= "")
        print()

def swapnumbers(a, b):
    temp = a
    a = b
    b = temp
    print("After Swapping two Numbers",(a, b))
    number1 = int(input("first number: "))
    number2 = int(input(" second number: "))
    print("Before Swapping",(number1, number2))

    # making sure that the inputs stay in order
    if number1 > number2:
        swapnumbers(number1, number2)
    else:
        print("After Swapping",(number1, number2))

# code that calls the function to swap
# used input so that users can play around with numbers and see how swaps + keeps in order

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def ocean_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 35)


# print ship with colors and leading spaces
def ship_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "---()---")
    print(sp + "--[  ]--")
    print(SHIP_COLOR, end="")
    print(sp + "--[  ]--")
    print(sp + "--[__]--")
    print(RESET_COLOR)


# ship function, iterface into this file
def ship():
    # only need to print ocean once
    ocean_print()

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate ship sailing
    for position in range(start, distance, step):
        ship_print(position)  # call to function with parameter
        time.sleep(.1)

# menu option 1


# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    global number1
    global number2
    while True:
        try:
            option = int(input('Enter your choice 1-4: '))
            if option == 1:
                swapnumbers()
            elif option == 2:
                matrix()
            elif option == 3:
                ship()
            elif option == 4:
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 5.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    # print_menu1()
    print_menu2()