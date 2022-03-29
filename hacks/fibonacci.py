#basic recursion and implimentation of fibonacci pattern
def recur_fibonacci(n):
  if n<=1:
    return n
  else:
    return(recur_fibonacci(n-1) + recur_fibonacci(n-2))
# recursive function
    
def tester():
  try:
    nterms = int(input("Number of Terms? "))
    if nterms <= 0: #only prints postive terms
      print("please enter a positive integer")
    else: #goes through each term and prints recursively
        print("Fibonacci sequence:")
        for i in range(nterms):
          print(recur_fibonacci(i))
  except ValueError: #error message
    print(f"Not a number:{nterms}")