#while loop
num_rows = int(input("Enter the number of rows for the pattern: "))

current_row = 1
while current_row <= num_rows:
    if current_row == 1 or current_row == num_rows:
        print('*' * 5)
    else:
        print('*   *')
    current_row += 1
