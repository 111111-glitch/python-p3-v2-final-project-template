from helpers import exit_program 
from models.task import add_task, delete_task, get_all_tasks, find_task_by_id, update_task_status


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            show_menu_tasks()
        elif choice == "2":
            create_new_task()
        elif choice == "3":
            delete_existing_task()
        elif choice == "4":
            display_all_tasks()
        elif choice == "5":
            find_task_by_id_menu()
        elif choice == "6":
            update_task_status_menu()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Tasks menu")
    print("2. Create new task")
    print("3. Delete task")
    print("4. View all tasks")
    print("5. Find task by ID")
    print("6. Update task status")

def show_menu_tasks():
    print("Tasks menu:")
    print("1. View all tasks")
    print("2. Find task by ID")
    # Add more options as needed

def create_new_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    add_task(title, description)
    print("Task created successfully!")

def delete_existing_task():
    task_id = input("Enter task ID to delete: ")
    delete_task(task_id)
    print("Task deleted successfully!")

def display_all_tasks():
    tasks = get_all_tasks()
    if tasks:
        print("All Tasks:")
        for task in tasks:
            print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}")
    else:
        print("No tasks found!")

def find_task_by_id_menu():
    task_id = input("Enter task ID to find: ")
    task = find_task_by_id(task_id)
    if task:
        print(f"Task found - ID: {task.id}, Title: {task.title}, Description: {task.description}")
    else:
        print("Task not found!")

def update_task_status_menu():
    task_id = input("Enter task ID to update status: ")
    new_status = input("Enter new status: ")
    update_task_status(task_id, new_status)
    print("Task status updated successfully!")

if __name__ == "__main__":
    main()
