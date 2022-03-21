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