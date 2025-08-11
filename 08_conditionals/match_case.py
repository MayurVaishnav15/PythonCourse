a = int(input("Enter a Lucky number between 1 to 10 : "))

match a:
    case 1:
        print("You won a earphone")
    case 3: 
        print("You won a camera")
    case 8: 
        print("You won a Smartphone")
    case _:
        print("Better Luck Next Time")