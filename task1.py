with open("indata.txt", "r") as file: #"r" untuk mode read saja
    numbers = [int(line.strip()) for line in file]

total = sum(numbers)
print(" Task 1 -  Program Read Data ".center(50, "="))
print(f"{total:.2f}")