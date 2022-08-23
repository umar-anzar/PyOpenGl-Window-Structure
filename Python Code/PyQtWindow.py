import PyQt5.QtCore as QtCore
from PyQt5 import QtWidgets
from GL_window import GLWidget
import sys

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self) -> QtWidgets.QMainWindow:
        super().__init__()
        self.windowSetting()

        self.windowObject()
        self.GL_window.show()
        self.setCentralWidget(self.central_widget)

        #For multiThreading
        self.timer = QtCore.QTimer()
        self.animate = True

        #Button functions
        self.Btn_clear.clicked.connect(self.closeEvent)
        self.Btn_draw.clicked.connect(self.animation)

    def windowSetting(self) -> None:
        self.setWindowTitle("B19102104 Muhammad Umar Anzar")
        self.resize(800,600)
        self.center()

    def center(self) -> None:
        #Determines the center of screen
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        x,y = cp.x() , cp.y()
        #Center the window
        x = x - self.width()//2
        y = y - self.height()//2
        #apply new axis
        self.move(x,y)


    def windowObject(self) -> None:
       
        self.central_widget = QtWidgets.QWidget(self)
        self.GL_window = GLWidget(self.central_widget)
        self.Btn_clear = QtWidgets.QPushButton("Animation Off",self.central_widget)
        self.Btn_draw = QtWidgets.QPushButton("Animation ON",self.central_widget)

        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.central_widget)
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()

        self.verticalLayout1.addWidget(self.GL_window)
        self.verticalLayout1.addLayout(self.horizontalLayout1)
        self.horizontalLayout1.addWidget(self.Btn_draw)
        self.horizontalLayout1.addWidget(self.Btn_clear)

    def animation(self):
        #Function That uses Qtimer multiThreading to Animated The OpenGl Widget
        if self.animate:
            self.timer.timeout.connect(self.GL_window.update) #Updating OpenGl Widget

            #Starts or restarts the timer with a timeout interval of msec milliseconds. Like setting FPS
            self.timer.start(20)
            self.animate = False

    def closeEvent(self, event): # WHEN window is closed Automatically Qtimer is stopped.
        self.animate = True
        self.timer.stop()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
