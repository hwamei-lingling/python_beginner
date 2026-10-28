goal = int(input("Enter your savings goal: "))  # 5000
total = 0

while total < goal:
    deposit = int(input("Enter amount to deposit: "))  # 2500, then 1000, then 1300, then 300
    total += deposit
    print(f"Total savings: {total}")

print("Goal reached!")
