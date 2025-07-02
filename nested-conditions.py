age = int(input("ENTER YOUR AGE - "))

if age>=18:
    vid = int(input("DO YOU HAVE VOTER ID? (1. Yes | 2. NO)"))
    if vid == 1:
        print("CONGRATULATIONS! YOU CAN VOTE.")
    else:
        print("SORRY! YOU CAN NOT VOTE.")
else:
    print(f"GET LOST! GROW UP AND THEN COME FOR VOTING AFTER {18-age} YEARS")