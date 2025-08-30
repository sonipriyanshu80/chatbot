queue = []
print("\n---Queue Menu---")
print("1. Enqueue")
print("2. Dequeue")
print("3. Peek")
print("4. Display")
print("5. Exit")

while True:
    choice = int(input("Enter your choice:"))
    if choice == 1:
        element = input("Enter element to enqueue:")
        queue.append(element)
        print(str(element)+" enqueued into queue")

    elif choice == 2:
         if len(queue)==0:
            print("queue is empty")
         else:
            removed = queue.pop(0)
            print("Dequeued element",{removed})

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty! No front element")
        else:
            print("Front element",{queue[0]})
            
    elif choice == 4:
        if len(queue) == 0:
            print("queue is empty")
        else:
            print("Current queue:",queue)

    elif choice == 5:
        print("See you again....")
        break
    else:
        print("Invalid choice! Try again")


