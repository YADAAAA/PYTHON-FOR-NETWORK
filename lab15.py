try :
    items = int(input("Enter a number of items : "))
    print(items)
except ValueError:
    print("Your value is not an integer")