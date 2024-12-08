from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
window= Tk()
window.title("tkinter's Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800,weight=1)
window.columnconfigure(1, minsize=800, weight=1)
def open_file():
    filepath = askopenfilename(filetypes=[("Text files", "*.txt", ("All Files", "*.*"))])