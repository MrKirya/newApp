from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
import os
import shutil
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(90, 70, 461, 291))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(parent=MainWindow)
        self.action.setObjectName("action")
        self.action.triggered.connect(self.open_folder_dialog)
        self.action_2 = QtGui.QAction(parent=MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_2.triggered.connect(self.open_file_dialog)
        self.action_4 = QtGui.QAction(parent=MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_4.triggered.connect(self.save_button_clicked)
        self.action_6 = QtGui.QAction(parent=MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_6.triggered.connect(QtCore.QCoreApplication.quit)
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_4)
        self.menu.addSeparator()
        self.menu.addAction(self.action_6)
        self.menubar.addAction(self.menu.menuAction())
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(90, 70, 461, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_folder_dialog(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.Directory)  # Установка режима выбора папки
        folder_path = dialog.getExistingDirectory(None, "Выберите папку", QtCore.QDir.homePath())
        new_folder_path = os.path.join(folder_path, "hello world")
        os.mkdir(new_folder_path)
        new_json_path = os.path.join(new_folder_path, "config.json")
        existing_json_path = "C:/Users/Kirill/PycharmProjects/GraphPyQT/config.json"
        shutil.copyfile(existing_json_path, new_json_path)
        # Дальнейшая обработка выбранной папки
        if folder_path:
            print("Сохранили конфиг в папку:", folder_path)

    def open_file_dialog(self):
        dialog = QFileDialog()
        file_path, _ = dialog.getOpenFileName(None, "Выберите файл")

        # Дальнейшая обработка выбранного файла
        if file_path:
            print("Выбранный файл:", file_path)
            with open(file_path, 'r') as file:
                content = file.read()
                self.textBrowser.setText(content)

    def save_button_clicked(self):
        # Пустой обработчик нажатия кнопки "Сохранить"
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graph Editor (v.0.1)"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.action.setText(_translate("MainWindow", "Новый проект"))
        self.action_2.setText(_translate("MainWindow", "Открыть проект"))
        self.action_4.setText(_translate("MainWindow", "Сохранить"))
        self.action_6.setText(_translate("MainWindow", "Выход"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
