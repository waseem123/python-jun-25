print("1. Biryani - RS. 110")
print("2. Tahari - RS. 90")
print("3. Noodles - RS. 100")
print("4. Pizza - RS. 120")
choice = int(input("ENTER YOUR CHOICE - "))

match(choice):
    case 1:
        qty = int(input("ENTER QUANTITY FOR BIRYANI - "))
        bill = qty * 110
        print(f'YOUR BILL FOR {qty} BIRYANI(s) IS RS. {bill}')
    case 2:
        qty = int(input("ENTER QUANTITY FOR TAHARI - "))
        bill = qty * 90
        print(f'YOUR BILL FOR {qty} TAHARI(s) IS RS. {bill}')
    case 3:
        qty = int(input("ENTER QUANTITY FOR NOODLES - "))
        bill = qty * 100
        print(f'YOUR BILL FOR {qty} NOODLES IS RS. {bill}')
    case 4:
        qty = int(input("ENTER QUANTITY FOR PIZZA - "))
        bill = qty * 120
        print(f'YOUR BILL FOR {qty} PIZZA(s) IS RS. {bill}')
    case _:
        print("WRONG INPUT! PLEASE SELECT THE OPTION BETWEEN 1 TO 4")