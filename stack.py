stack = []
while True:
    print("\n---Stack Menu---")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice:"))
    if choice == 1:
        element = input("Enter element to push:")
        stack.append(element)
        print(str(element)+" pushed into stack")
    elif choice == 2:
         if len(stack)==0:
            print(Stack is empty)
         else:
            popped = stack.pop()
            print((element)+" popped from stack")
            
    elif choice == 3:
        print("Current stack:",stack)
    elif choice == 4:
        print("Goodbye....")
        break

