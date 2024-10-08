# Date    : 12/08/22 7:27 pm
# Author  : Parmar Maulik (mm.2004.parmar@gmail.com)
# GitHub    : (https://github.com/Maulikatgit)
# Twitter    : (https://twitter.com/Mr_younglord)
# Version : 1.0.0
from customtkinter import *
import configure
import customtkinter as ctk
from PIL import Image


class CustomBox(CTkToplevel):
    def errorBox(self, title, message):
        self.title(title)
        self.resizable(False, False)
        self.configure(bg=configure.very_dark_gray)
        self.geometry("350x175+{}+{}".format(0, 0))
        img = ctk.CTkImage(Image.open('Assets/error.png'), size=(35, 35))
        self.iconphoto(False, img)
        error_image = CTkLabel(master=self, image=img, anchor='nw')
        error_image.place(x=10, y=15)
        label = CTkTextbox(master=self, width=300, height=100, state='normal', font=configure.welcome_fontstyle,
                           border_color=configure.very_dark_gray, fg_color=configure.very_dark_gray,
                           text_color=configure.white)
        label.place(x=50, y=10)
        label.insert('end', message)
        label.configure(state='disabled')
        button = CTkButton(master=self, text='OK', width=100, height=35, font=configure.welcome_fontstyle,
                           fg_color=configure.light_cyan, text_color=configure.very_dark_gray,
                           border_color=configure.white, hover_color=configure.vivid_cyan,
                           command=self.destroy, corner_radius=15)
        button.place(x=125, y=130)
        self.mainloop()
