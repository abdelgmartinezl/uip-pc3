def factorial(n):
     fact = 1
     x = 1
     while x <= n:
         fact *= x
         x += 1
     return fact

if __name__ == "__main__":
    print(factorial(5))