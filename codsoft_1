import tkinter as t
from tkinter import messagebox
from datetime import datetime

class TDList:
      def __init__(self,root):
            self.root=root
            self.tasks=[]
              
            self.m_frame=t.Frame(root,bg="#d4d4d4")
            self.m_frame.pack(side=t.LEFT,padx=20,pady=20)
              
            self.b_frame=t.Frame(root,bg="#d4d4d4")
            self.b_frame.pack(side=t.RIGHT,padx=15,pady=15)

            self.d_label=t.Label(self.m_frame,text=self.get_c_date(),bg="#d4d4d4",fg="#222222",font=("Arial",20,"bold"))
            self.d_label.pack(padx=10,pady=5)

            self.h_label=t.Label(self.m_frame,text="Today's Tasks To Complete",bg="#d4d4d4",fg="#222222",font=("Arial",20,"bold"))
            self.t_list=t.Listbox(self.m_frame,width=40,bg="#ffffff",fg="#222222",font=("Arial",12))      
            self.t_entry=t.Entry(self.m_frame,width=40,bg="#f0f0f0",fg="#222222",font=("Arial",12))

            self.add_b=t.Button(self.b_frame,text="Add",command=self.add_a_task,bg="#909090",font=("Arial",12))
            self.remove_b=t.Button(self.b_frame,text="Remove",command=self.remove_the_task,bg="#909090",font=("Arial",12))
            self.update_b=t.Button(self.b_frame,text="Update",command=self.update_the_task,bg="#909090",font=("Arial",12))
            self.complete_b=t.Button(self.b_frame,text="Complete",command=self.complete_task,bg="#909090",font=("Arial",12))
            self.incomplete_b=t.Button(self.b_frame,text="Incomplete Tasks",command=self.incomplete_tasks,bg="#909090",font=("Arial",12))
            self.all_b=t.Button(self.b_frame,text="All Tasks",command=self.all_tasks,bg="#909090",font=("Arial",12))
            self.rall_b=t.Button(self.b_frame,text="Remove all",command=self.rall_tasks,bg="#909090",font=("Arial",12))
              
            self.congrats_l=t.Label(self.m_frame,text="",bg="#f0f0f0",fg="#4CA450",font=("Arial",20,"bold"),width=40,height=2,anchor="center",justify="center")

            self.d_label.pack(padx=10,pady=5)
            self.h_label.pack(padx=10,pady=5)
            self.t_list.pack(padx=10,pady=5)
            self.t_entry.pack(padx=10,pady=10)
            self.congrats_l.pack(padx=10,pady=20)

            self.add_b.pack(padx=10,pady=5,fill=t.X)
            self.remove_b.pack(padx=10,pady=5,fill=t.X)
            self.update_b.pack(padx=10,pady=5,fill=t.X)
            self.complete_b.pack(padx=10,pady=5,fill=t.X)
            self.incomplete_b.pack(padx=10,pady=5,fill=t.X)
            self.all_b.pack(padx=10,pady=5,fill=t.X)
            self.rall_b.pack(padx=10,pady=5,fill=t.X)

            root.configure(bg="#f0f0f0")
      
      def get_c_date(self):
            return datetime.now().strftime("%Y-%m-%d")
      
      def add_a_task(self):
            task=self.t_entry.get()
            if task:
                  self.tasks.append({"task":task,"status":"Pending"})
                  self.t_list.insert(t.END,task)
                  self.t_entry.delete(0,t.END)
                  self.congrats_l.config(text="")

      def remove_the_task(self):
            try:
                  task_i=self.t_list.curselection()[0]
                  self.t_list.delete(task_i)
                  self.tasks.pop(task_i)

                  if not self.tasks:
                        self.congrats_l.config(text="All Tasks are Removed. Add new Tasks!")
                  else:
                        self.congrats_l.config(text="")

            except IndexError:
                  messagebox.showwarning("Error","Select a task to remove")        

      def update_the_task(self):
            try:
                  task_i=self.t_list.curselection()[0]
                  new_task=self.t_entry.get()      
                  if new_task:
                        self.tasks[task_i]["task"]=new_task
                        self.t_list.delete(task_i)
                        self.t_list.insert(task_i,new_task) 
                        self.t_entry.delete(0,t.END)
            except IndexError:
                  messagebox.showwarning("Error","Select a task to update")               

      def complete_task(self) :
            try:
                  task_i=self.t_list.curselection()[0]
                  self.tasks[task_i]["status"]="Completed"
                  self.t_list.delete(task_i)
                  self.t_list.insert(task_i,f"{self.tasks[task_i]['task']}(Completed)")

                  if all(task["status"]=="Completed" for task in self.tasks):
                        self.congrats_l.config(text="")
                  else:
                        self.congrats_l.config(text="")     

            except IndexError:
                  messagebox.showwarning("Error","Select a task to complete")

      def incomplete_tasks(self):
            self.t_list.delete(0,t.END)
            for task in self.tasks:
                  if task["status"]=="Pending":
                        self.t_list.insert(t.END,task["task"])     

      def all_tasks(self):
            self.t_list.delete(0,t.END) 
            for task in self.tasks:
                  task_d=task["task"]
                  if task["status"]=="Completed":
                        task_d+=" (Completed)"
                  self.t_list.insert(t.END,task_d)           

      def rall_tasks(self):
            self.t_list.delete(0,t.END)
            self.tasks=[]
            self.congrats_l.config(text="All tasks are removed. Add new tasks!")

if __name__=="__main__":
      root=t.Tk()
      root.title("To-Do-List")
      app=TDList(root)
      root.mainloop() 
