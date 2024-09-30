import tkinter as t
import random
import string
from tkinter import messagebox

def generate_pswd(type,size):
    if type== 'easy':
        characters = string.ascii_lowercase
    elif type== 'medium':
        characters=string.ascii_letters+string.digits
    else:
        characters= string.ascii_letters+string.digits+string.punctuation

    if size < 8:
        pswd_entry.delete(0,t.END)
        pswd_entry.insert(t.END, "Password must be at least 8 characters.")
        return None

    pswd=''.join(random.choice(characters) for _ in range (size))
    pswd_entry.delete(0, t.END)
    pswd_entry.insert(t.END, pswd) 

def generator_page():
    welcome_f.pack_forget()
    generator_f.pack(expand=True)    

def main():
    global pswd_entry, generator_f, welcome_f
    root=t.Tk()
    root.title("Password Generator")

    root.geometry("600x400")
    root.resizable(False,False)
    root.configure(bg="#f0f8ff")

    welcome_f=t.Frame(root, bg="#f0f8ff", padx=20, pady=20)
    welcome_f.pack(expand=True)

    welcome_l=t.Label(welcome_f, text="Password Generator", font=("Arial", 32, "bold"), bg="#f0f8ff", fg="#333333")
    welcome_l.pack(pady=50)

    next_b=t.Button(welcome_f, text="Next", font=("Arial", 18), bg="#add8e6", fg="#333333", command=generator_page)
    next_b.pack(pady=20)      

    generator_f=t.Frame(root, bg="#f0f8ff", padx=20, pady=20)       

    type_l=t.Label(generator_f, text="Select password Strength:", font=("Arial", 18), bg="#f0f8ff", fg="#333333")
    type_l.grid(row=0, column=0, columnspan=3, pady=10)

    type_var= t.StringVar(value="easy")

    easy_r= t.Radiobutton(generator_f, text="Easy", variable=type_var, value="easy", font=("Arial", 20, "bold"),bg="#f0f8ff", fg="#333333" )    
    medium_r= t.Radiobutton(generator_f, text="Medium", variable=type_var, value="medium", font=("Arial", 20, "bold"),bg="#f0f8ff", fg="#333333" )    
    strong_r= t.Radiobutton(generator_f, text="Strong", variable=type_var, value="strong", font=("Arial", 20, "bold"),bg="#f0f8ff", fg="#333333" )

    easy_r.grid(row=1, column=0, padx=40, pady=20, sticky="w")    
    medium_r.grid(row=1, column=1, padx=40, pady=20, sticky="w")    
    strong_r.grid(row=1, column=2, padx=40, pady=20, sticky="w")  

    size_l=t.Label(generator_f, text="Enter Password Length:", font=("Arial", 18), bg="#f0f8ff", fg="#333333")
    size_l.grid(row=2, column=0, columnspan=3, pady=10)

    size_entry=t.Entry(generator_f, width=10, font=("Arial", 18), bg="#f0f8ff", fg="#333333" )
    size_entry.grid(row=3, column=0, columnspan=3, pady=5)
    def generate():
        try:
            size= int(size_entry.get())
            type= type_var.get()
            generate_pswd(type, size)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number for password length.")

    generate_b=t.Button(generator_f, text="Generate Password",font=("Arial", 18), bg="#add8e6", fg="#333333", command=generate )   
    generate_b.grid(row=4, column=0, columnspan=3, pady=10)

    pswd_entry=t.Entry(generator_f, width=40, font=("Arial", 18), bg="#f0f8ff", fg="#333333" )
    pswd_entry.grid(row=5, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()    

    


  



