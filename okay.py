import random

#
x = random.randint(1, 100)

#
attempts_remaining = 10

print("Masz tylko 10 szans na odgadnięcie liczby.")

graj = "true"
while graj == "true":
    guess = int(input("\nZgadnij liczbę: "))
    #
    attempts_remaining = attempts_remaining - 1
    if guess == x:
        print("Gratulacje, udało ci się odgadnąć liczbę!")
        graj = "false"

    else:
        if guess > x:
            print("Liczba jest za duża!")
        if guess < x:
            print("Liczba jest za mała")
        if attempts_remaining == 0:
            print("\nPrzegrałeś, liczba to ",x," .")
            graj = "false"

