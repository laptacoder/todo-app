import tkinter as tk
import csv
import os

def Load_Tasks():
    if os.path.exists("tasks.csv"):
        with open("tasks.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # skip empty rows
                    AddTask(row[0])

root = tk.Tk()
root.title("Todo App")
root.configure(bg="grey")
root.geometry("500x500")

tasks = []
deleted_tasks = []

# configure grid columns so tasks expand horizontally
root.grid_columnconfigure(0, weight=1)

What_isTask = tk.Entry(root, width=30)
What_isTask.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

task_row = 1

def AddTask(task_text=None):
    global task_row
    if task_text is None:
        task_text = What_isTask.get()

    task_frame = tk.Frame(root, background="grey")
    task_frame.grid(column=0, row=task_row, columnspan=2, sticky="ew", padx=(8, 80))
    newtask = tk.Label(task_frame, text=task_text, fg="black", anchor="center", bg="white")
    newtask.grid(row=task_row, column=0, padx=5, pady=5, sticky="ew")
    task_row += 1

    Task_Done = tk.Button(task_frame, text="✔", command=lambda: delete_task(task_frame, task_text), background="Green", pady=2, padx=5)
    Task_Done.grid(row=task_row-1, column=1, padx=15)

    tasks.append(task_text)

def delete_task(task_frame, task_text):
    deleted_tasks.append(task_text)   # save text
    task_frame.destroy()
    if task_text in tasks:
        tasks.remove(task_text)

#Restore the last deleted task
def Undo():
    if deleted_tasks:
        last_task = deleted_tasks.pop()
        AddTask(last_task)

# button to add task
Add_Task = tk.Button(root, text="Add a task", pady=15, padx=5, command=AddTask)
Add_Task.grid(row=0, column=1, padx=10, pady=10)
Add_Task.configure(background="white")

#Undo Button
Undo_Button = tk.Button(root, text="Undo", pady= 5, padx=10, command=Undo)
Undo_Button.place(relx=0.98, rely=0.98, anchor="se")
Undo_Button.configure(background="white")

def Save_Tasks():
    with open("tasks.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task])

#Save Button
Save_Button = tk.Button(root, text="Save Tasks", padx= 5, pady=15, command=Save_Tasks, background="white")
Save_Button.grid(row=0, column=2, padx=(0,15))

root.protocol("WM_DELETE_WINDOW", lambda: (Save_Tasks(), root.destroy()))
Load_Tasks()
root.mainloop()
