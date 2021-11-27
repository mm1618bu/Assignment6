def gcd(m, n):
    if n==0:
        return m
    else:
        return gcd(n, m % n)

def main():
    m = eval(input("Enter a number: "))
    n = eval(input("Enter a number: "))
    print("The GCD of",m,"and",n,"is",gcd(m,n))

main()
