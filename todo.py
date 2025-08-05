FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = [line.strip() for line in file]
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task, tasks):
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added successfully!")

def remove_task(task, tasks):
    if task in tasks:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Task '{task}' removed successfully!")
    else:
        print("Task not found.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
        print()

def menu():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task, tasks)
        elif choice == '3':
            task = input("Enter the exact task to remove: ")
            remove_task(task, tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    menu()
