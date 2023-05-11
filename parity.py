
#calculating parity with modulo
    
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

#function calculates if argument is even    
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
   #IMPORTANT: BOOLEAN VALUES HAVE TO BE WRITTEN WITH UPPER CASE


main()
