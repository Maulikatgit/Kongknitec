# Date    : 22-03-2023 15:04
# Author  : Parmar Maulik (mm.2004.parmar@gmail.com)
# GitHub    : (https://github.com/Maulikatgit)
# Twitter    : (https://twitter.com/Mr_younglord)
# Version : 1.0.0

from firebase_admin import firestore


class AttendanceServices:

    def __init__(self):
        self.db = firestore.client()

    def insertAttendance(self, date, data):
        try:
            doc = self.db.collection('Attendance').document(date)
            if not doc.get().exists:
                self.db.collection('Attendance').document(date).set({'Date': date, 'Enrollment': data})
            else:
                enrolls = self.getAttendance(date)
                enrolls = enrolls['Enrollment']
                for enroll in data:
                    if enroll not in enrolls:
                        enrolls.append(enroll)
                print(enrolls)
                self.db.collection('Attendance').document(date).update({'Enrollment': enrolls})
        except Exception as e:
            file = open('KONGKNITEC.log', 'a')
            file.write(str(e))
            file.close()

    def getAttendance(self, date):
        try:
            doc = self.db.collection('Attendance').document(date)
            if not doc.get().exists:
                return None
            else:
                return doc.get().to_dict()
        except Exception as e:
            file = open('KONGKNITEC.log', 'a')
            file.write(str(e))
            file.close()
