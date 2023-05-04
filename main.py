from PyQt6 import QtCore, QtGui, QtWidgets


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
        self.comboBox.setItemText(0, _translate("Dialog", "Создать проект"))
        self.comboBox.setItemText(1, _translate("Dialog", "Открыть проект"))
        self.comboBox.setItemText(2, _translate("Dialog", "Сохранить проект"))
        self.buttonSave.setText(_translate("Dialog", "OK"))
        self.buttonCancel.setText(_translate("Dialog", "Cancel"))

    def selectionChanged(self, index):
        # сохраняем выбранное значение
        self.selectedValue = self.comboBox.currentText()

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
