# Date    : 25/11/22 11:43 am
# Author  : Parmar Maulik (mm.2004.parmar@gmail.com)
# GitHub    : (https://github.com/Maulikatgit)
# Twitter    : (https://twitter.com/Mr_younglord)
# Version : 1.0.0
import customtkinter as ctk
from PIL import Image
import configure
from Backend.SqliteServices.login_sqlite_services import LoginSqliteServices
from Backend.SqliteServices.signup_sqlite_services import SignupSqliteServices
from Screens.Dashboard import attendance, dataset, dashboard, profile
from Screens.Refactor.customWidgets import CustomWidgets
from Screens.Refactor.dashboardHeaderGUI import dashboardHeaderGUI


class MainScreen(ctk.CTkFrame):

    def __init__(self, **kwargs):
        ctk.CTkFrame.__init__(self, kwargs['parent'], fg_color=configure.very_dark_gray)
        self.__parent = kwargs['parent']
        self.__parent.grid_configure(pady=0, padx=0)
        self.__controller = kwargs['controller']
        self.loginsql = LoginSqliteServices()
        self.signupsql = SignupSqliteServices()
        self.__mainScreenGUI()

    def __switcher(self, index):
        match index:
            case 0:
                self.__switcher('default')
                self.navigator.dashboardDarkImg = ctk.CTkImage(Image.open("Assets/dashboardd.png"), size=(20, 20))
                self.__dashboard.configure(fg_color=configure.vivid_cyan, text_color=configure.very_dark_gray,
                                           hover_color=configure.light_cyan, image=self.navigator.dashboardDarkImg)
                self.showFrame('Dashboard')

            case 1:
                self.__switcher('default')
                self.navigator.datasetDarkImg = ctk.CTkImage(Image.open("Assets/datasetd.png"), size=(20, 20))
                self.__dataset.configure(fg_color=configure.vivid_cyan, text_color=configure.very_dark_gray,
                                         hover_color=configure.light_cyan, image=self.navigator.datasetDarkImg)
                self.showFrame('Dataset')

            case 2:
                self.__switcher('default')
                self.navigator.attendanceDarkImg = ctk.CTkImage(Image.open("Assets/attendanced.png"), size=(20, 20))
                self.__attendance.configure(fg_color=configure.vivid_cyan, text_color=configure.very_dark_gray,
                                            hover_color=configure.light_cyan, image=self.navigator.attendanceDarkImg)
                self.showFrame('Attendance')

            case 3:
                self.__switcher('default')
                self.navigator.profileDarkImg = ctk.CTkImage(Image.open("Assets/profiled.png"), size=(20, 20))
                self.__profile.configure(fg_color=configure.vivid_cyan, text_color=configure.very_dark_gray,
                                         hover_color=configure.light_cyan, image=self.navigator.profileDarkImg)
                self.showFrame('Profile')

            case 'default':
                self.__dashboard.configure(fg_color=configure.very_dark_gray, text_color=configure.white,
                                           hover_color=configure.dark_gray, image=self.navigator.dashboardImg)
                self.__dataset.configure(fg_color=configure.very_dark_gray, text_color=configure.white,
                                         hover_color=configure.dark_gray, image=self.navigator.datasetImg)
                self.__attendance.configure(fg_color=configure.very_dark_gray, text_color=configure.white,
                                            hover_color=configure.dark_gray, image=self.navigator.attendanceImg)
                self.__profile.configure(fg_color=configure.very_dark_gray, text_color=configure.white,
                                         hover_color=configure.dark_gray, image=self.navigator.profileImg)

    def __mainScreenGUI(self):
        dashboardHeaderGUI(self, self.__controller)
        self.navigator = ctk.CTkFrame(master=self, width=configure.screen_width / 4,
                                      fg_color=configure.very_dark_gray,
                                      height=configure.screen_height - 100)
        ctk.CTkLabel(master=self.navigator, text='', height=30).grid(row=0, column=0)
        self.navigator.dashboardImg = ctk.CTkImage(Image.open('Assets/dashboard.png'), size=(20, 20))
        self.navigator.datasetImg = ctk.CTkImage(Image.open('Assets/dataset.png'), size=(20, 20))
        self.navigator.attendanceImg = ctk.CTkImage(Image.open('Assets/attendance.png'), size=(20, 20))
        self.navigator.profileImg = ctk.CTkImage(Image.open('Assets/profile.png'), size=(20, 20))
        self.__dashboard = CustomWidgets.customDashboardButtons(self.navigator, 'Dashboard',
                                                                self.navigator.dashboardImg,
                                                                lambda: self.__switcher(0))
        self.__dashboard.grid(row=1, column=0, pady=20)
        self.__dataset = CustomWidgets.customDashboardButtons(self.navigator, 'Dataset',
                                                              self.navigator.datasetImg,
                                                              lambda: self.__switcher(1))
        self.__dataset.grid(row=2, column=0)
        self.__attendance = CustomWidgets.customDashboardButtons(self.navigator, 'Attendance',
                                                                 self.navigator.attendanceImg,
                                                                 lambda: self.__switcher(2))
        self.__attendance.grid(row=3, column=0, pady=20)

        self.__profile = CustomWidgets.customDashboardButtons(self.navigator, 'Profile',
                                                              self.navigator.profileImg,
                                                              lambda: self.__switcher(3))
        self.__profile.grid(row=4, column=0)
        self.navigator.grid(row=1, column=0, sticky='n')
        self.__dashboardStack = ctk.CTkFrame(master=self, width=(configure.screen_width / 4) * 3)
        ctk.CTkLabel(master=self.__dashboardStack, height=configure.screen_height - 100,
                     width=(configure.screen_width / 4) * 3, text='').grid(row=0, column=0)
        self.__dashboardStack.grid(row=1, column=1, sticky='n')
        self.frames = {}
        self.__frameStack = (dashboard.Dashboard, attendance.Attendance, profile.Profile, dataset.Dataset)
        for window in self.__frameStack:
            page_name = window.__name__
            # to take the first frame and place it on the main frame
            frame = window(parent=self.__dashboardStack, controller=self)
            # to add the frame to the stack
            self.frames[page_name] = frame
            # to place the frame on the main frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.showFrame("Dashboard")
        self.__switcher(0)

    def showFrame(self, page_name):
        """
        Show a frame for the given page name
        """
        frame = self.frames[page_name]
        frame.tkraise()
