from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Ui_MainWindow
import sys
    
#основная логика калькулятора
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        keyboard=(1,2,3,4,5,6,7,8,9,0,"add","sub","mul","div","tk")
        for n in keyboard:
            getattr(self.ui, 'pushButton_%s' % n).pressed.connect(lambda v=n: self.input_number(v))
        self.ui.pushButton_eq.clicked.connect(self.btnClicked_eq)
        self.ui.pushButton_m.clicked.connect(self.btnClicked_m)

    def input_number(self, v):
        if v=="add":
            lineEdit=self.ui.lineEdit.text()+"+"
        elif v=="sub":
            lineEdit=self.ui.lineEdit.text()+"-"
        elif v=="mul":
            lineEdit=self.ui.lineEdit.text()+"*"
        elif v=="div":
            lineEdit=self.ui.lineEdit.text()+"/"
        elif v=="tk":
            lineEdit=self.ui.lineEdit.text()+"."
        else:
            lineEdit=self.ui.lineEdit.text()+str(v)
        self.ui.lineEdit.setText(lineEdit)

    def btnClicked_m(self):
        del_=self.ui.lineEdit.text()[0:-1]
        self.ui.lineEdit.setText(del_)

        
    def btnClicked_eq(self):
        try:
            example=self.ui.lineEdit.text()
            result=eval(example)
            self.ui.lineEdit.setText(str(result))
        except:
            self.ui.lineEdit.setText("Err")
        

#создание приложения
app = QtWidgets.QApplication([])

#создание формы и инициализация Ui
application = mywindow()
application.show()

#чтение главного цикла
sys.exit(app.exec())
    
