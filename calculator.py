from time import sleep


def add(P, Q):
    return P + Q


def subtract(P, Q):
    return P - Q


def multiply(P, Q):
    return P * Q


def divide(P, Q):
    return P / Q


print("Selectionnez l'opération :")
print("A. Adition")
print("B. Soustraction")
print("C. Multiplication")
print("D. Division")

choice = input("Entrez votre choix (a / b / c / d): ")

num_1 = int(input("Entrez le premier nombre: "))
num_2 = int(input("Entrez le second  nombre: "))

if choice == "a":
    print(num_1, " + ", num_2, " = ", add(num_1, num_2))
elif choice == "b":
    print(num_1, " - ", num_2, " = ", subtract(num_1, num_2))
elif choice == "c":
    print(num_1, " * ", num_2, " = ", multiply(num_1, num_2))
    sleep(10000)
elif choice == "d":
    print(num_1, " / ", num_2, " = ", divide(num_1, num_2))

else:
    print("Choix incorrect")
