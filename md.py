l1 = []
print("\n---Menu---")
print("1. add")
print("2. remove") 
print("3. display")
print("4. sort")
print("5. reverse")
print("6. search")
print("7. Exit")

while True:
    choice = int(input("Enter your choice:"))
    if choice == 1:
        element = int(input("Enter element to add:"))
        l1.append(element)
        print(str(element)+"added")

    elif choice == 2:
         val=int(input("enter element to remove"))
         if val not in l1:
            print("element not found")
         else:
            l1.remove(val)
            print("removed from list")

    elif choice == 3:
        if len(l1) == 0:
            print("list is empty")
        else:
            print("Current list:",l1)

    elif choice == 4:
        print("sorted list:",sorted(l1))

    elif choice == 5:
        l1.reverse()
        print(l1)

    elif choice == 6:
        val = int(input("enter element to search"))
        if val not in l1:
            print("element not found")
        else:
            print(val,"found at",l1.index(val))
    
    elif choice == 7:
        print("See you again....")
        break
    else:
        print("Invalid choice! Try again")










            
