def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

def fib(n):
    if n==1 or n==2:
        return n-1
    return fib(n-1)+fib(n-2)


def prime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
if __name__=='__main__':
    print(fib(5))
    print(prime(5))







def prime(n):
    if n<=1:
        return False
    for x in range(2,n//2+1):
        if n%x==0:
            return False
        return True
def fib(n):
    if n==1 or n==2:
        return n-1
    return fib(n-1)+fib(n-2)

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
if __name__=='__main__':
    print(fact(5))
    print(fib(5))
    print(prime(5))