from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title('Gestion de tareas')
root.geometry('550x500') 

try:
    conn = sqlite3.connect('tareas.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE if not exists tareas (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
              title TEXT NOT NULL,
              description TEXT NOT NULL,
              completed BOOLEAN NOT NULL
              );
                """)
    conn.commit()
except sqlite3.Error as e:
    messagebox.showerror("Database Error", f"Error connecting to database: {e}")

def delete_task(task_id):
    try:
        c.execute("SELECT completed FROM tareas WHERE id = ?", (task_id,))
        completed = c.fetchone()[0]
        if completed:
            c.execute("DELETE FROM tareas WHERE id = ?", (task_id,))
            conn.commit()
            render_tasks()
        else:
            messagebox.showwarning("Delete Error", "Cannot delete a task that is not completed")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error deleting task: {e}")

def toggle_completed(task_id):
    try:
        c.execute("SELECT completed FROM tareas WHERE id = ?", (task_id,))
        completed = c.fetchone()[0]
        c.execute("UPDATE tareas SET completed = ? WHERE id = ?", (not completed, task_id))
        conn.commit()
        render_tasks()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error updating task: {e}")

def edit_task(task_id):
    try:
        c.execute("SELECT title, description FROM tareas WHERE id = ?", (task_id,))
        task = c.fetchone()
        et.delete(0, END)
        et.insert(0, task[0])
        ed.delete("1.0", END)
        ed.insert("1.0", task[1])
        btn.config(text='Actualizar tarea', command=lambda: update_task(task_id))
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error fetching task: {e}")

def update_task(task_id):
    titulo = et.get()
    descripcion = ed.get("1.0", END).strip()
    if not titulo or not descripcion:
        messagebox.showwarning("Input Error", "Title and description cannot be empty")
        return
    try:
        c.execute("UPDATE tareas SET title = ?, description = ? WHERE id = ?", (titulo, descripcion, task_id))
        conn.commit()
        et.delete(0, END)
        ed.delete("1.0", END)
        btn.config(text='Agregar tarea', command=add_task)
        render_tasks()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error updating task: {e}")

def render_tasks():
    try:
        for widget in frame.winfo_children():
            widget.destroy()
        
        c.execute("SELECT * FROM tareas")
        tasks = c.fetchall()
        
        for task in range(0, len(tasks)):
            id = tasks[task][0]
            completed = tasks[task][4]
            title = tasks[task][2]
            description = tasks[task][3]
            created_at = tasks[task][1]
            task_text = f"Titulo: {title}\nDescripcion: {description}\nFecha: {created_at}"
            
            l = Checkbutton(frame, text=task_text, width=42, anchor='w', command=lambda id=id: toggle_completed(id))
            l.grid(row=task, column=0, sticky='w', padx=5, pady=5)
            if completed:
                l.select()
                l.config(fg='grey')  
            
            btn_delete = Button(frame, text='Eliminar', command=lambda id=id: delete_task(id))
            btn_delete.grid(row=task, column=1, padx=5, pady=5, sticky='e')
            
            btn_edit = Button(frame, text='Modificar', command=lambda id=id: edit_task(id))
            btn_edit.grid(row=task, column=2, padx=5, pady=5, sticky='e')
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error fetching tasks: {e}")

def add_task(event=None):
    titulo = et.get()
    descripcion = ed.get("1.0", END).strip()
    if not titulo or not descripcion:
        messagebox.showwarning("Input Error", "Title and description cannot be empty")
        return
    try:
        c.execute("INSERT INTO tareas (title, description, completed) VALUES (?, ?, ?)", (titulo, descripcion, False))
        conn.commit()
        et.delete(0, END)
        ed.delete("1.0", END)
        render_tasks()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error adding task: {e}")

def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

l = Label(root, text='Titulo de la tarea')
l.grid(row=0, column=0, padx=5, pady=5)

et = Entry(root, width=50)
et.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

l2 = Label(root, text='Descripcion de la tarea')
l2.grid(row=1, column=0, padx=5, pady=5)

ed = Text(root, width=50, height=5)
ed.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

btn = Button(root, text='Agregar tarea', command=add_task)
btn.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

frame_container = Frame(root)
frame_container.grid(row=3, column=0, columnspan=3, sticky='nswe', padx=5, pady=5)

canvas = Canvas(frame_container)
scrollbar = Scrollbar(frame_container, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

frame = scrollable_frame

canvas.bind_all("<MouseWheel>", on_mouse_wheel)

et.focus()
root.bind('<Return>', add_task)

render_tasks()

root.mainloop()