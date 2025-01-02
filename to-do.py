tasks = {}


def add_task(description):
    task_id = len(tasks) + 1
    tasks[task_id] = {"description": description, "status": "pending"}
    print("Task '{}' added with ID {}.".format(description, task_id))


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nTo-Do List:")
    for task_id, details in tasks.items():
        status = " Completed" if details["status"] == "completed" else " Pending"
        print("{}. {} [{}]".format(task_id, details["description"], status))


def update_task(task_id, new_description):
    if task_id in tasks:
        tasks[task_id]["description"] = new_description
        print("Task ID {} updated.".format(task_id))
    else:
        print("Task ID {} not found.".format(task_id))


def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        print("Task ID {} deleted.".format(task_id))
    else:
        print("Task ID {} not found.".format(task_id))

def mark_completed(task_id):
    if task_id in tasks:
        tasks[task_id]["status"] = "completed"
        print("Task ID {} marked as completed.".format(task_id))
    else:
        print("Task ID {} not found.".format(task_id))

while True:
    print("\nOperations")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Update Tasks")
    print("4. Delete Tasks")
    print("5. Mark As Completed")
    print("6. Exit")

    choice = input("Enter the choice (1-6): ")

    if choice == "1":
        description = input("Enter task description: ")
        add_task(description)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        try:
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new task description: ")
            update_task(task_id, new_description)
        except ValueError:
            print("Invalid input! Task ID must be a number.")
    elif choice == "4":
        try:
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        except ValueError:
            print("Invalid input! Task ID must be a number.")
    elif choice == "5":
        try:
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_completed(task_id)
        except ValueError:
            print("Invalid input! Task ID must be a number.")
    elif choice == "6":
        print("Exiting the application.")
        break
    else:
        print("Invalid choice! Please select a valid option.")
