import tkinter as tk
import random

foods = [
    ["apple", "healthy"], ["rice", "healthy"], ["milk", "healthy"], ["fish", "healthy"], ["egg", "healthy"],
    ["corn", "healthy"], ["bean", "healthy"], ["pear", "healthy"], ["nuts", "healthy"], ["yogurt", "healthy"],
    ["cake", "unhealthy"], ["coke", "unhealthy"], ["chip", "unhealthy"], ["candy", "unhealthy"], ["fries", "unhealthy"],
    ["pizza", "unhealthy"], ["donut", "unhealthy"], ["chocolate syrup", "unhealthy"], ["burger", "unhealthy"], ["gum", "unhealthy"]
]

score = 0  

def restart():
    global score
    score = 0
    update_food()
    update_score()
    label_restart.pack_forget()
    btn_restart.pack_forget()
    btn_eat.config(state="normal")
    btn_do_not_eat.config(state="normal")

def update_food():
    global current_food, current_health
    current_food, current_health = random.choice(foods)
    label_food.config(text=f"Food: {current_food}", fg="black")
    label_feedback.config(text="")  

def update_score():
    label_score.config(text=f"Score: {score}")

def on_eat():
    global score
    if current_health == "healthy":
        score += 1
        label_food.config(text="✅ Well done! You have chosen a healthy food.", fg="green")
        update_score()
        root.after(3000, update_food)  
    else:
        label_food.config(text="❌ Oops! You have chosen unhealthy food.\nGame Over!", fg="red")
        game_over()

def on_do_not_eat():
    global score
    if current_health == "unhealthy":
        score += 1
        label_food.config(text="✅ Well done! You avoided unhealthy food.", fg="green")
        update_score()
        root.after(2000, update_food)
    else:
        label_food.config(text="❌ Oops! You avoided a healthy food.\nGame Over!", fg="red")
        game_over()

def game_over():
    btn_eat.config(state="disabled")
    btn_do_not_eat.config(state="disabled")
    label_restart.pack(pady=10)
    btn_restart.pack(pady=5)


root = tk.Tk()
root.title("Healthy Hero")
root.geometry("550x450")
root.configure(bg="white")


label_title = tk.Label(root, text="HEALTHY HERO!", fg="red", font=("Arial", 20, "bold"), bg="white")
label_title.pack(pady=10)


label_score = tk.Label(root, text=f"Score: {score}", fg="black", font=("Arial", 16, "bold"), bg="white")
label_score.pack(pady=5)

label_food = tk.Label(root, text="", fg="black", font=("Arial", 16, "bold"), bg="white")
label_food.pack(pady=10)

label_feedback = tk.Label(root, text="", fg="green", font=("Arial", 14), bg="white")
label_feedback.pack(pady=5)

update_food()

frame = tk.Frame(root, bg="white")
frame.pack(pady=20)

btn_eat = tk.Button(frame, text="Eat ✅", font=("Arial", 14), fg="white", bg="green", padx=20, command=on_eat)
btn_eat.pack(side=tk.LEFT, padx=10)

btn_do_not_eat = tk.Button(frame, text="Do not Eat ❌", font=("Arial", 14), fg="white", bg="red", padx=20, command=on_do_not_eat)
btn_do_not_eat.pack(side=tk.LEFT, padx=10)


label_restart = tk.Label(root, text="Click to Restart the Game", font=("Arial", 14), fg="green", bg="white")
btn_restart = tk.Button(root, text="Restart 🔁", font=("Arial", 14), fg="white", bg="blue", command=restart)


root.mainloop()