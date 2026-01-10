import tkinter as tk

root = tk.Tk()
root.title("To-Do List")
root.geometry("350x400")

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

tk.Label(root, text="My To-Do List", font=("Arial", 14)).pack(pady=10)

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)

listbox = tk.Listbox(root, width=40, height=15)
listbox.pack(pady=10)

root.mainloop()
