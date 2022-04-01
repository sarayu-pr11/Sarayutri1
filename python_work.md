{% include navigation.html %}
## Python Weekly Work
## [Replit](https://replit.com/@sarayu-pr11/Sarayutri1#hacks/main.py)
<table>
  <tr>
    <td>Week</td>
    <td>Topic</td>
  </tr>
 </table>
 
 <table>
  <tr>
    <td>2</td>
    <td>Classes and OOP Programming</td>
    <td>
      <pre>
      <code>
      while True:
        factorial_of = Factorial()
      if n <=0:
                raise ValueError
      print(f"Factorial sequence of {n} terms is: ", [factorial_of(i) for i in range(n)])
       </code>
       </pre>
     </td>
      <td>
      <pre>
      <code>
      def __call__(self, n):
      for i in range (1, n + 1):
        if n % i == 0:
            self.factors.append(i)
       </code>
       </pre>
     </td>
  </tr>
 </table>
 <table>
  <tr>
    <td>1</td>
    <td>Lists and Loops </td>
    <td>
      <pre>
      <code>
      nterms = int(input("number of Terms? "))
    if nterms <= 0: 
      print("please enter a positive integer")
    else:
        print("fibonacci sequence:")
        for i in range(nterms):
          print(recur_fibonacci(i))
       </code>
       </pre>
     </td>
        <td>
      <pre>
      <code>
      def for_loop():
    for n in range(len(InfoDb)):
      </code>
      </pre>
    </td>
    <td>
      <pre>
      <code>
      while n < len(InfoDb):
        print_data(n)
        n += 1
      </code>
      </pre>
    </td>
    <td>
      <pre>
      <code>
      if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
      </code>
      </pre>
    </td>
      
  </tr>
 </table>
<iframe frameborder="0" width="100%" height="800px" src="https://replit.com/@sarayu-pr11/Sarayutri1?lite=true#hacks/main.py">
</iframe> <table>
  <tr>
    <td>0</td>
    <td>Python Menus</td>
        <td><pre>
 <code>
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
</code>
</pre>
    </td>
    <td>
      <pre>
      <code>
      if number1 > number2:
        swapnumbers(number1, number2)
    else:
        print("After Swapping",(number1, number2))
        </code>
        </pre>
    </td>
    <td>
      <pre>
      <code>
      rows = int(input("Enter height of the tree:  "))
      spaces = lambda a: int(a-2) + a % 2
      moveRt = " " * spaces(rows)
      </code>
      </pre>
    </td>
  </tr>
</table>
