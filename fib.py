dicionary = {0:1, 1:1}

def fib(n):
    if n in dicionary:
        return dicionary[n]
    dicionary[n] = fib(n-1) + fib(n-2)
    return dicionary[n]

num = int(input('Digite o numero '))
print(fib(num))