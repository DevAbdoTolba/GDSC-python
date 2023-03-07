# allot of simple methods without any imports


def isPrime(n):
    """
    This function will check if a number is prime or not.
    """
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

def primeNumbers(n):
    """
    This function will print all the prime numbers from 1 to n.
    """
    for x in range(1, n + 1):
        if isPrime(x):
            print(x)

def sum(x, y):
    """
    This function will return the sum of two numbers.
    """
    return x + y

def difference(x, y):
    """
    This function will return the difference of two numbers.
    """
    return x - y

def helloName(name):
    """
    This function will print Hello and the name of the person.
    """
    print("Hello " + name)


def HelloWorld():
    """
    This function will print Hello World.
    """
    print("Hello World")

def SayHello():
    """
    Print a string of code in assembly that prints helloworld
    """
    code = """
    mov eax, 4
    mov ebx, 1
    mov ecx, msg
    mov edx, msglen
    int 0x80
    mov eax, 1
    mov ebx, 0
    int 0x80
    msg db 'Hello World', 0xa, 0
    msglen equ $ - msg
    """

    print(code)
    


    
    
