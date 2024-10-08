# Date    : 15/02/23 6:53 pm
# Author  : Parmar Maulik (mm.2004.parmar@gmail.com)
# GitHub    : (https://github.com/Maulikatgit)
# Twitter    : (https://twitter.com/Mr_younglord)
# Version : 1.0.0
from tkinter import PhotoImage
import customtkinter as ctk
import cv2
import dlib
from PIL import Image, ImageTk
import configure
from Backend.FirebaseServices.datasetServices import DatasetServices
from Backend.SqliteServices.dataset_sqlite_services import DatasetSqliteServices
from Backend.SqliteServices.signup_sqlite_services import SignupSqliteServices


class FaceDetection(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title("Face Detection")
        self.geometry("650x550")
        self.configure(fg_color=configure.very_dark_gray)
        self._icon = PhotoImage(file="Assets/logo.png")
        self.iconphoto(False, self._icon)
        self.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.__firebaseDataset = DatasetServices()
        self.__parent = kwargs["master"]
        self.__signupsql = SignupSqliteServices()
        self.__datasetsql = DatasetSqliteServices()
        self.__detector = dlib.get_frontal_face_detector()
        self.__enrollment = kwargs["enrollment"]
        self.__cap = cv2.VideoCapture(0)
        self.__label = ctk.CTkLabel(self, font=(configure.font, 20, "bold"), text='')
        self.__label.grid(row=0, column=0, sticky="nsew")
        self.__frame = ctk.CTkFrame(self)
        self.__frame.grid(row=1, column=0, sticky="nsew")
        self.__error = ctk.CTkLabel(self.__frame)
        self.__take_photo = ctk.CTkButton(self.__frame, text="Take Photo")
        self.__take_photo.grid(row=0, column=1, sticky="nsew")
        self.__detect_face()

    def __detect_face(self):
        _, frame = self.__cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rgbframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        capturedFrame = Image.fromarray(rgbframe)
        photo_image = ImageTk.PhotoImage(image=capturedFrame)
        self.__label.photo_image = photo_image
        self.__label.configure(image=photo_image)

        faces2 = self.__detector(gray, 2)
        faces = []
        if not faces2:
            self.__error.configure(text="No face detected")
            self.__error.grid(row=0, column=0)
            self.__take_photo.configure(state="disabled")
        else:
            for result in faces2:
                faces.append([result.left(), result.top(), result.right(), result.bottom()])
                if len(faces) > 1:
                    self.__error.configure(text="Multiple faces detected")
                    self.__error.grid(row=0, column=0)
                    self.__take_photo.configure(state="disabled")
                elif len(faces) == 1:
                    self.__error.configure(text="Perfectly Fine")
                    self.__error.grid(row=0, column=0)
                    self.__take_photo.configure(state="normal")

                    def save():
                        try:
                            cv2.imwrite("Dataset/{}.jpg".format(self.__enrollment), frame)
                            self.__datasetsql.massInsert(list(self.__enrollment))
                            self.__firebaseDataset.addDataset(self.__enrollment, 'Dataset/{}.jpg'.format(self.__enrollment))
                        except Exception as e:
                            obj = open("KONGKNITEC.log", "a")
                            obj.write(str(e))
                            obj.close()
                        self.onClosing()

                    self.__take_photo.configure(command=lambda: save())

        self.__label.after(10, self.__detect_face)

    def onClosing(self):
        try:
            self.__cap.release()
            self.destroy()
        except Exception as e:
            print(e)
