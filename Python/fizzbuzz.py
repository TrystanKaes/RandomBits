""" Trystan Kaes
    Fun little way to do FizzBuzz because of pythons string behavior
    March 10, 2020 """
    
n = input("Enter a value for n:")

for x in range(1,int(n)+1):
    print("Fizz"*(x%3==0) + "Buzz"*(x%5==0) or x)
