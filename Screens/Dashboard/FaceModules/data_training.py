# Date    : 15/02/23 6:53 pm
# Author  : Parmar Maulik (mm.2004.parmar@gmail.com)
# GitHub    : (https://github.com/Maulikatgit)
# Twitter    : (https://twitter.com/Mr_younglord)
# Version : 1.0.0

import os
import pickle
import face_recognition


class TrainDataset:
    def __init__(self, parent):
        parent.configure(state="disabled")
        self.allFaceEncodings = {}
        for file in os.listdir("Dataset"):
            if not file.endswith(".jpg"):
                continue
            image = face_recognition.load_image_file("Dataset/" + file)
            user = file.split(".")[0]
            self.allFaceEncodings[str(user)] = face_recognition.face_encodings(image)[0]
        with open('Dataset/TrainedData/trained_dataset.dat', 'wb') as f:
            pickle.dump(self.allFaceEncodings, f)
        parent.configure(state="normal")
