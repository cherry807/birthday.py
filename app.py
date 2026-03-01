import tkinter as tk
from tkinter import PhotoImage

# ---------- SETUP ----------
root = tk.Tk()
root.title("Happy Birthday Kusuma 💖")
root.geometry("600x500")
root.configure(bg="pink")

# ---------- FUNCTIONS ----------
def show_second_template():
    clear_frame()
    msg = tk.Label(root, text="You are the brightest star in my world 🌟",
                   font=("Arial", 18, "bold"), bg="lightyellow", fg="darkblue", wraplength=500)
    msg.pack(pady=100)
    btn2 = tk.Button(root, text="Mee too 💕", font=("Arial", 14, "bold"),
                     bg="lightblue", fg="black", command=show_third_template)
    btn2.pack(pady=30)

def show_third_template():
    clear_frame()
    try:
        teddy_img = PhotoImage(file="teddy.png")  # Replace with your teddy image file path (PNG)
        img_label = tk.Label(root, image=teddy_img, bg="lightblue")
        img_label.image = teddy_img  # keep a reference
        img_label.pack(pady=20)
    except Exception:
        tk.Label(root, text="🐻💙", font=("Arial", 80), bg="lightblue").pack(pady=20)
    
    tk.Label(root, text="Happy Birthday Kusuma 💐", font=("Arial", 20, "bold"),
             bg="lightblue", fg="navy").pack(pady=10)

def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

# ---------- FIRST TEMPLATE ----------
heart = tk.Label(root, text="❤️", font=("Arial", 100), bg="pink")
heart.pack(pady=20)

text1 = tk.Label(root, text="Happy Birthday Kusuma 💖", font=("Arial", 22, "bold"),
                 bg="pink", fg="purple")
text1.pack(pady=10)

btn1 = tk.Button(root, text="Love U 💞", font=("Arial", 14, "bold"),
                 bg="red", fg="white", command=show_second_template)
btn1.pack(pady=30)

root.mainloop()
