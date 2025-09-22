# todo_app.py
"""
A simple To-Do List app skeleton using Tkinter.
Google Calendar API integration will be added later.
"""
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("To-Do List")
    root.geometry("400x400")
    label = tk.Label(root, text="To-Do List App Skeleton")
    label.pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    main()


tasks = []
def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

    def remove_task(task):
        if task in tasks:
            tasks.remove(task)
            print(f"Task removed: {task}")
        else:
            print(f"Task not found: {task}")

            print("Remove task function")

            add_button = tk.Button(root, text="Add Task", command=lambda: add_task("Sample Task"))
            add_button.pack(pady=10)
            remove_button = tk.Button(root, text="Remove Task", command=lambda: remove_task("Sample Task"))
            remove_button.pack(pady=10)
            print("Add task function")

            