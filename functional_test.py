from main import MainWindow
from PyQt5 import QtCore, QtTest, QtWidgets
from pytestqt import qtbot

def test_system(qtbot):
    app = QtWidgets.QApplication([])
    window = MainWindow()
    qtbot.addWidget(window)
    window.sourceText.setText("aaabbc")
    qtbot.mouseClick(window.button, QtCore.Qt.LeftButton)
    assert window.targetText.toPlainText() == "(3)a(2)b(1)c"