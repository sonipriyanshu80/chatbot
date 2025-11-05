print("Menu driven program for list operations")
print("1. Numeric")
print("2. Character")
print("3. Exit")
choice = int(input("Enter your choice: "))  
if choice == 1:
    l1 = []
    n = int(input("Enter length of list: "))
    for i in range(n):
        print("enter",i+1,"value")
        a = int(input())
        l1.append(a)
    print("Original list:", l1)
    search = int(input("Enter element to search: "))
    if search in l1:
        print("Element found at index:", l1.index(search))
    else:
        print("Element not found")
elif choice == 2:
    l2 = []
    n = int(input("Enter length of list: "))
    for i in range(n):
        print("enter",i+1,"value")
        a = input()
        l2.append(a)
    print("Original list:", l2)
    search = input("Enter element to search: ")
    if search in l2:
        print("Element found at index:", l2.index(search))
    else:
        print("Element not found")
else:
    print("wrong choice")
