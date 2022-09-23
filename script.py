# Recursion #
def fibo(n):
    return 1 if n <=2 else fibo(n-1) + fibo(n-2)

# Dynamic programming #
def fibo2(n):
    result = [0 for i in range(n+1)]
    result[0] = 1
    result[1] = 1
    for i in range(2, n+1):
        result[i] = result[i-2] + result[i-1]
    return result[n-1]
