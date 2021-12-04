def gcd(m, n): # define the GCD function taking in two arguments which is two different numbers
    if n==0: # if n isnt 0, proceed with the program
        return m
    else:
        return gcd(n, m % n)

def main(): # run the program
    print("Lets find the GCD of two numbers")
    m = eval(input("Enter the first number: ")) # get the first number
    n = eval(input("Enter the second number: ")) # get the second number
    print("The GCD of",m,"and",n,"is",gcd(m,n)) # print the result

main()
