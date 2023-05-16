import os
import shutil
import sys
import time
import sqlite3

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QFileDialog, QMessageBox, QApplication, QSplashScreen, QTabWidget, QTableView, QTextBrowser
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QMetaObject, QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage, QWebEngineUrlRequestInterceptor
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1076, 772)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")





        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1081, 721))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")

        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tableView = QtWidgets.QTableView(parent=self.tab_1)
        self.tableView.setGeometry(QtCore.QRect(30, 30, 256, 192))
        self.tableView.setObjectName("tableView")
        self.tabWidget.addTab(self.tab_1, "")


        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableView_2 = QtWidgets.QTableView(parent=self.tab_2)
        self.tableView_2.setGeometry(QtCore.QRect(30, 20, 256, 192))
        self.tableView_2.setObjectName("tableView_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setTabletTracking(False)
        self.tab_3.setObjectName("tab_3")
        self.webView = QWebEngineView(parent=self.tab_3)
        self.webView.setGeometry(QtCore.QRect(0, 0, 1091, 721))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setObjectName("webView")
        self.tabWidget.addTab(self.tab_3, "")
        self.tabWidget.setCurrentWidget(self.tab_3)  # Установить tab_3 как текущую вкладку




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

        # self.textBrowser = QtWidgets.QTextBrowser(parent=self.tab_3)
        # self.textBrowser.setGeometry(QtCore.QRect(90, 70, 461, 291))
        # self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clear_text(self):
        self.webView.setHtml("")  # Очистить содержимое QWebEngineView

    def open_folder_dialog(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.Directory)  # Установка режима выбора папки
        folder_path = dialog.getExistingDirectory(None, "Выберите папку", QtCore.QDir.homePath())

        if folder_path:
            new_folder_path = os.path.join(folder_path, "New Package")
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
            self.setupUi(MainWindow)
        else:
            # Пользователь нажал "Отмена"
            QMessageBox.information(None, "Message", "Операция отменена. Возврат в главное меню.")
            self.setupUi(MainWindow)

    def open_file_dialog(self):
        dialog = QFileDialog()
        file_path, _ = dialog.getOpenFileName(None, "Выберите файл")

        if file_path:
            print("Выбранный файл:", file_path)
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension == ".html":
                self.open_html_file(file_path)
            else:
                QMessageBox.warning(None, "Предупреждение", "Выбранный файл не является HTML-файлом.")
        else:
            QMessageBox.information(None, "Сообщение", "Операция отменена. Возврат в главное меню.")
            self.setupUi(MainWindow)

    def open_html_file(self, file_path):
        self.webView.setUrl(QtCore.QUrl.fromLocalFile(file_path))
        self.webView.show()
    def create_database(self,database_path, folder_path):
        if getattr(sys, 'frozen', False):
            # Путь к исполняемому файлу (.exe)
            base_path = sys._MEIPASS
        else:
            # Путь к исходному коду Python
            base_path = os.path.dirname(os.path.abspath(__file__))

        db_path = os.path.join(base_path, database_path)
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        # Создание таблицы professions
        cur.execute("""CREATE TABLE IF NOT EXISTS professions(
           id INTEGER PRIMARY KEY,
           name TEXT,
           type INTEGER DEFAULT 10,
           counter INTEGER DEFAULT 1);
        """)
        conn.commit()

        # Создание таблицы growths
        cur.execute("""CREATE TABLE IF NOT EXISTS growths(
               id INTEGER PRIMARY KEY,
               prof1 INTEGER,
               prof2 INTEGER,
               counter INTEGER DEFAULT 1,
               period REAL DEFAULT 0.0);
            """)
        conn.commit()

        conn.close()
    def save_button_clicked(self):
        # При нажатии кнопки "Сохранить проект"
        dialog = QFileDialog()
        folder_path = dialog.getExistingDirectory(None, "Выберите папку для сохранения проекта")

        if folder_path:
            # Определение пути к config.json в исполняемом файле
            if getattr(sys, 'frozen', False):
                # Исполняемый файл (.exe)
                base_path = sys._MEIPASS
            else:
                # Исходный код Python
                base_path = os.path.dirname(os.path.abspath(__file__))

            # Путь для сохранения файла config.json
            config_file_path = os.path.join(folder_path, "config.json")

            # Сохранение файла config.json
            existing_json_path = os.path.join(base_path, "config.json")
            shutil.copyfile(existing_json_path, config_file_path)

            # Путь для сохранения базы данных
            database_path = os.path.join(folder_path, "database.db")

            # Создание базы данных с фиксированной структурой
            self.create_database(database_path, folder_path)

            QMessageBox.information(None, "Message", "Проект успешно сохранен.")
        else:
            QMessageBox.warning(None, "Message", "Не выбрана папка для сохранения проекта.")



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graph Editor (v.0.2)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Вершины"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Рёбра"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Визуализация"))
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
