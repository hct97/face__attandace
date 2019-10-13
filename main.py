import sys
import os
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

current_user = (1, "admin")


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.alert = Alert(self)

        self.setWindowTitle("LOGIN")
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
            global current_user
            current_user = record
            self.mainWindow = MainWindow()
            self.mainWindow.show()
            form.close()
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


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.table = QTableWidget()
        self.setWindowTitle("WELCOME " + current_user[1])

        self.resize(800, 600)

        # table.setAlignment(Qt.AlignCenter)
        self.table.setRowCount(3)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Class name", "Subject name"])
        self.getAllClass()
        self.setCentralWidget(self.table)

    def getAllClass(self):
        con = mysql.connector.connect(user="root", password="123456", host="localhost", database="face_attandance")
        cursor = con.cursor()

        sql = "Select classes.name, subjects.name from classes inner join subjects on subjects.id = classes.subjectID " \
              "where teacherID = %s"
        cursor.execute(sql, (current_user[0],))
        records = cursor.fetchall()

        for index, row in enumerate(records):
            self.table.setItem(index, 0, QTableWidgetItem(row[0]))
            self.table.setItem(index, 1, QTableWidgetItem(row[1]))


app = QApplication(sys.argv)

form = Form()
form.show()

app.exec_()
