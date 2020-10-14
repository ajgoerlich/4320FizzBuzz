#Created by Andrew Goerlich for IT 4320 at the University of Missouri-Columbia
#FizzBuzz

for n in range(1, 101):
    if(n % 3 == 0) and (n % 5 == 0):
        print("FizzBuzz")
        continue
        
    if(n % 3 == 0):
        print("Fizz")
        continue

    if(n % 5 == 0):
        print("Buzz")

    else:
        print(n)
