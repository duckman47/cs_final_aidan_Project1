from PyQt6.QtWidgets import *
from gui import *
from csv import *
import os

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.__setup=0
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda:self.submit())

    def submit(self):
        vid=self.lineEdit_2.text().strip()
        write_in = self.lineEdit.text().strip()
        vote = ""
        if os.path.isfile("vote.csv"):
            ids_counted=[]
            with open('vote.csv', mode='r', newline='') as f:
                file = reader(f)
                for row in file:
                    ids_counted.append(row[0])
        else:
            ids_counted=[]
        if vid != "":
            if vid.isdigit():
                if vid not in ids_counted:
                    if self.radioButton.isChecked():
                        vote = "john"
                        self.radioButton.setChecked(False)
                    elif self.radioButton_2.isChecked():
                        vote = "jane"
                        self.radioButton_2.setChecked(False)
                    elif self.radioButton_3.isChecked():
                        if write_in != "":
                            vote = write_in
                            self.radioButton_3.setChecked(False)
                        else:
                            self.label_4.setText("<font color='red'>Please Fill Out Write In</font>")

                    else:
                        self.label_4.setText("<font color='red'>Please Select Option</font>")
                else:
                    self.label_4.setText("<font color='red'>Id Error</font>")
                    self.lineEdit_2.setText("")
            else:
                self.label_4.setText("<font color='red'>Id Error</font>")
                self.lineEdit_2.setText("")


        else:
            self.label_4.setText("<font color='red'>Please Enter ID</font>")
        if vote != "":

            header=["Voter ID","Vote"]
            info=[vid,vote]
            if os.path.isfile("vote.csv"):
                with open('vote.csv', 'a', newline='') as f:
                    w = writer(f)
                    w.writerow(info)
                self.label_4.setText("<font color='green'>Vote Counted</font>")
                self.lineEdit_2.setText("")
            else:
                with open('vote.csv', 'w', newline='') as f:
                    w = writer(f)
                    w.writerow(header)
                    w.writerow(info)
                self.label_4.setText("<font color='green'>Vote Counted</font>")
                self.lineEdit_2.setText("")







