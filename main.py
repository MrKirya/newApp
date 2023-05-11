from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QApplication, QSplashScreen
from PyQt6.QtGui import QPixmap
import os
import shutil
import sys
import time


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
        self.action_8 = QtGui.QAction(parent=MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_8.triggered.connect(self.clear_text)
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_4)
        self.menu.addSeparator()
        self.menu.addAction(self.action_6)
        self.menu.addSeparator()
        self.menu.addAction(self.action_8)
        self.menubar.addAction(self.menu.menuAction())
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(90, 70, 461, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clear_text(self):
        self.textBrowser.clear()

    def open_folder_dialog(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.Directory)  # Установка режима выбора папки
        folder_path = dialog.getExistingDirectory(None, "Выберите папку", QtCore.QDir.homePath())

        if folder_path:
            new_folder_path = os.path.join(folder_path, "hello world")
            os.mkdir(new_folder_path)
            new_json_path = os.path.join(new_folder_path, "config.json")

            # Определение пути к config.json в исполняемом файле
            if getattr(sys, 'frozen', False):
                # Исполняемый файл (.exe)
                base_path = sys._MEIPASS
            else:
                # Исходный код Python
                base_path = os.path.dirname(os.path.abspath(__file__))
            existing_json_path = os.path.join(base_path, "config.json")

            shutil.copyfile(existing_json_path, new_json_path)
            MainWindow.close()  # Закрыть текущее окно
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()  # Отобразить главное меню
        else:
            # Пользователь нажал "Отмена"
            QMessageBox.information(None, "Message", "Операция отменена. Возврат в главное меню.")
            self.setupUi(MainWindow)

    def open_file_dialog(self):
        dialog = QFileDialog()
        file_path, _ = dialog.getOpenFileName(None, "Выберите файл")

        # Дальнейшая обработка выбранного файла
        if file_path:
            print("Выбранный файл:", file_path)
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension == ".html":
                with open(file_path, 'r') as file:
                    content = file.read()
                    self.textBrowser.setHtml(content)
            elif file_extension == ".json":
                with open(file_path, 'r') as file:
                    content = file.read()
                    self.textBrowser.setText(content)
            else:
                self.textBrowser.setText("Выбранный файл не является HTML- или JSON-файлом.")
        else:
            # Пользователь нажал "Отмена"
            QMessageBox.information(None, "Message", "Операция отменена. Возврат в главное меню.")
            self.setupUi(MainWindow)

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
        self.action_8.setText(_translate("MainWindow", "Очистить главное окно"))


if __name__ == "__main__":
    # Получаем абсолютный путь к папке images
    image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')

    # Создаем путь к файлу general_picture.png внутри папки images
    image_path = os.path.join(image_dir, 'general_picture.png')

    app = QApplication(sys.argv)

    # Отображение картинки (3 секунды)
    splash = QSplashScreen(QPixmap(image_path))
    splash.show()
    app.processEvents()
    time.sleep(3)
    splash.close()

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
