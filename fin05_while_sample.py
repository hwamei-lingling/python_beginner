while True:
    print("\n--- Tuple Operations ---")
    print("1. Create a tuple")
    print("2. Access tuple elements")
    print("3. Update a tuple (via list conversion)")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        elements = input("Enter elements separated by commas: ")
        tup = tuple(elements.split(','))
        print(f"Created tuple: {tup}")

    elif choice == '2':
        if 'tup' in locals():
            index = int(input(f"Enter index (0 to {len(tup)-1}): "))
            if 0 <= index < len(tup):
                print(f"Element at index {index}: {tup[index]}")
            else:
                print("Index out of range.")
        else:
            print("No tuple created yet.")

    elif choice == '3':
        if 'tup' in locals():
            li_tup = list(tup)
            new_element = input("Enter new element to add: ")
            li_tup.append(new_element)
            tup = tuple(li_tup)
            print(f"Updated tuple: {tup}")
        else:
            print("No tuple created yet.")

    elif choice == '4':
        print("Exiting tuple operations.")
        break

    else:
        print("Invalid choice. Please try again.")