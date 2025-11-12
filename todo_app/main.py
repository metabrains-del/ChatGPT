def load_tasks():
    try:
        with open('todo_app/tasks.txt', 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('todo_app/tasks.txt', 'w') as f:
        for task in tasks:
            f.write(f"{task}\n")

def add_task(tasks, new_task):
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def delete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks.pop(task_index - 1)
        save_tasks(tasks)
        print("Task deleted!")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            new_task = input("Enter task: ")
            add_task(tasks, new_task)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            try:
                task_index = int(input("Enter task number to delete: "))
                delete_task(tasks, task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
