from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QPainter, QPen, QColor, QPolygon
from PyQt5.QtCore import Qt, QPoint, QPointF
import random
import math
 
class MainWindow(QWidget):
    
    def __init__(self, title, x, y, width, height):
        super(MainWindow, self).__init__()
        
        self.setGeometry(x, y, width, height)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon("1.jpeg"))
 
        self.initGUI()
 
    def initGUI(self):
 
        #upperLay
 
        uWidget = MyDrawWidget()
 
        #lowerLay
 
        names = ["Треугольники", "Прямоугольники", "Круги", "Линии", "Текст", "Многоугольники"]
        self.btns = []
 
        lLay = QHBoxLayout()
        for i, name in enumerate(names):
            btn = QPushButton(name)
            btn.clicked.connect(lambda ch, i=i: self.btnClicked(uWidget, i))
            lLay.addWidget(btn)
            self.btns.append(btn)
 
        lWidget = QWidget()
        lWidget.setLayout(lLay)
 
        #mainLay
 
        mLay = QVBoxLayout()
        mLay.addWidget(uWidget, 9)
        mLay.addWidget(lWidget, 1)
 
        self.setLayout(mLay)
 
    def btnClicked(self, uWidget, i):
 
        uWidget.myFlag = i
        self.update()
 
class MyDrawWidget(QWidget):
    
    def __init__(self):
        super(MyDrawWidget, self).__init__()
 
        self.myFlag = -1
 
    def paintEvent(self, e):
 
        qp = QPainter()
        qp.begin(self)
        for i in range(30):
            self.drawSomething(qp, i)
        qp.end()
 
    def drawSomething(self, qp, i):
 
        if self.myFlag == -1:
            return
        
        elif self.myFlag == 0:
            r, g, b, a = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            qp.setBrush(QColor(r, g, b, a))
            a, b = random.randint(0, self.width()), random.randint(0, self.height())
            c, d = random.randint(0, self.width()), random.randint(0, self.height())
            e, f = random.randint(0, self.width()), random.randint(0, self.height())
            points = QPolygon([
                QPoint(a, b),
                QPoint(c, d),
                QPoint(e, f)])
            qp.drawPolygon(points)
            
        elif self.myFlag == 1:
            r, g, b, a = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            qp.setBrush(QColor(r, g, b, a))
            x, y = random.randint(0, self.width()), random.randint(0, self.height())
            x2, y2 = random.randint(0, self.width()), random.randint(0, self.height())
            points = QPolygon([
                QPoint(x, y),
                QPoint(x, y2),
                QPoint(x2, y2),
                QPoint(x2, y)])
            qp.drawPolygon(points)
            #a, b = random.randint(0, self.width()), random.randint(0, self.height())
            #w, h = random.randint(1, self.width()-a), random.randint(1, self.height()-b)
            #qp.drawRect(a, b, w, h)
 
        elif self.myFlag == 2:
            r, g, b, a = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            qp.setBrush(QColor(r, g, b, a))
            x, y = random.randint(1, self.width()-2), random.randint(1, self.height()-2)
            if x < self.width()//2:
                w = random.randint(1, x)
            else:
                w = random.randint(1, self.width()-x-1)
            if y < self.height()//2:
                h = random.randint(1, y)
            else:
                h = random.randint(1, self.height()-y-1)
            qp.drawEllipse(QPoint(x, y), w, h)
            
        elif self.myFlag == 3:
            #pen = QPen(Qt.black, 1, Qt.SolidLine)
            #qp.setPen(pen)
            a, b = random.randint(0, self.width()), random.randint(0, self.height())
            c, d = random.randint(0, self.width()), random.randint(0, self.height())
            qp.drawLine(a, b, c ,d)
 
        elif self.myFlag == 4:
            r, g, b, a = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            qp.setBrush(QColor(r, g, b, a))
            x, y = random.randint(0, self.width()-50), random.randint(0, self.height()-50)
            qp.drawText(x, y, "Hello, world!")
 
        elif self.myFlag == 5:
            r, g, b, a = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            qp.setBrush(QColor(r, g, b, a))
            num = random.randint(3, 10)
            radius = random.randint(1, 100)
            centerX, centerY = random.randint(1, self.width()), random.randint(1, self.height())
            w = 360 // num
            points = []
            for i in range(num):
                t = w*i
                x = radius*math.cos(math.radians(t))
                y = radius*math.sin(math.radians(t))
                points.append(QPoint(math.ceil(centerX+x), math.ceil(centerY+y)))
            points = QPolygon(points)
            qp.drawPolygon(points)
 
if __name__ == "__main__":
    
    import sys
 
    app = QApplication(sys.argv)
    deskX, deskY = QApplication.desktop().width(), QApplication.desktop().height()
    
    window = MainWindow("Лабораторная 4", deskX//2-500, deskY//2-400, 1000, 800)
    window.show()
    sys.exit(app.exec())
