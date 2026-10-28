password = "admin"
attempt = input("Enter password: ")  # Attempts as above

while attempt != password:
    print("Incorrect! Try again.")
    attempt = input("Enter password: ")

print("Access granted!")
