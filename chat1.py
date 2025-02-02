import customtkinter as ctk
from PIL import Image, ImageTk
import sys
def hrk(event):
    global x, y
    x = event.x
    y = event.y
def stkk(event):
    root.geometry(f'+{event.x_root - x}+{event.y_root - y}')
root = ctk.CTk()
root.overrideredirect(True)
root.geometry("600x800")
ctk.set_appearance_mode("leight")
root.title("Panel free fier")
root.bind("<ButtonPress-1>", hrk)
root.bind("<B1-Motion>", stkk)
ptm = "/home/blackglitch/Desktop/imporatant/icons/exit.png"
img = Image.open(ptm)
img = img.resize((40, 40))  
photos = ImageTk.PhotoImage(img)
def op():
    sys.exit()
but = ctk.CTkButton(root,image=photos,width=40,text="",hover_color="black",bg_color="#212121",fg_color="#212121",command=op)
but.place(x=550,y=0)
ptm = "/home/blackglitch/Desktop/imporatant/icons/start.png"
img = Image.open(ptm)
img = img.resize((200, 200))  
photos = ImageTk.PhotoImage(img)
def op():
    tx = ctk.CTkLabel(root, text="starting miner now your walet in .json file now", font=("Helvetica", 15, "bold"), text_color="red")
    tx.place(x=180,y=370)
but = ctk.CTkButton(root, image=photos, width=40, text="", hover_color="#e0e7d9",bg_color="#eaeee6", fg_color="#eaeee6", command=op)
but.place(x=210, y=200)
tx = ctk.CTkLabel(root, text="Enter For Start Miner Monero", font=("Helvetica", 24, "bold"), text_color="black")
tx.place(x=160,y=400)
ptm = "/home/blackglitch/Desktop/imporatant/icons/sl.png"  
img = Image.open(ptm)
img = img.resize((80, 80))  
photo = ImageTk.PhotoImage(img)
lb = ctk.CTkLabel(root, image=photo, text="")
lb.place(x=210, y=60)
tx = ctk.CTkLabel(root, text="SKIN-MINING", font=("Helvetica", 24, "bold"), text_color="red")
tx.place(x=290,y=90)
button = ctk.CTkButton(
    root,                      
    text="Enter Walet",
    width=300,
    height=50,
    fg_color="red",
    hover_color="#080808",
    corner_radius=10,
    text_color="white",
    font=("Arial", 14),
    border_width=2,
    border_color="black",
)
button.place(x=170, y=150)
fr = ctk.CTkFrame(root,width=600,height=400,bg_color="black",fg_color="black")
fr.place(x=0,y=400)
ptm = "/home/blackglitch/Desktop/imporatant/icons/c.png"  
img = Image.open(ptm)
img = img.resize((600, 400))  
photo = ImageTk.PhotoImage(img)
lb = ctk.CTkLabel(fr, image=photo, text="")
lb.place(x=0, y=0)
ptm = "/home/blackglitch/Desktop/imporatant/icons/g.png"  
img = Image.open(ptm)
img = img.resize((100, 100))  
photo = ImageTk.PhotoImage(img)
lb = ctk.CTkLabel(fr, image=photo, text="")
lb.place(x=20, y=230)
ptm = "/home/blackglitch/Desktop/imporatant/icons/m.png"  
img = Image.open(ptm)
img = img.resize((100, 100))  
photo = ImageTk.PhotoImage(img)
lb = ctk.CTkLabel(fr, image=photo, text="")
lb.place(x=480, y=10)
tx = ctk.CTkLabel(root, text="SKIN MINING V 1.1.00", font=("Helvetica", 18, "bold"), text_color="red")
tx.place(x=210,y=15)
root.mainloop()