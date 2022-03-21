import time 

ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def flame_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 35)


# print ship with colors and leading spaces
def candle_print(position):
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
def candle():
    # only need to print ocean once
    flame_print()

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate ship sailing
    for position in range(start, distance, step):
        candle_print(position)  # call to function with parameter
        time.sleep(.1)

if __name__=='__main__':
    # print_menu1()
    candle()