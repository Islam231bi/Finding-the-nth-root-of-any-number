x = int(input("Enter the number "))
n = int(input("nth root "))
if x < 0 and n % 2 == 0:
    print("undefined")
else:

    def f(x, n):
        return x**(1/n)


    print(f(x, n))