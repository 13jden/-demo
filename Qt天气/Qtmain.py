# -*- coding: utf-8 -*-
import datetime
import time

import ntplib
import requests
# Form implementation generated from reading ui file 'main1106.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from MechanicalClock import MechanicalClock


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 514)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"    background-color:rgb(255, 85, 0);\n"
"border-radius:30px ;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"    padding:8px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(255, 149, 0);\n"
"    border-radius:8px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 149, 0,80%);\n"
"border:2px outset rgba(36, 36, 36,0);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 149, 0,100%);\n"
"border:4px outset rgba(36, 36, 36,0);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setContentsMargins(24, 24, 24, 24)
        self.verticalLayout_6.setSpacing(12)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(42)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4.addWidget(self.frame_4)
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_4.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_4.addWidget(self.label_15)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setMinimumSize(QtCore.QSize(0, 2))
        self.line.setMaximumSize(QtCore.QSize(16777215, 2))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 64))
        self.frame_2.setStyleSheet("image: url(:/buttom_white/img/buttom_white/雷雨_thunderstorm.svg);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_16 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_7.addWidget(self.label_16)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 64))
        self.frame_3.setStyleSheet("image: url(:/buttom_white/img/buttom_white/雷雨_thunderstorm.svg);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3.addWidget(self.frame_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_17 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_8.addWidget(self.label_17)
        self.label_6 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.label_7 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)

        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_7.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 添加机械时钟部件到verticalLayout_5
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_7.addLayout(self.verticalLayout_5)


        # 将MechanicalClock实例添加到verticalLayout_5
        self.clock_widget = MechanicalClock(self.centralwidget)
        # self.verticalLayout_5.addWidget(self.clock_widget)
        self.clock_widget.setGeometry(800, 20, 200, 200)

        MainWindow.setCentralWidget(self.centralwidget)
        # 设置定时器每秒更新时间
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_current_time)
        self.timer.start(1000)  # 1000毫秒 = 1秒

        # 每天同步时间
        self.sync_time_ntp()  # 同步时间一次
        self.timer_sync = QtCore.QTimer()
        self.timer_sync.timeout.connect(self.sync_time_ntp)
        self.timer_sync.start(1000 * 60 * 60 * 24)  # 24小时后执行一次


        # 更新天气数据
        self.fetch_weather_data()
    def fetch_weather_data(self):
                url = "https://api.seniverse.com/v3/weather/daily.json"
                params = {
                        "key": "StNpolda4k1SpZReD",
                        "location": "hangzhou",
                        "language": "zh-Hans",
                        "unit": "c",
                        "start": 0,
                        "days": 5
                }
                response = requests.get(url, params=params)
                return response.json()
                # 更新每小时天气
                self.update_weather_data(weather_data)

    def sync_time_ntp(self):
        try:
            # 连接到NTP服务器
            ntp_client = ntplib.NTPClient()
            response = ntp_client.request('ntp.aliyun.com')
            # 获取NTP服务器返回的时间戳
            ntp_time = datetime.datetime.fromtimestamp(response.tx_time)
            # 将系统时间调整为NTP服务器返回的时间
            datetime.datetime.now().replace(year=ntp_time.year, month=ntp_time.month, day=ntp_time.day,
                                            hour=ntp_time.hour, minute=ntp_time.minute, second=ntp_time.second)
            print("系统时间已校准为:", datetime.datetime.now())

        except Exception as e:
            print("时间同步失败:", e)
    def update_current_time(self):
                current_time = time.localtime()
                formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
                day_of_week = time.strftime("%A", current_time)
                self.label_2.setText(formatted_time)
                self.label.setText(day_of_week)

    def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                # 更新当前时间
                self.update_current_time()

                weather_data = self.fetch_weather_data()
                daily_data = weather_data["results"][0]["daily"]

                # 更新每一天的天气信息
                labels = [
                        (self.label_15, self.label_14, self.label_3),
                        (self.label_16, self.label_5, self.label_4),
                        (self.label_17, self.label_6, self.label_7),
                ]
                tq1 = daily_data[0]["text_day"]
                print(tq1)
                self.frame_4.setStyleSheet(f"image: url('img/{tq1}.png'); padding-left: -30px;")


                tq2 = daily_data[1]["text_day"]
                print(tq2)
                self.frame_2.setStyleSheet(f"image: url('img/{tq2}.png');")

                tq3 = daily_data[2]["text_day"]
                print(tq3)
                self.frame_3.setStyleSheet(f"image: url('img/{tq3}.png');")

                for i, (date_label, weather_label, temp_label) in enumerate(labels):
                        if i < len(daily_data):
                                date_label.setText(_translate("MainWindow", daily_data[i]["date"]))
                                weather_label.setText(_translate("MainWindow", daily_data[i]["text_day"]))
                                temp_label.setText(
                                        _translate("MainWindow", f'{daily_data[i]["low"]}～{daily_data[i]["high"]}℃'))
                        else:
                                date_label.setText(_translate("MainWindow", "无数据"))
                                weather_label.setText(_translate("MainWindow", "无数据"))
                                temp_label.setText(_translate("MainWindow", "无数据"))

    import resources_rc

if __name__ == "__main__":
            import sys
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())
