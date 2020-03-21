from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from design import Ui_MainWindow
import sys
from counter import Counter, InvalidLengthException
from validator import LengthValidator
            

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.button.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        text = self.sourceText.toPlainText()
        try:
            validator = LengthValidator(30)
            counter = Counter(validator)
            self.targetText.setPlainText(counter.count_repeated(text))
        except InvalidLengthException:
            self.targetText.setPlainText("длина строки не должна превышать 30 символов")
 
def main():
    app = QtWidgets.QApplication([])
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()