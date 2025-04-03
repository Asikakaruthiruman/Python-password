import random
info = input("Enter your name and birth year: ")
choice = input("Enter choice:\n 1. Numbers & alphabet\n 2. Only numbers & special characters\n 3. Mix of both\n")

if choice == '1':
    characters = list(info) + [str(random.randint(0, 9)) for _ in range(5)]
elif choice == '2':
    characters = list("!@#$%^&*") + [str(random.randint(0, 9)) for _ in range(5)]
else:
    characters = list(info) + list("!@#$%^&*") + [str(random.randint(0, 9)) for _ in range(5)]

random.shuffle(characters)
password = ''.join(random.choices(characters, k=8))

print("Generated password:", password)
