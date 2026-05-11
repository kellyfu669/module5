from module5_mod import NumberManager

manager = NumberManager()

N = int(input("Enter N: "))

for i in range(N):
    number = int(input("Enter number: "))
    manager.add_number(number)

X = int(input("Enter X: "))

print(manager.find_number(X))
