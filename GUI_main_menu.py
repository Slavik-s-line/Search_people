from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QMessageBox
from PyQt5 import QtGui
from intormation import *


def result(name, surname, age):
    victory_win = QMessageBox()
    victory_win.setWindowTitle('Картка воєнного')
    try:
        text_result = get_question_after(str(name), str(surname), int(age))
        victory_win.setText(f"Ім'я: {text_result[0]}\n"
                            f"Фамілія: {text_result[1]}\n"
                            f"Рік народження: {text_result[2]}\n"
                            f"Звання: {text_result[3]}\n"
                            f"Тип військ: {text_result[4]}\n"
                            f"Нагороди: {text_result[5]}\n"
                            f"Місце служби: {text_result[6]}")
    except:
        victory_win.setText("Такого військового не знайдено")

    victory_win.exec_()


def main_menu():
    def get_info():
        name = txt_name.text()
        surname = txt_surname.text()
        age = txt_age.text()
        result(name, surname, age)

    app = QApplication([])
    main_win = QWidget()
    main_win.setWindowTitle('ЄПошук')
    main_win.resize(400, 200)
    main_win.setObjectName("MainWindow")
    main_win.setStyleSheet("#MainWindow{border-image:url(background.jpg)}")

    label_1 = QLabel('   Для пошуку військовослужбовця, внесіть дані у відповідні поля   ')
    label_1.setStyleSheet("background-color: rgb(255,255,255);")
    label_1.setFont(QtGui.QFont('SansSerif', 10))

    label_2 = QLabel("   Ім'я   ")
    label_2.setStyleSheet("background-color: rgb(255,255,255);")
    label_2.setFont(QtGui.QFont('SansSerif', 10))

    txt_name = QLineEdit('')

    label_3 = QLabel('   Фамілія   ')
    label_3.setStyleSheet("background-color: rgb(255,255,255);")
    label_3.setFont(QtGui.QFont('SansSerif', 10))

    txt_surname = QLineEdit('')

    label_4 = QLabel('   Рік народження   ')
    label_4.setStyleSheet("background-color: rgb(255,255,255);")
    label_4.setFont(QtGui.QFont('SansSerif', 10))

    txt_age = QLineEdit('')
    btn_ok = QPushButton('ЗНАЙТИ')
    btn_ok.clicked.connect(get_info)

    layout_main = QVBoxLayout()
    layoutH1 = QHBoxLayout()
    layoutH2 = QHBoxLayout()
    layoutH3 = QHBoxLayout()
    layoutH4 = QHBoxLayout()
    layoutH5 = QHBoxLayout()

    layoutH1.addWidget(label_1, alignment=Qt.AlignCenter)
    layoutH2.addWidget(label_2, alignment=Qt.AlignCenter)
    layoutH2.addWidget(txt_name, alignment=Qt.AlignCenter)
    layoutH3.addWidget(label_3, alignment=Qt.AlignCenter)
    layoutH3.addWidget(txt_surname, alignment=Qt.AlignCenter)
    layoutH4.addWidget(label_4, alignment=Qt.AlignCenter)
    layoutH4.addWidget(txt_age, alignment=Qt.AlignCenter)
    layoutH5.addWidget(btn_ok, alignment=Qt.AlignCenter)

    layout_main.addLayout(layoutH1)
    layout_main.addLayout(layoutH2)
    layout_main.addLayout(layoutH3)
    layout_main.addLayout(layoutH4)
    layout_main.addLayout(layoutH5)
    main_win.setLayout(layout_main)

    main_win.show()
    app.exec_()


if __name__ == "__main__":
    main_menu()
