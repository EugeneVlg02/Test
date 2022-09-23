def fibo(n):
    return 1 if n <=2 else fibo(n-1) + fibo(n-2)
for i in range(1, 10):
    print(fibo(i))

print("NEW feature")
