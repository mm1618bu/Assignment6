def sumDigits(num):  # define the inital function
    if(num <= 9):   # if the number entered is less then 9, return the program
        return num
    else:
        return (num%10) + sumDigits(num//10) # run the program

def main():
    n = eval(input("Enter an integer: ")) # get input
    print("The sum of digits in",n,"is",sumDigits(n)) # prints the sum of all of the digits in the input

main()
