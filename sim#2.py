rows = int(input("Enter number of rows: "))  # 3
cols = int(input("Enter number of columns: "))  # 4
for r in range(1, rows + 1):
    for c in range(1, cols + 1):
        print(f"Seat R{r}C{c}")