import sys
import os
import mysql.connector
from PyQt5.QtWidgets import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.alert = Alert(self)

        self.username = QLineEdit(self)
        self.QUserLabel = QLabel("EMAIL")

        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.QPasswordLabel = QLabel("PASSWORD")

        self.btn_Submit = QPushButton("LOGIN")

        layout = QFormLayout()
        layout.addRow(self.QUserLabel, self.username)
        layout.addRow(self.QPasswordLabel, self.password)
        layout.addRow(self.btn_Submit)

        self.setLayout(layout)

        self.btn_Submit.clicked.connect(self.submit_btn)

    def submit_btn(self):
        USERNAME = self.username.text()
        PASSWORD = self.password.text()

        con = mysql.connector.connect(user="root", password="123456", host="localhost", database="face_attandance")
        cursor = con.cursor(prepared=True)

        get_user = """SELECT * FROM teachers WHERE email = %s AND password = %s"""
        cursor.execute(get_user, (USERNAME, PASSWORD))
        record = cursor.fetchone()
        con.commit()

        if record:
            print(record)
        else:
            self.alert.show()


class Alert(QDialog):
    def __init__(self, parent=Form):
        super().__init__(parent)

        self.txtAlter = QLabel("Email or Passwoord Incorect")
        self.btn_Submit = QPushButton("OK")

        layout = QFormLayout()
        layout.addRow(self.txtAlter)
        layout.addRow(self.btn_Submit)

        self.setLayout(layout)

        self.btn_Submit.clicked.connect(self.submit_btn)

    def submit_btn(self):
        Alert.close(self)


app = QApplication(sys.argv)

form = Form()
form.show()

app.exec_()
