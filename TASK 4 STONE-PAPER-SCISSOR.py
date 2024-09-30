import random
import tkinter as t
from tkinter import messagebox

def welcome_animation(step=0):
    welcome_txt=["Welcome to the", "Rock-Paper-Scissor", "Game!"]
    if step<len(welcome_txt):
        welcome_l.config(text=welcome_txt[step], font=('Hervetica',40 + step*6),bg='#A37171', fg='white')
        win.after(1000, welcome_animation, step + 1)
    else:
        win.after(1000, ask_name) 

def ask_name():
    welcome_l.config(text="Enter Player's name:", font=('Helvetica', 30), bg='#A37171', fg='white')
    name_enter.pack(pady=10)
    name_l.pack(pady=5)
    start_b.pack(pady=10)

def rules():
    rule="Rules of the Game:\n\n1) Rock beats Scissor\n2) Scissor beats Paper\n3) Paper beats Rock\n\nBest of Luck!!"
    messagebox.showinfo("Game Rules",rule)   

def start():
    global u_name
    u_name=name_enter.get().strip()
    if not u_name:
        messagebox.showinfo("Input Error", "Please enter your name to start .")
        return
    
    name_enter.pack_forget()
    start_b.pack_forget()
    name_l.pack_forget()

    welcome_l.config(text="Get Ready!", font=('Hervetica', 40), bg='#A37171', fg='white')
    win.after(1000, countdn, 3)
     
def countdn(num):
    if num>0:
        welcome_l.config(text=str(num), font=('Hervetica', 40), bg='#A37171', fg='white')
        win.after(1000, countdn, num -1)
    else:
        welcome_l.config(text="Let's Go!", font=('Hervetica', 40), bg='#A37171', fg='white')
        win.after(1000, start_game)

def start_game():
    welcome_l.pack_forget()
    win.geometry('750x500')
    win.resizable(False,False)    

    global u_score, com_score, round_n, score_text
    u_score, com_score, round_n=0,0,1
    score_text=t.StringVar()

    score_f=t.Frame(win,bg='#A37171')
    score_f.pack(pady=20)

    global user_l,com_l
    user_l=t.Label(score_f, text=f"{u_name}'s Score:0",font=('Helvetica',15), bg='#A37171', fg='white')
    user_l.pack(side=t.LEFT,padx=50)   
    com_l=t.Label(score_f, text="Computer's Score:0", font=('Helvetica',15), bg='#A37171', fg='white')
    com_l.pack(side=t.RIGHT,padx=50)   

    global result_l
    result_l=t.Label(win,text="",font=('Helvetica',15), bg='#A37171', fg='white')
    result_l.pack(pady=20)

    button_f=t.Frame(win, bg='#A37171')
    button_f.pack(pady=20)
    rock_b=t.Button(button_f, text="Rock", width=10, height=5, command=lambda: det_winner('Rock'), bg='lightblue')
    rock_b.grid(row=0, column=0, padx=20)
    paper_b=t.Button(button_f, text="Paper", width=10, height=5, command=lambda: det_winner('Paper'), bg='lightgreen')
    paper_b.grid(row=0, column=1, padx=20)
    scissor_b=t.Button(button_f, text="Scissor", width=10, height=5, command=lambda: det_winner('Scissor'), bg='lightcoral')
    scissor_b.grid(row=0, column=2, padx=20)

    control_f=t.Frame(win,bg='#A37171')
    control_f.pack(side=t.BOTTOM, fill=t.X, pady=20)
    t.Button(control_f, text="Scoreboard", command=toggle_score, bg='lightgrey').pack(side=t.LEFT, padx=20)
    t.Button(control_f, text="Rules", command=rules, bg='lightgrey' ).pack(side=t.LEFT, padx=20)
    t.Button(control_f, text="Quit Game", command=win.destroy, bg='lightgrey' ).pack(side=t.RIGHT, padx=20)
    t.Button(control_f, text="Reset Game", command=reset, bg='lightgrey' ).pack(side=t.RIGHT, padx=20)

    global score_display, congrats_l
    score_display=t.Label(win, textvariable=score_text, font=('Helvetica', 10), justify=t.LEFT, bg='#A37171', fg='White')
    congrats_l=t.Label(win,text="",font=('Helvetica', 24), bg='#A37171', fg='white')
    congrats_l.pack(pady=20)

def det_winner(user_c):
    option=['Rock', 'Paper', 'Scissor']
    computer_c=random.choice(option)

    if user_c == computer_c:
        result= f"Both choose {user_c}. It's a Tie!"
    elif(user_c == 'Rock' and computer_c== 'Scissor') or \
        (user_c == 'Paper' and computer_c== 'Rock') or \
        (user_c == 'Scissor' and computer_c== 'Paper'):
        result= f"You choose {user_c}, Computer choose {computer_c}. You Won!"
        up_score('user')
    else:
        result=f"You choose {user_c}, Computer choose {computer_c}. Computer Won!"
        up_score('computer')

    result_l.config(text=result)    

    if u_score>=10 or com_score>=10:
        show_congrats()

def up_score(winner):
    global u_score, com_score
    if winner=='user':
        u_score+=1
        user_l.config(text=f"{u_name}'s Score: {u_score}")   
    else:
        com_score+=1      
        com_l.config(text=f"Computer's Score: {com_score}")  

def show_congrats():
    msg=f"Congratulations, {u_name}!\n You Won!" if u_score>=10 else "Computer Won!"
    congrats_l.config(text=msg)
    ani_congrats(0)
    save_score()
    
def save_score():
    global round_n, score_text
    winner= u_name if u_score>=10 else "Computer"
    round_res=f"Round {round_n}: {winner} Won! (You: {u_score}, Computer: {com_score})"
    score_text.set(score_text.get() + round_res + "\n")
    round_n+=1
    reset_s()

def reset_s():
    global u_score, com_score
    u_score=0
    com_score=0
    user_l.config(text=f"{u_name}'s Score: 0")
    com_l.config(text="Computer's Score: 0")

def ani_congrats(step):
    colors=['Green','blue']
    if step< 10:
        congrats_l.config(fg=colors[step %2])
        win.after(300, ani_congrats, step + 1 )
    else:
        congrats_l.config(text="")   

def reset():
    global u_score, com_score, round_n
    u_score, com_score, round_n=0, 0, 1
    reset_s()
    result_l.config(text="")
    score_text.set("")
    congrats_l.config(text="")


def toggle_score():
    if score_display.winfo_ismapped():
        score_display.pack_forget()
    else:
        score_display.pack()    

win=t.Tk()
win.title("Rock-Paper-Scissor Game")
win.geometry('750x500')
win.resizable(False, False)
win.config(bg='#A37171')

welcome_l=t.Label(win, text="", font=('Helvetica', 40), bg='#A37171', fg='white')
welcome_l.pack(pady=(100, 20))

name_enter=t.Entry(win, font=('Helvetica', 20), bg='lightgrey')
name_l=t.Label(win, text="", font=('Helvetica', 20), fg='black', bg='#A37171')
start_b=t.Button(win, text="Start Game", command=start, bg='lightgrey')

win.after(500, welcome_animation)
win.mainloop()

