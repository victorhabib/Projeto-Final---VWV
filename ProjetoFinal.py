import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os

class BatalhaNaval:
    
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.title("Batalha Naval")
        self.window.geometry("500x500")
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)
        self.window.rowconfigure(3, weight=1)
        self.window.rowconfigure(4, weight=1)
        self.window.rowconfigure(5, weight=1)
        self.window.columnconfigure(0, weight=0)
        self.window.columnconfigure(1, weight=0)
        self.window.columnconfigure(1, weight=0)
        self.window.columnconfigure(2, weight=0)
        self.window.columnconfigure(3, weight=0)
        self.window.columnconfigure(4, weight=0)
        
        
        
        im=Image.open("batalha.jpg")  
        photo=ImageTk.PhotoImage(im)  
        cv = tk.Canvas()  
        cv.grid(row = 0, column = 8)  
        cv.create_image(4, 4, image=photo, anchor='nw')  
        
        
        
        botão = tk.Button(self.window)
        botão.configure(text="A1")
        botão.configure()
        botão.grid(row=1, column=0)
        
        
        botão = tk.Button(self.window)
        botão.configure(text="A2")
        botão.configure()
        botão.grid(row=1, column=1)
        
        botão = tk.Button(self.window)
        botão.configure(text="A3")
        botão.configure()
        botão.grid(row=1, column=2)
        
        botão = tk.Button(self.window)
        botão.configure(text="A4")
        botão.configure()
        botão.grid(row=1, column=3)
        
        botão = tk.Button(self.window)
        botão.configure(text="A5")
        botão.configure()
        botão.grid(row=1, column=4)
        
        botão = tk.Button(self.window)
        botão.configure(text="A6")
        botão.configure()
        botão.grid(row=1, column=5)
        
        botão = tk.Button(self.window)
        botão.configure(text="A7")
        botão.configure()
        botão.grid(row=1, column=6)
        
        #####
        
        botão = tk.Button(self.window)
        botão.configure(text="B1")
        botão.configure()
        botão.grid(row=2, column=0)
        
        botão = tk.Button(self.window)
        botão.configure(text="B2")
        botão.configure()
        botão.grid(row=2, column=1)
        
        botão = tk.Button(self.window)
        botão.configure(text="B3")
        botão.configure()
        botão.grid(row=2, column=2)
        
        botão = tk.Button(self.window)
        botão.configure(text="B4")
        botão.configure()
        botão.grid(row=2, column=3)
        
        botão = tk.Button(self.window)
        botão.configure(text="B5")
        botão.configure()
        botão.grid(row=2, column=4)
        
        botão = tk.Button(self.window)
        botão.configure(text="B6")
        botão.configure()
        botão.grid(row=2, column=5)
        
        botão = tk.Button(self.window)
        botão.configure(text="B7")
        botão.configure()
        botão.grid(row=2, column=6)
        
        #####
        
        botão = tk.Button(self.window)
        botão.configure(text="C1")
        botão.configure()
        botão.grid(row=3, column=0)
        
        botão = tk.Button(self.window)
        botão.configure(text="C2")
        botão.configure()
        botão.grid(row=3, column=1)
        
        botão = tk.Button(self.window)
        botão.configure(text="C3")
        botão.configure()
        botão.grid(row=3, column=2)
        
        botão = tk.Button(self.window)
        botão.configure(text="C4")
        botão.configure()
        botão.grid(row=3, column=3)
        
        botão = tk.Button(self.window)
        botão.configure(text="C5")
        botão.configure()
        botão.grid(row=3, column=4)
        
        botão = tk.Button(self.window)
        botão.configure(text="C6")
        botão.configure()
        botão.grid(row=3, column=5)
        
        botão = tk.Button(self.window)
        botão.configure(text="C7")
        botão.configure()
        botão.grid(row=3, column=6)
        
        ####
        
        botão = tk.Button(self.window)
        botão.configure(text="D1")
        botão.configure()
        botão.grid(row=4, column=0)
        
        botão = tk.Button(self.window)
        botão.configure(text="D2")
        botão.configure()
        botão.grid(row=4, column=1)
        
        botão = tk.Button(self.window)
        botão.configure(text="D3")
        botão.configure()
        botão.grid(row=4, column=2)
        
        botão = tk.Button(self.window)
        botão.configure(text="D4")
        botão.configure()
        botão.grid(row=4, column=3)
        
        botão = tk.Button(self.window)
        botão.configure(text="D5")
        botão.configure()
        botão.grid(row=4, column=4)
        
        botão = tk.Button(self.window)
        botão.configure(text="D6")
        botão.configure()
        botão.grid(row=4, column=5)
        
        botão = tk.Button(self.window)
        botão.configure(text="D7")
        botão.configure()
        botão.grid(row=4, column=6)
        
        #####
        
        botão = tk.Button(self.window)
        botão.configure(text="E1")
        botão.configure()
        botão.grid(row=5, column=0)
        
        botão = tk.Button(self.window)
        botão.configure(text="E2")
        botão.configure()
        botão.grid(row=5, column=1)
        
        botão = tk.Button(self.window)
        botão.configure(text="E3")
        botão.configure()
        botão.grid(row=5, column=2)
        
        botão = tk.Button(self.window)
        botão.configure(text="E4")
        botão.configure()
        botão.grid(row=5, column=3)
        
        botão = tk.Button(self.window)
        botão.configure(text="E5")
        botão.configure()
        botão.grid(row=5, column=4)
        
        botão = tk.Button(self.window)
        botão.configure(text="E6")
        botão.configure()
        botão.grid(row=5, column=5)
        
        botão = tk.Button(self.window)
        botão.configure(text="E7")
        botão.configure()
        botão.grid(row=5, column=6)
        
        
        
        
    def iniciar(self):
        self.window.mainloop()
    

    

app = BatalhaNaval()
app.iniciar()
