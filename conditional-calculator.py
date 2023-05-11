#harvard learn python course
#conditional calculator!

def main():
    type = int(input("Which calculator do you want to use? 1. ADDITION 2. SUBSTRACTION 3. SQUARE: "))
   
   #choose calculator function by integer input
   
    if type == 1:
        x = int(input("Define X: "))
        y = int(input("Define Y: "))
        
        print(addition(x, y))

    elif type == 2:
        x = int(input("Define X: "))
        y = int(input("Define Y: "))

        print(substraction(x, y))

    elif type == 3:
        x = int(input("Define X: "))
        
        print(square(x))
    
    else: print("invalid input!")


#define calculator functions
def square(n):
    return pow(n, 2)

def addition(x, y):
    return x + y

def substraction(x, y):
    return x - y



main()
