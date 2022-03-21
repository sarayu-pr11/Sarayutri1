InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Sarayu",  
               "LastName": "Pochimireddy",  
               "DOB": "November 10",  
               "Grade": "11",  
               "Email": "sarayu.pr11@gmail.com",  
               "Class":["APCSP", "APCalcBC", "APEL", "APUSH", "Ceramics"]  
              })  

InfoDb.append({  
               "FirstName": "Lola",  
               "LastName": "Smith",  
               "DOB": "August 2",  
               "Grade": "10",  
               "Email": "lolasmith@gmail.com",  
               "Class":["APEC", "APCalcAB", "APChem", "Honors Principles of Engineering", "Spanish 7"]  
              })  

InfoDb.append({  
               "FirstName": "John",  
               "LastName": "Doe",  
               "DOB": "March 7",  
               "Grade": "12",  
               "Email": "johndoe@gmail.com",  
               "Class":["APStats", "APPhysics", "APCSA", "APLit", "Ceramics 2"]  
              })  


# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["Email"])  # 
    print("\t", "Class: ", end="")
    print(", ".join(InfoDb[n]["Class"]))
    print()


def lists_tester():
    print("||    For loop   ||")
    for_loop()
    print("||   While loop   ||")
    while_loop(0)
    print("||   Recursive loop   ||")
    recursive_loop(0)

  
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

if __name__ == '__main__':
    # print_menu1()
    tester()