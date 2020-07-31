from random import randint

n1 = randint(1, 100)
n2 = int(input("Guess an integer number between 1 and 100: "))
n_tentativas = 1

while n2 != n1:
    if n2 > n1:
        n_tentativas += 1
        n2 = int(input("The number is lower than this. Try again: "))
    else:
        n_tentativas += 1
        n2 = int(input("The number is higher than this. Try again: "))

print("Congratulations! You got it in {} attempts.".format(n_tentativas))
