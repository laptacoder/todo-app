import tkinter as tk

root = tk.Tk()
root.title("Todo App")
root.configure(bg="grey")
root.geometry("500x500")

# configure grid columns so tasks expand horizontally
root.grid_columnconfigure(0, weight=1)

What_isTask = tk.Entry(root, width=30)
What_isTask.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

task_row = 1

def AddTask():
    global task_row
    task_text = What_isTask.get()
    if not task_text.strip():
        return  # ignore empty input

    newtask = tk.Label(root, text=task_text, bg="white", anchor="center")
    newtask.grid(row=task_row, column=0, padx=5, pady=5, sticky="ew")
    task_row += 1

    Task_Done = tk.Button(root, text="✔", command=lambda: newtask.destroy())
    Task_Done.grid(row=task_row-1, column=1)

# button to add task
Add_Task = tk.Button(root, text="Add a task", pady=10, padx=15, command=AddTask)
Add_Task.grid(row=0, column=1, padx=10, pady=10)

def Task_Complete():
    Task_Done.destroy()

root.mainloop()
