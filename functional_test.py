from main import MainWindow
from PyQt5 import QtCore, QtTest, QtWidgets
from pytestqt import qtbot

def test_system_valid(qtbot):
    app = QtWidgets.QApplication([])
    window = MainWindow()
    qtbot.addWidget(window)
    window.sourceText.setText("aaabbc")
    qtbot.mouseClick(window.button, QtCore.Qt.LeftButton)
    assert window.targetText.toPlainText() == "(3)a(2)b(1)c"

def test_system_invalid(qtbot):
    app = QtWidgets.QApplication([])
    window = MainWindow()
    qtbot.addWidget(window)
    window.sourceText.setText("1234567890123456789012345678901")
    qtbot.mouseClick(window.button, QtCore.Qt.LeftButton)
    assert window.targetText.toPlainText() == "длина строки не должна превышать 30 символов"

def test_system_empty(qtbot):
    app = QtWidgets.QApplication([])
    window = MainWindow()
    qtbot.addWidget(window)
    window.sourceText.setText("")
    qtbot.mouseClick(window.button, QtCore.Qt.LeftButton)
    assert window.targetText.toPlainText() == ""