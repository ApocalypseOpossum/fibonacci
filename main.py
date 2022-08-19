fibmemory = {}

def main():
    print("\n\nThis program prints a fibonacci sequence up to 100.\n\n")
    for x in range(0, 100):
        print("{0} {1} ".format(x, fibonacci(x)))

def fibonacci(n):

    if n in fibmemory:
        return fibmemory[n]

    if n <= 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)
    fibmemory[n] = value
    return value
        
if __name__ == '__main__':
    main()