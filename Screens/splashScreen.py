# Date    : 18/11/22 5:47 pm
# Author  : Parmar Maulik (mm.2004.parmar@gmail.com)
# GitHub    : (https://github.com/Maulikatgit)
# Twitter    : (https://twitter.com/Mr_younglord)
# Version : 1.0.0
from Helper_Functions.videoPlayer import VideoPlayer
import customtkinter as ctk
import configure


class SplashScreen(ctk.CTkFrame):
    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self._controller = kwargs['controller']
        self._parent = kwargs['parent']
        self._parent.grid_configure(padx=0, pady=0)
        self._splashGUI()

    def _splashGUI(self):
        splash = ctk.CTkLabel(self, text='', height=350, width=600,
                              bg_color=configure.very_dark_gray, anchor='center')
        splash.grid(row=0, column=0, padx=(configure.screen_width - 570) / 2,
                    pady=(configure.screen_height - 500) / 2)
        splashscreen = VideoPlayer("Assets/splash.gif", splash,
                                   controller=self._controller, parent=self._parent)
        splashscreen.play()
