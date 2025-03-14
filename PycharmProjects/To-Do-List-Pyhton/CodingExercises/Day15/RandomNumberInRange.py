import random


def randomNumberInRange():
    n1 = int(input("Please provide the first number in range: "))
    n2 = int(input("Please provide the second number in range: "))
    return random.randrange(n1,n2)

print(f"The number is: {randomNumberInRange()}")