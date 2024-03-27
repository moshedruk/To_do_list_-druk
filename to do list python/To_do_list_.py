

tasks = []

def add_task():
    description = input("Enter task description: ")
    due_date = input("Enter due date: ")
    status = input("Enter task status: ")
    task = {"description": description, "due_date": due_date, "status": status}
    tasks.append(task)
    print("Task added successfully.")


def edit_task():
    index = int(input("Enter index of task to edit: ")) - 1
    if 0 <= index < len(tasks):
        task = tasks[index]
        description = input(f"Enter new description (current: {task['description']}): ")
        due_date = input(f"Enter new due date (current: {task['due_date']}): ")
        status = input(f"Enter new status (current: {task['status']}): ")
        tasks[index] = {"description": description,"due_date": due_date ,"status": status }                        
        print("Task edited successfully.")
    else:
        print("Invalid index.")


def delete_task():
    if tasks:
        index = int(input("Enter index of task to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            print("Task deleted successfully.")
        else:
            print("Invalid index.")
    else:
        print("Taxts is Empty. you need to enter a task")


def display_tasks():
    if tasks:
        for index, task in enumerate(tasks, 1):
            print(f"Task {index}:")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Status: {task['status']}")
            print()
    else:
        print("No tasks available.")


def main():
     ###create the loop to run the app
    while True:     
        print("welcome to the to do list app")        
        print("================================")
        print("Select your request. ")
        print("\n")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Display Tasks")
        print("5. Quit")
        print("\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            edit_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            print("goodbye")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





