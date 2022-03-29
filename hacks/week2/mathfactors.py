def findFactors (n):
    factors = []
    x = range (1, n + 1)
    for i in x:
        if (n % i == 0):
          #checks to see if each number in the list divides into the integer without a remainder
          factors.append(i)
          # updates the list with each factor that works
          print(i, end=' ')
    print(factors)
  # class method to create a function that factorizes an interger

class Factors:
    def __init__(self):
        self.factors = []
          #need to call self and intitalize an init variable in order for class to work

    def __call__(self, n):
      for i in range (1, n + 1):
        if n % i == 0:
            self.factors.append(i)
      return self.factors
      
factors_of = Factors() 
def testdata():
  factors(12)
  factors(100)
def testinput():
  while True:
      n = int(input("Integer to factor:"))
      try:
            n = int(n)
            if n <= 0:
                raise ValueError
            print("Factors of {0} is: ".format(n))
            print(factors_of(n))
      except ValueError:
            print(f'Positive integer number is expected, got "{n}" Try again.')

if __name__ == "__main__":
    testinput()
if __name__ == "__main__":
    testdata()