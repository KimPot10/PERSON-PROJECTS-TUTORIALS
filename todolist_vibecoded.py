import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.config(bg="#f0f0f0")
        
        self.tasks = []
        
        # Title
        title = tk.Label(root, text="My To-Do List", font=("Arial", 20, "bold"), bg="#f0f0f0")
        title.pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(root, bg="#f0f0f0")
        input_frame.pack(pady=10)
        
        self.task_entry = tk.Entry(input_frame, width=30, font=("Arial", 12))
        self.task_entry.pack(side=tk.LEFT, padx=5)
        self.task_entry.bind("<Return>", lambda e: self.add_task())
        
        add_btn = tk.Button(input_frame, text="Add Task", command=self.add_task, 
                           bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
                           cursor="hand2")
        add_btn.pack(side=tk.LEFT)
        
        # Task list frame with scrollbar
        list_frame = tk.Frame(root, bg="#f0f0f0")
        list_frame.pack(pady=10, fill=tk.BOTH, expand=True, padx=20)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox = tk.Listbox(list_frame, font=("Arial", 12), 
                                       selectmode=tk.SINGLE, bg="white",
                                       yscrollcommand=scrollbar.set, height=15)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.task_listbox.yview)
        
        # Button frame
        btn_frame = tk.Frame(root, bg="#f0f0f0")
        btn_frame.pack(pady=10)
        
        toggle_btn = tk.Button(btn_frame, text="✓ Complete/Uncomplete", 
                              command=self.toggle_task,
                              bg="#2196F3", fg="white", font=("Arial", 10, "bold"),
                              cursor="hand2", width=20)
        toggle_btn.pack(side=tk.LEFT, padx=5)
        
        delete_btn = tk.Button(btn_frame, text="🗑 Delete Task", 
                              command=self.delete_task,
                              bg="#f44336", fg="white", font=("Arial", 10, "bold"),
                              cursor="hand2", width=15)
        delete_btn.pack(side=tk.LEFT, padx=5)
        
        # Bind double-click to toggle
        self.task_listbox.bind("<Double-Button-1>", lambda e: self.toggle_task())
    
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"text": task, "completed": False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
    
    def toggle_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_listbox()
            self.task_listbox.selection_set(index)
    
    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks.pop(index)
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete!")
    
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            if task["completed"]:
                display_text = f"✓ {task['text']}"
                self.task_listbox.insert(tk.END, display_text)
                # Get the last index and change its color
                last_index = self.task_listbox.size() - 1
                self.task_listbox.itemconfig(last_index, fg="gray")
            else:
                self.task_listbox.insert(tk.END, f"○ {task['text']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

    #di mapush amp