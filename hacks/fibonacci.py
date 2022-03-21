#basic recursion and implimentation of fibonacci pattern
def recur_fibonacci(n):
  if n<=1:
    return n
  else:
    return(recur_fibonacci(n-1) + recur_fibonacci(n-2))

def tester():
  try:
    nterms = int(input("Number of Terms? "))
    if nterms <= 0:
      print("please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(nterms):
          print(recur_fibonacci(i))
  except ValueError:
    print(f"Not a number:{nterms}")