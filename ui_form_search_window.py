# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_search_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_FormSearchWindow(object):
    def setupUi(self, FormSearchWindow):
        if not FormSearchWindow.objectName():
            FormSearchWindow.setObjectName(u"FormSearchWindow")
        FormSearchWindow.resize(900, 800)
        FormSearchWindow.setMinimumSize(QSize(900, 800))
        FormSearchWindow.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(FormSearchWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(100, 20, 100, 100)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_header = QLabel(FormSearchWindow)
        self.label_header.setObjectName(u"label_header")
        font = QFont()
        font.setPointSize(24)
        self.label_header.setFont(font)
        self.label_header.setLayoutDirection(Qt.RightToLeft)
        self.label_header.setStyleSheet(u"QLabel{\n"
"	color:dimgray;\n"
"}")
        self.label_header.setFrameShape(QFrame.NoFrame)
        self.label_header.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_header.setIndent(0)

        self.verticalLayout.addWidget(self.label_header)

        self.label_information = QLabel(FormSearchWindow)
        self.label_information.setObjectName(u"label_information")
        font1 = QFont()
        font1.setPointSize(16)
        self.label_information.setFont(font1)
        self.label_information.setStyleSheet(u"QLabel{\n"
"	color:dimgray;\n"
"}")
        self.label_information.setMargin(0)

        self.verticalLayout.addWidget(self.label_information)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(40)
        self.gridLayout.setContentsMargins(100, 25, 100, 50)
        self.input_max_meter = QLineEdit(FormSearchWindow)
        self.input_max_meter.setObjectName(u"input_max_meter")
        font2 = QFont()
        font2.setPointSize(14)
        self.input_max_meter.setFont(font2)
        self.input_max_meter.setStyleSheet(u"background-color: white;\n"
"color: dimgray;")
        self.input_max_meter.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.input_max_meter, 2, 0, 1, 1)

        self.label_max_meter = QLabel(FormSearchWindow)
        self.label_max_meter.setObjectName(u"label_max_meter")
        self.label_max_meter.setFont(font1)
        self.label_max_meter.setStyleSheet(u"color: dimgray;\n"
"")

        self.gridLayout.addWidget(self.label_max_meter, 2, 1, 1, 1)

        self.input_zone_code = QLineEdit(FormSearchWindow)
        self.input_zone_code.setObjectName(u"input_zone_code")
        self.input_zone_code.setFont(font2)
        self.input_zone_code.setStyleSheet(u"background-color: white;\n"
"color: dimgray;")
        self.input_zone_code.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.input_zone_code, 0, 0, 1, 1)

        self.input_min_price = QLineEdit(FormSearchWindow)
        self.input_min_price.setObjectName(u"input_min_price")
        self.input_min_price.setFont(font2)
        self.input_min_price.setStyleSheet(u"background-color: white;\n"
"color: dimgray;")

        self.gridLayout.addWidget(self.input_min_price, 3, 0, 1, 1)

        self.input_min_meter = QLineEdit(FormSearchWindow)
        self.input_min_meter.setObjectName(u"input_min_meter")
        self.input_min_meter.setFont(font2)
        self.input_min_meter.setStyleSheet(u"background-color: white;\n"
"color: dimgray;")
        self.input_min_meter.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.input_min_meter, 1, 0, 1, 1)

        self.label_max_price = QLabel(FormSearchWindow)
        self.label_max_price.setObjectName(u"label_max_price")
        self.label_max_price.setFont(font1)
        self.label_max_price.setStyleSheet(u"color: dimgray;\n"
"")

        self.gridLayout.addWidget(self.label_max_price, 4, 1, 1, 1)

        self.label_zone_code = QLabel(FormSearchWindow)
        self.label_zone_code.setObjectName(u"label_zone_code")
        self.label_zone_code.setFont(font1)
        self.label_zone_code.setStyleSheet(u"color: dimgray;\n"
"")

        self.gridLayout.addWidget(self.label_zone_code, 0, 1, 1, 1)

        self.button_submit = QPushButton(FormSearchWindow)
        self.button_submit.setObjectName(u"button_submit")
        self.button_submit.setMinimumSize(QSize(0, 0))
        self.button_submit.setFont(font2)
        self.button_submit.setStyleSheet(u"background-color: lightgray;\n"
"color: teal;")
        self.button_submit.setAutoDefault(False)
        self.button_submit.setFlat(False)

        self.gridLayout.addWidget(self.button_submit, 5, 0, 1, 1)

        self.label_min_meter = QLabel(FormSearchWindow)
        self.label_min_meter.setObjectName(u"label_min_meter")
        self.label_min_meter.setFont(font1)
        self.label_min_meter.setStyleSheet(u"color: dimgray;\n"
"")

        self.gridLayout.addWidget(self.label_min_meter, 1, 1, 1, 1)

        self.label_min_price = QLabel(FormSearchWindow)
        self.label_min_price.setObjectName(u"label_min_price")
        self.label_min_price.setFont(font1)
        self.label_min_price.setStyleSheet(u"color: dimgray;\n"
"")

        self.gridLayout.addWidget(self.label_min_price, 3, 1, 1, 1)

        self.input_max_price = QLineEdit(FormSearchWindow)
        self.input_max_price.setObjectName(u"input_max_price")
        self.input_max_price.setFont(font2)
        self.input_max_price.setStyleSheet(u"background-color: white;\n"
"color: dimgray;")

        self.gridLayout.addWidget(self.input_max_price, 4, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.button_zone_list = QPushButton(FormSearchWindow)
        self.button_zone_list.setObjectName(u"button_zone_list")
        self.button_zone_list.setFont(font2)
        self.button_zone_list.setStyleSheet(u"background-color: lightgray;\n"
"color: teal;")

        self.horizontalLayout.addWidget(self.button_zone_list)

        self.button_predict_price = QPushButton(FormSearchWindow)
        self.button_predict_price.setObjectName(u"button_predict_price")
        self.button_predict_price.setFont(font2)
        self.button_predict_price.setStyleSheet(u"background-color: lightgray;\n"
"color: teal;")

        self.horizontalLayout.addWidget(self.button_predict_price)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(FormSearchWindow)

        self.button_submit.setDefault(False)


        QMetaObject.connectSlotsByName(FormSearchWindow)
    # setupUi

    def retranslateUi(self, FormSearchWindow):
        FormSearchWindow.setWindowTitle(QCoreApplication.translate("FormSearchWindow", u"\u0641\u0631\u0645 \u0627\u0637\u0644\u0627\u0639\u0627\u062a", None))
        self.label_header.setText(QCoreApplication.translate("FormSearchWindow", u"\u062c\u0633\u062a \u0648 \u062c\u0648\u06cc \u062e\u0627\u0646\u0647", None))
        self.label_information.setText(QCoreApplication.translate("FormSearchWindow", u"\u062f\u0631 \u0641\u0631\u0645 \u0632\u06cc\u0631 \u0627\u0637\u0644\u0627\u0639\u0627\u062a \u062e\u0627\u0646\u0647 \u0645\u0648\u0631\u062f\u0646\u0638\u0631 \u062e\u0648\u062f \u0631\u0627  \u0648\u0627\u0631\u062f \u06a9\u0646\u06cc\u062f :", None))
        self.label_max_meter.setText(QCoreApplication.translate("FormSearchWindow", u"\u062d\u062f\u0627\u06a9\u062b\u0631 \u0645\u062a\u0631\u0627\u0698 :", None))
        self.label_max_price.setText(QCoreApplication.translate("FormSearchWindow", u"\u062d\u062f\u0627\u06a9\u062b\u0631 \u0642\u06cc\u0645\u062a(\u0645\u06cc\u0644\u06cc\u0627\u0631\u062f \u062a\u0648\u0645\u0627\u0646) :", None))
        self.label_zone_code.setText(QCoreApplication.translate("FormSearchWindow", u"\u06a9\u062f \u0645\u0646\u0637\u0642\u0647 :", None))
        self.button_submit.setText(QCoreApplication.translate("FormSearchWindow", u"\u0627\u0631\u0633\u0627\u0644", None))
        self.label_min_meter.setText(QCoreApplication.translate("FormSearchWindow", u"\u062d\u062f\u0627\u0642\u0644 \u0645\u062a\u0631\u0627\u0698 :", None))
        self.label_min_price.setText(QCoreApplication.translate("FormSearchWindow", u"\u062d\u062f\u0627\u0642\u0644 \u0642\u06cc\u0645\u062a(\u0645\u06cc\u0644\u06cc\u0627\u0631\u062f \u062a\u0648\u0645\u0627\u0646) :", None))
        self.button_zone_list.setText(QCoreApplication.translate("FormSearchWindow", u"\u0644\u06cc\u0633\u062a \u0645\u0646\u0627\u0637\u0642", None))
        self.button_predict_price.setText(QCoreApplication.translate("FormSearchWindow", u"\u067e\u06cc\u0634\u0628\u06cc\u0646\u06cc \u0642\u06cc\u0645\u062a \u062e\u0627\u0646\u0647", None))
    # retranslateUi

