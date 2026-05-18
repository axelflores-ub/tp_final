from task import Task

# TaskManager handles all task operations

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        if not description:
            print("Task cannot be empty")
            return

        if priority not in ["High", "Medium", "Low"]:
            print("Invalid priority")
            return

        task = Task(description, priority)
        self.tasks.append(task)

    def get_sorted_tasks(self):
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        return sorted(self.tasks, key=lambda x: priority_order[x.priority])

    def show_tasks(self):
        tasks = self.get_sorted_tasks()

        if not tasks:
            print("No tasks available")
            return

        for i, task in enumerate(tasks):
            status = "Done" if task.done else "Pending"
            print(f"{i} - {task.description} [{task.priority}] [{status}]")

    def complete_task(self, index):
        try:
            self.tasks[index].mark_as_done()
        except:
            print("Invalid task number")

    def delete_task(self, index):
        try:
            self.tasks.pop(index)
        except:
            print("Invalid task number")