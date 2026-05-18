from task_manager import TaskManager

# Entry point of the application

manager = TaskManager()

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Delete Task\n5. Exit")
    option = input("Choose an option: ")

    if option == "1":
        desc = input("Enter task description: ")
        prio = input("Enter priority (High/Medium/Low): ").capitalize()
        manager.add_task(desc, prio)

    elif option == "2":
        manager.show_tasks()

    elif option == "3":
        manager.show_tasks()
        i = int(input("Enter task number to complete: "))
        manager.complete_task(i)

    elif option == "4":
        manager.show_tasks()
        i = int(input("Enter task number to delete: "))
        manager.delete_task(i)

    elif option == "5":
        break

    else:
        print("Invalid option")