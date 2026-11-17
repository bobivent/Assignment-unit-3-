def main():
    tasks = []
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task name: ")
            tasks.append(task)
            print(f"Added: {task}")
        elif choice == "2":
            print("Your Tasks:", tasks if tasks else "No tasks yet.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()