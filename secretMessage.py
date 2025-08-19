import tkinter as tk #rename tkinter to tk
import os, sys
from tkinter import scrolledtext, messagebox, PhotoImage

# this is to handle the resource path for the image so it works in both .py and .exe
# If you are using PyInstaller, this will ensure the image is included in the build
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)  
    return os.path.join(os.path.abspath("."), relative_path)

# create the main window
class SecretMessage():
    def __init__ (self, mainWindow):
        self.mainWindow = mainWindow
        
        mainWindow.title("💖 Secret Message 💖")
        mainWindow.geometry("400x400")
        mainWindow.config(bg="#ECECEC")

        #principal text (Label)
        # this is the main text that will be displayed in the window
        principalText = tk.Label(mainWindow, text="🔐 Enter password 🔐", font=("Ubuntu", 14, "bold"))
        principalText.pack(pady=20) 

        #image
        #the image needs to be in the same folder as the script or in the resource directory
        self.imagen = PhotoImage(file=resource_path("breadog22100.png")) 
        labelImagen = tk.Label(self.mainWindow, image=self.imagen, bg="#ECECEC",justify="center" )
        labelImagen.pack(pady=10)

        #ask for password
        self.entry = tk.Entry(mainWindow, show="*", font=(20))
        self.entry.pack(pady=10)

        #button to send
        #this button will call the verificarPass method when clicked
        self.btn = tk.Button(mainWindow, text="Send", command=self.verifyPass)
        self.btn.pack(pady=10)        

    def verifyPass(self):

        password = self.entry.get()
        messages = {
            "friend1": "hey thank you so much for test my project! I really appreciate it 💖💖💖",
            "friend2": "have a great day! remember that you are awesome and you can do anything you want 💖💖💖",
            "friend3": "I wish you all the best in your life, you deserve all the happiness in the world 💖💖💖",
        }

        if password in messages:
            # we use the window of long message instead of messagebox to see the full message
            showLongMessage(messages[password])
        else:
            messagebox.showerror("Error", "wrong password 😡")

        self.entry.delete(0, tk.END)  # limpia el entry para que puedan intentar otra vez

def showLongMessage(message):
    window = tk.Toplevel()
    window.title('secret message 👀👀👀👀')

    st = scrolledtext.ScrolledText(window, width=40, height=20, wrap=tk.WORD, font=("Arial", 14))
    st.pack(padx=10, pady=10)
    st.insert(tk.END, message)
    st.configure(state="disabled") #Para que no se pueda editar


mainWindow = tk.Tk()       
secretMessage = SecretMessage(mainWindow)
mainWindow.mainloop()
