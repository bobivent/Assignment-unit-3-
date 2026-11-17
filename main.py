def main():
    tasks = []

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            task = input("Enter the task description: ")

            # TODO: We will add validation here
            if task.strip() == "":
                print("Error: Task cannot be empty or spaces only!")
                continue

            tasks.append(task)
            print(f"Success: '{task}' added to the list.")

        elif choice == '2':
            print("\nYour Tasks:")
            if not tasks:
                print("No tasks yet.")
            else:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select 1, 2, or 3.")


if __name__ == "__main__":
    main()