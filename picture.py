import tkinter as tk
from PIL import Image, ImageTk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        
    
    def create_widgets(self):
        img = Image.open(fp="myProjects/cat-world/cat.jfif")
        self.photoimage = ImageTk.PhotoImage(image=img)
        self.canvas = tk.Canvas(self, height=self.photoimage.height(), width=self.photoimage.width())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photoimage)
        self.canvas.grid(row=0, column=0, columnspan=2)
      
        self.next = tk.Button(self, text="NEXT")
        self.next.grid(row=1, column=0, sticky=tk.SW, pady=10, padx=5)

        self.quit = tk.Button(self, text="QUIT", command=self.master.destroy)
        self.quit.grid(row=1, column=1, sticky=tk.SE, pady=10, padx=5)

root = tk.Tk()
app = Application(root)
app.mainloop()
