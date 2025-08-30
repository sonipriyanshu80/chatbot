stack = []
print("\n---Stack Menu---")
print("1. Push")
print("2. Pop")
print("3. Peek")
print("4. Display")
print("5. Exit")

while True:
    choice = int(input("Enter your choice:"))
    if choice == 1:
        element = input("Enter element to push:")
        stack.append(element)
        print(str(element)+" pushed into stack")

    elif choice == 2:
         if len(stack)==0:
            print("Stack is empty")
         else:
            popped = stack.pop()
            print("popped from stack")

    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty! Nothing at peek")
        else:
            print("Top element",{stack[-1]})
            
    elif choice == 4:
        if len(stack) == 0:
            print("stack is empty")
        else:
            print("Current stack:",stack)

    elif choice == 5:
        print("See you again....")
        break
    else:
        print("Invalid choice! Try again")

