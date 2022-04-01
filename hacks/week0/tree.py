def create_tree(rows):
  for i in range(0, rows+1):
        for j in range(0, rows-i):
            print(end=' ')
        for k in range(0, i):
            print('*', end=' ')
        print()

def grow_tree():
  rows = int(input("Enter height of the tree:  "))
  create_tree(rows)
  spaces = lambda a: int(a-2) + a % 2
  moveRt = " " * spaces(rows)
  for i in range(3):
      print(moveRt, end="###")
      print()
