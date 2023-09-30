import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class DailyTaskScheduler:
    def __init__(self, root):
        self.tasks = []
        self.logged_in = False
        self.current_user = ""
        self.root = root
        self.root.title("Daily Task Scheduler")
        self.root.geometry("500x600")
        self.root.configure(bg='#66ccff')

        self.login_frame = tk.Frame(root,bg='#66ccff')

        self.username_label = tk.Label(self.login_frame, text="Username",font=("Arial", 15),bg='#66ccff')
        self.username_label.pack(pady=(50, 10))
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()

        self.password_label = tk.Label(self.login_frame, text="Password",font=("Arial", 15),bg='#66ccff')
        self.password_label.pack(pady=(50, 10))
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login_user,font=("Arial", 15))
        self.login_button.pack(pady=(50, 10))

        self.login_frame.pack()

        self.task_frame = tk.Frame(root,width=100,height=100,bg='#66ccff')

        self.task_label = tk.Label(self.task_frame, text="Add Task",font=("Arial", 15),bg='#66ccff')
        self.task_label.pack()
        self.task_entry = tk.Entry(self.task_frame,width='20')
        self.task_entry.pack(pady=(10,10))

        self.add_button = tk.Button(self.task_frame, text="Add Task", command=self.add_task,font=("Arial", 10))
        self.add_button.pack()

        self.delete_button = tk.Button(self.task_frame, text="Delete Task", command=self.delete_task,font=("Arial", 10))
        self.delete_button.pack(pady=(20,20))

        self.task_label = tk.Label(self.task_frame, text="List of tasks added",font=("Arial", 15),bg='#66ccff')
        self.task_label.pack()
        
        self.task_listbox = tk.Listbox(self.task_frame, selectmode=tk.SINGLE,width='30')
        self.task_listbox.pack(pady=(10,10))

        self.reminder_button = tk.Button(self.task_frame, text="Set Reminder", command=self.set_task_reminder,font=("Arial", 10))
        self.reminder_button.pack()

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "1234":
            self.logged_in = True
            self.current_user = username
            self.login_frame.pack_forget()
            self.show_task_list()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def add_task(self):
        task = self.task_entry.get()
        self.tasks.append(task)
        self.task_listbox.insert(tk.END, task)
        messagebox.showinfo("Task Added", "Task added successfully.")

    def delete_task(self):
        selected_task = self.task_listbox.curselection()

        if selected_task:
            task_index = selected_task[0]
            task = self.task_listbox.get(task_index)
            self.task_listbox.delete(task_index)
            self.tasks.remove(task)
            messagebox.showinfo("Task Deleted", "Task deleted successfully.")
        else:
            messagebox.showinfo("No Task Selected", "Please select a task to delete.")

    def show_task_list(self):
        if self.logged_in:
            self.task_frame.pack()

    def set_task_reminder(self):
        task = self.task_entry.get()

        if task in self.tasks:
            reminder_window = tk.Toplevel(self.root)
            reminder_window.title("Set Reminder")

            reminder_label = tk.Label(reminder_window, text="Reminder Time (HH:MM):")
            reminder_label.pack()

            reminder_entry = tk.Entry(reminder_window)
            reminder_entry.pack()

            set_button = tk.Button(reminder_window, text="Set", command=lambda: self.schedule_reminder(task, reminder_entry.get(), reminder_window))
            set_button.pack()
        else:
            messagebox.showinfo("Invalid Task", "Please select a valid task.")

    def schedule_reminder(self, task, reminder_time, reminder_window):
        try:
            current_time = datetime.now().strftime("%H:%M")
            reminder_datetime = datetime.strptime(reminder_time, "%H:%M").strftime("%H:%M")

            # Code to schedule the reminder 

            messagebox.showinfo("Reminder Set", f"Reminder set for '{task}' at {reminder_time}.")
            reminder_window.destroy()
        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter a valid time (HH:MM).")


root = tk.Tk()


task_scheduler = DailyTaskScheduler(root)


root.mainloop()