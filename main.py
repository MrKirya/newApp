from PyQt6 import QtCore, QtGui, QtWidgets

class CreateProjectDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Создать проект")

        # Создаем 4 поля для ввода данных
        self.line_edit_1 = QtWidgets.QLineEdit(self)
        self.line_edit_2 = QtWidgets.QLineEdit(self)
        self.line_edit_3 = QtWidgets.QLineEdit(self)
        self.line_edit_4 = QtWidgets.QLineEdit(self)

        # Создаем кнопки для сохранения и отмены
        self.button_save = QtWidgets.QPushButton("Сохранить", self)
        self.button_cancel = QtWidgets.QPushButton("Отмена", self)

        # Устанавливаем лейаут для расположения элементов на окне
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.line_edit_1)
        layout.addWidget(self.line_edit_2)
        layout.addWidget(self.line_edit_3)
        layout.addWidget(self.line_edit_4)
        layout.addWidget(self.button_save)
        layout.addWidget(self.button_cancel)

        # Устанавливаем обработчики событий для кнопок
        self.button_save.clicked.connect(self.save_clicked)
        self.button_cancel.clicked.connect(self.reject)

    def save_clicked(self):
        # Сохраняем данные из полей в переменные
        name = self.line_edit_1.text()
        date = self.line_edit_2.text()
        author = self.line_edit_3.text()
        description = self.line_edit_4.text()

        # Передаем названия колонок в таблице
        column_names = ('id', name, author, description)

        # Закрываем окно
        self.accept()


class Ui_Dialog(object):
    def __init__(self):
        self.buttonCancel = None
        self.buttonSave = None
        self.comboBox = None
        self.selectedValue = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("")
        self.comboBox = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox.setGeometry(QtCore.QRect(140, 90, 121, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.buttonSave = QtWidgets.QPushButton(parent=Dialog)
        self.buttonSave.setGeometry(QtCore.QRect(210, 230, 75, 24))
        self.buttonSave.setObjectName("buttonSave")
        self.buttonCancel = QtWidgets.QPushButton(parent=Dialog)
        self.buttonCancel.setGeometry(QtCore.QRect(290, 230, 75, 24))
        self.buttonCancel.setObjectName("buttonCancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # устанавливаем обработчики событий для кнопок
        self.buttonSave.clicked.connect(self.saveClicked)
        self.buttonSave.clicked.connect(Dialog.close)
        self.buttonCancel.clicked.connect(Dialog.close)
        self.comboBox.currentIndexChanged.connect(self.selectionChanged)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "Список функций"))
        self.comboBox.setItemText(1, _translate("Dialog", "Создать проект"))
        self.comboBox.setItemText(2, _translate("Dialog", "Сохранить проект"))
        self.comboBox.setItemText(3, _translate("Dialog", "Открыть проект"))
        self.buttonSave.setText(_translate("Dialog", "OK"))
        self.buttonCancel.setText(_translate("Dialog", "Cancel"))

    def selectionChanged(self, index):
        # сохраняем выбранное значение
        self.selectedValue = self.comboBox.currentText()

        # проверяем, было ли выбрано "Создать проект"
        if self.selectedValue == "Создать проект":
            # Создаем новое окно для ввода данных
            create_project_dialog = CreateProjectDialog()

            # Показываем окно и ждем, пока пользователь введет данные
            if create_project_dialog.exec() == QtWidgets.QDialog.Accepted:
                # Если пользователь нажал "Сохранить", то сохраняем данные
                # и продолжаем выполнение программы
                column_names = create_project_dialog.column_names
                print(column_names)

    def saveClicked(self):
        if self.selectedValue:
            print(self.selectedValue)
            QtWidgets.QDialog().done(0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
