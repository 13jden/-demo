from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import QWidget
import datetime


class MechanicalClock(QWidget):
    def __init__(self, parent=None):
        super(MechanicalClock, self).__init__(parent)
        self.setMinimumSize(200, 200)  # 设置机械时钟部件的最小尺寸

        # 创建定时器
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)  # 连接定时器的timeout信号到update槽函数
        self.timer.start(1000)  # 每1000毫秒(1秒)触发一次

    def paintEvent(self, event):
        # 获取当前时间
        time = datetime.datetime.now()
        hour = time.hour % 12  # 将小时数限制在0-11
        minute = time.minute
        second = time.second

        # 将指针和刻度的颜色设置为白色
        pointer_color = QColor(255, 255, 255)

        # 在数码管的下面绘制一个机械钟表盘显示当前时间
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 先绘制一个表盘，无边框，刻度线为白色
        painter.setPen(QColor(0, 0, 0, 0))
        painter.drawEllipse(10, 10, 180, 180)  # 位置在数码管下面

        # 移动原点到圆心
        painter.translate(100, 100)

        # 按60等分绘制刻度线
        for i in range(60):
            if i % 5 == 0:
                painter.setPen(pointer_color)
                painter.drawLine(0, -80, 0, -90)
            else:
                painter.setPen(pointer_color)
                painter.drawLine(0, -85, 0, -90)
            painter.rotate(6)
        painter.setPen(QColor(255, 255, 255))
        painter.setFont(QtGui.QFont("Arial", 12))
        painter.drawText(-11, -65, "12")
        painter.drawText(-48, -55, "11")
        painter.drawText(-72, -30, "10")
        painter.drawText(-80, 5, "9")
        painter.drawText(-65, 45, "8")
        painter.drawText(-40, 70, "7")
        painter.drawText(-5, 80, "6")
        painter.drawText(35, 70, "5")
        painter.drawText(58, 42, "4")
        painter.drawText(70, 5, "3")
        painter.drawText(60, -30, "2")
        painter.drawText(30, -55, "1")
        # 根据当前时间绘制时针
        painter.setPen(QPen(pointer_color, 4))
        painter.save()
        painter.rotate(30 * (hour + minute / 60))
        painter.drawLine(0, 0, 0, -50)
        painter.restore()
        # 根据当前时间绘制分针
        painter.setPen(QPen(pointer_color, 3))
        painter.save()
        painter.rotate(6 * (minute + second / 60))
        painter.drawLine(0, 0, 0, -70)
        painter.restore()
        # 根据当前时间绘制秒针
        painter.setPen(QPen(pointer_color, 2))
        painter.save()
        painter.rotate(6 * second)
        painter.drawLine(0, 0, 0, -80)
        painter.restore()
        painter.end()
