import json
import os

class Task:
    def __init__(self, title, description, due_date, priority, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed

    def __str__(self):
        return f"[{'X' if self.completed else ' '}] {self.title} (Due: {self.due_date}, Priority: {self.priority})"

class ToDoList:
    def __init__(self, filename="todo_list.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def update_task(self, index, new_task):
        self.tasks[index] = new_task
        self.save_tasks()

    def delete_task(self, index):
        del self.tasks[index]
        self.save_tasks()

    def mark_as_complete(self, index):
        self.tasks[index].completed = True
        self.save_tasks()

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return [Task(**data) for data in json.load(file)]
        return []

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark as Complete")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date: ")
            priority = input("Priority: ")
            task = Task(title, description, due_date, priority)
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Task number to update: ")) - 1
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date: ")
            priority = input("Priority: ")
            new_task = Task(title, description, due_date, priority)
            todo_list.update_task(index, new_task)
        elif choice == '4':
            index = int(input("Task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            index = int(input("Task number to mark as complete: ")) - 1
            todo_list.mark_as_complete(index)
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
