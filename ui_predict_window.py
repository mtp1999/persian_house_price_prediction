# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'predict_window.ui'
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
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_PredictWindow(object):
    def setupUi(self, PredictWindow):
        if not PredictWindow.objectName():
            PredictWindow.setObjectName(u"PredictWindow")
        PredictWindow.resize(900, 800)
        PredictWindow.setMinimumSize(QSize(900, 800))
        self.gridLayout_3 = QGridLayout(PredictWindow)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(100, 20, 100, 100)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_header = QLabel(PredictWindow)
        self.label_header.setObjectName(u"label_header")
        font = QFont()
        font.setPointSize(16)
        self.label_header.setFont(font)
        self.label_header.setStyleSheet(u"color:dimgray;")

        self.verticalLayout_5.addWidget(self.label_header)

        self.frame_predict_price = QFrame(PredictWindow)
        self.frame_predict_price.setObjectName(u"frame_predict_price")
        font1 = QFont()
        font1.setPointSize(13)
        self.frame_predict_price.setFont(font1)
        self.frame_predict_price.setStyleSheet(u"color:dimgray;")
        self.frame_predict_price.setFrameShape(QFrame.StyledPanel)
        self.frame_predict_price.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_predict_price)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.label_zone_value = QLabel(self.frame_predict_price)
        self.label_zone_value.setObjectName(u"label_zone_value")
        self.label_zone_value.setFont(font1)
        self.label_zone_value.setStyleSheet(u"color:dimgray;")
        self.label_zone_value.setAlignment(Qt.AlignCenter)
        self.label_zone_value.setMargin(0)
        self.label_zone_value.setIndent(0)

        self.verticalLayout.addWidget(self.label_zone_value)

        self.label_meter_value = QLabel(self.frame_predict_price)
        self.label_meter_value.setObjectName(u"label_meter_value")
        self.label_meter_value.setFont(font1)
        self.label_meter_value.setStyleSheet(u"color:dimgray;")
        self.label_meter_value.setAlignment(Qt.AlignCenter)
        self.label_meter_value.setMargin(0)
        self.label_meter_value.setIndent(0)

        self.verticalLayout.addWidget(self.label_meter_value)

        self.label_bedroom_value = QLabel(self.frame_predict_price)
        self.label_bedroom_value.setObjectName(u"label_bedroom_value")
        self.label_bedroom_value.setFont(font1)
        self.label_bedroom_value.setStyleSheet(u"color:dimgray;")
        self.label_bedroom_value.setAlignment(Qt.AlignCenter)
        self.label_bedroom_value.setMargin(0)
        self.label_bedroom_value.setIndent(0)

        self.verticalLayout.addWidget(self.label_bedroom_value)

        self.label_year_value = QLabel(self.frame_predict_price)
        self.label_year_value.setObjectName(u"label_year_value")
        self.label_year_value.setFont(font1)
        self.label_year_value.setStyleSheet(u"color:dimgray;")
        self.label_year_value.setAlignment(Qt.AlignCenter)
        self.label_year_value.setMargin(0)
        self.label_year_value.setIndent(0)

        self.verticalLayout.addWidget(self.label_year_value)

        self.label_predict_price_value = QLabel(self.frame_predict_price)
        self.label_predict_price_value.setObjectName(u"label_predict_price_value")
        font2 = QFont()
        font2.setPointSize(15)
        self.label_predict_price_value.setFont(font2)
        self.label_predict_price_value.setStyleSheet(u"color:teal;")
        self.label_predict_price_value.setAlignment(Qt.AlignCenter)
        self.label_predict_price_value.setMargin(0)
        self.label_predict_price_value.setIndent(0)

        self.verticalLayout.addWidget(self.label_predict_price_value)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.label_zone = QLabel(self.frame_predict_price)
        self.label_zone.setObjectName(u"label_zone")
        self.label_zone.setFont(font1)
        self.label_zone.setStyleSheet(u"color:dimgray;")
        self.label_zone.setAlignment(Qt.AlignCenter)
        self.label_zone.setMargin(0)
        self.label_zone.setIndent(0)

        self.verticalLayout_2.addWidget(self.label_zone)

        self.label_meter = QLabel(self.frame_predict_price)
        self.label_meter.setObjectName(u"label_meter")
        self.label_meter.setFont(font1)
        self.label_meter.setStyleSheet(u"color:dimgray;")
        self.label_meter.setAlignment(Qt.AlignCenter)
        self.label_meter.setMargin(0)
        self.label_meter.setIndent(0)

        self.verticalLayout_2.addWidget(self.label_meter)

        self.label_bedroom = QLabel(self.frame_predict_price)
        self.label_bedroom.setObjectName(u"label_bedroom")
        self.label_bedroom.setFont(font1)
        self.label_bedroom.setStyleSheet(u"color:dimgray;")
        self.label_bedroom.setAlignment(Qt.AlignCenter)
        self.label_bedroom.setMargin(0)
        self.label_bedroom.setIndent(0)

        self.verticalLayout_2.addWidget(self.label_bedroom)

        self.label_year = QLabel(self.frame_predict_price)
        self.label_year.setObjectName(u"label_year")
        self.label_year.setFont(font1)
        self.label_year.setStyleSheet(u"color:dimgray;")
        self.label_year.setAlignment(Qt.AlignCenter)
        self.label_year.setMargin(0)
        self.label_year.setIndent(0)

        self.verticalLayout_2.addWidget(self.label_year)

        self.label_predict_price = QLabel(self.frame_predict_price)
        self.label_predict_price.setObjectName(u"label_predict_price")
        self.label_predict_price.setFont(font2)
        self.label_predict_price.setStyleSheet(u"color:dimgray;")
        self.label_predict_price.setAlignment(Qt.AlignCenter)
        self.label_predict_price.setMargin(0)
        self.label_predict_price.setIndent(0)

        self.verticalLayout_2.addWidget(self.label_predict_price)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_predict_price)

        self.label_network_information = QLabel(PredictWindow)
        self.label_network_information.setObjectName(u"label_network_information")
        self.label_network_information.setFont(font)
        self.label_network_information.setStyleSheet(u"color:dimgray;")

        self.verticalLayout_5.addWidget(self.label_network_information)

        self.frame_network_information = QFrame(PredictWindow)
        self.frame_network_information.setObjectName(u"frame_network_information")
        font3 = QFont()
        font3.setPointSize(10)
        self.frame_network_information.setFont(font3)
        self.frame_network_information.setFrameShape(QFrame.Box)
        self.frame_network_information.setFrameShadow(QFrame.Raised)
        self.frame_network_information.setLineWidth(1)
        self.frame_network_information.setMidLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.frame_network_information)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.label_train_data_number = QLabel(self.frame_network_information)
        self.label_train_data_number.setObjectName(u"label_train_data_number")
        self.label_train_data_number.setFont(font1)
        self.label_train_data_number.setStyleSheet(u"color:dimgray;")
        self.label_train_data_number.setScaledContents(False)
        self.label_train_data_number.setAlignment(Qt.AlignCenter)
        self.label_train_data_number.setWordWrap(False)
        self.label_train_data_number.setMargin(0)
        self.label_train_data_number.setIndent(0)

        self.verticalLayout_3.addWidget(self.label_train_data_number)

        self.label_test_data_number = QLabel(self.frame_network_information)
        self.label_test_data_number.setObjectName(u"label_test_data_number")
        self.label_test_data_number.setFont(font1)
        self.label_test_data_number.setStyleSheet(u"color:dimgray;")
        self.label_test_data_number.setScaledContents(False)
        self.label_test_data_number.setAlignment(Qt.AlignCenter)
        self.label_test_data_number.setWordWrap(False)
        self.label_test_data_number.setMargin(0)
        self.label_test_data_number.setIndent(0)

        self.verticalLayout_3.addWidget(self.label_test_data_number)

        self.label_mse = QLabel(self.frame_network_information)
        self.label_mse.setObjectName(u"label_mse")
        self.label_mse.setFont(font1)
        self.label_mse.setStyleSheet(u"color:dimgray;")
        self.label_mse.setScaledContents(False)
        self.label_mse.setAlignment(Qt.AlignCenter)
        self.label_mse.setWordWrap(False)
        self.label_mse.setMargin(0)
        self.label_mse.setIndent(0)

        self.verticalLayout_3.addWidget(self.label_mse)

        self.label_rmse = QLabel(self.frame_network_information)
        self.label_rmse.setObjectName(u"label_rmse")
        self.label_rmse.setFont(font1)
        self.label_rmse.setStyleSheet(u"color:dimgray;")
        self.label_rmse.setScaledContents(False)
        self.label_rmse.setAlignment(Qt.AlignCenter)
        self.label_rmse.setWordWrap(False)
        self.label_rmse.setMargin(0)
        self.label_rmse.setIndent(0)

        self.verticalLayout_3.addWidget(self.label_rmse)

        self.label_mae = QLabel(self.frame_network_information)
        self.label_mae.setObjectName(u"label_mae")
        self.label_mae.setFont(font1)
        self.label_mae.setStyleSheet(u"color:dimgray;")
        self.label_mae.setScaledContents(False)
        self.label_mae.setAlignment(Qt.AlignCenter)
        self.label_mae.setWordWrap(False)
        self.label_mae.setMargin(0)
        self.label_mae.setIndent(0)

        self.verticalLayout_3.addWidget(self.label_mae)

        self.label_mpd = QLabel(self.frame_network_information)
        self.label_mpd.setObjectName(u"label_mpd")
        self.label_mpd.setFont(font1)
        self.label_mpd.setStyleSheet(u"color:dimgray;")
        self.label_mpd.setScaledContents(False)
        self.label_mpd.setAlignment(Qt.AlignCenter)
        self.label_mpd.setWordWrap(False)
        self.label_mpd.setMargin(0)
        self.label_mpd.setIndent(0)

        self.verticalLayout_3.addWidget(self.label_mpd)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.label_train_data_number_value = QLabel(self.frame_network_information)
        self.label_train_data_number_value.setObjectName(u"label_train_data_number_value")
        self.label_train_data_number_value.setFont(font1)
        self.label_train_data_number_value.setStyleSheet(u"color:dimgray;")
        self.label_train_data_number_value.setScaledContents(False)
        self.label_train_data_number_value.setAlignment(Qt.AlignCenter)
        self.label_train_data_number_value.setWordWrap(False)
        self.label_train_data_number_value.setMargin(0)
        self.label_train_data_number_value.setIndent(0)

        self.verticalLayout_4.addWidget(self.label_train_data_number_value)

        self.label_test_data_number_value = QLabel(self.frame_network_information)
        self.label_test_data_number_value.setObjectName(u"label_test_data_number_value")
        self.label_test_data_number_value.setFont(font1)
        self.label_test_data_number_value.setStyleSheet(u"color:dimgray;")
        self.label_test_data_number_value.setScaledContents(False)
        self.label_test_data_number_value.setAlignment(Qt.AlignCenter)
        self.label_test_data_number_value.setWordWrap(False)
        self.label_test_data_number_value.setMargin(0)
        self.label_test_data_number_value.setIndent(0)

        self.verticalLayout_4.addWidget(self.label_test_data_number_value)

        self.label_mse_value = QLabel(self.frame_network_information)
        self.label_mse_value.setObjectName(u"label_mse_value")
        self.label_mse_value.setFont(font1)
        self.label_mse_value.setStyleSheet(u"color:dimgray;")
        self.label_mse_value.setScaledContents(False)
        self.label_mse_value.setAlignment(Qt.AlignCenter)
        self.label_mse_value.setWordWrap(False)
        self.label_mse_value.setMargin(0)
        self.label_mse_value.setIndent(0)

        self.verticalLayout_4.addWidget(self.label_mse_value)

        self.label_rmse_value = QLabel(self.frame_network_information)
        self.label_rmse_value.setObjectName(u"label_rmse_value")
        self.label_rmse_value.setFont(font1)
        self.label_rmse_value.setStyleSheet(u"color:dimgray;")
        self.label_rmse_value.setScaledContents(False)
        self.label_rmse_value.setAlignment(Qt.AlignCenter)
        self.label_rmse_value.setWordWrap(False)
        self.label_rmse_value.setMargin(0)
        self.label_rmse_value.setIndent(0)

        self.verticalLayout_4.addWidget(self.label_rmse_value)

        self.label_mae_value = QLabel(self.frame_network_information)
        self.label_mae_value.setObjectName(u"label_mae_value")
        self.label_mae_value.setFont(font1)
        self.label_mae_value.setStyleSheet(u"color:dimgray;")
        self.label_mae_value.setScaledContents(False)
        self.label_mae_value.setAlignment(Qt.AlignCenter)
        self.label_mae_value.setWordWrap(False)
        self.label_mae_value.setMargin(0)
        self.label_mae_value.setIndent(0)

        self.verticalLayout_4.addWidget(self.label_mae_value)

        self.label_mpd_value = QLabel(self.frame_network_information)
        self.label_mpd_value.setObjectName(u"label_mpd_value")
        self.label_mpd_value.setFont(font1)
        self.label_mpd_value.setStyleSheet(u"color:dimgray;")
        self.label_mpd_value.setScaledContents(False)
        self.label_mpd_value.setAlignment(Qt.AlignCenter)
        self.label_mpd_value.setWordWrap(False)
        self.label_mpd_value.setMargin(0)
        self.label_mpd_value.setIndent(0)

        self.verticalLayout_4.addWidget(self.label_mpd_value)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_network_information)

        self.horizontal_layout_buttons = QHBoxLayout()
        self.horizontal_layout_buttons.setSpacing(30)
        self.horizontal_layout_buttons.setObjectName(u"horizontal_layout_buttons")
        self.horizontal_layout_buttons.setContentsMargins(-1, 30, -1, -1)
        self.button_search_house = QPushButton(PredictWindow)
        self.button_search_house.setObjectName(u"button_search_house")
        font4 = QFont()
        font4.setPointSize(14)
        self.button_search_house.setFont(font4)
        self.button_search_house.setStyleSheet(u"color:teal;\n"
"background-color:lightgray;\n"
"")

        self.horizontal_layout_buttons.addWidget(self.button_search_house)

        self.button_back = QPushButton(PredictWindow)
        self.button_back.setObjectName(u"button_back")
        self.button_back.setFont(font4)
        self.button_back.setStyleSheet(u"color:teal;\n"
"background-color:lightgray;\n"
"")

        self.horizontal_layout_buttons.addWidget(self.button_back)


        self.verticalLayout_5.addLayout(self.horizontal_layout_buttons)


        self.gridLayout_3.addLayout(self.verticalLayout_5, 0, 0, 1, 1)


        self.retranslateUi(PredictWindow)

        QMetaObject.connectSlotsByName(PredictWindow)
    # setupUi

    def retranslateUi(self, PredictWindow):
        PredictWindow.setWindowTitle(QCoreApplication.translate("PredictWindow", u"Form", None))
        self.label_header.setText(QCoreApplication.translate("PredictWindow", u"\u067e\u06cc\u0634\u0628\u06cc\u0646\u06cc \u0642\u06cc\u0645\u062a \u062e\u0627\u0646\u0647", None))
        self.label_zone_value.setText(QCoreApplication.translate("PredictWindow", u"\u062f\u0631\u062d\u0627\u0644 \u062f\u0631\u06cc\u0627\u0641\u062a \u0627\u0637\u0644\u0627\u0639\u0627\u062a", None))
        self.label_meter_value.setText(QCoreApplication.translate("PredictWindow", u"\u062f\u0631\u062d\u0627\u0644 \u062f\u0631\u06cc\u0627\u0641\u062a \u0627\u0637\u0644\u0627\u0639\u0627\u062a", None))
        self.label_bedroom_value.setText(QCoreApplication.translate("PredictWindow", u"\u062f\u0631\u062d\u0627\u0644 \u062f\u0631\u06cc\u0627\u0641\u062a \u0627\u0637\u0644\u0627\u0639\u0627\u062a", None))
        self.label_year_value.setText(QCoreApplication.translate("PredictWindow", u"\u062f\u0631\u062d\u0627\u0644 \u062f\u0631\u06cc\u0627\u0641\u062a \u0627\u0637\u0644\u0627\u0639\u0627\u062a", None))
        self.label_predict_price_value.setText(QCoreApplication.translate("PredictWindow", u"\u062f\u0631\u062d\u0627\u0644 \u062f\u0631\u06cc\u0627\u0641\u062a \u0627\u0637\u0644\u0627\u0639\u0627\u062a", None))
        self.label_zone.setText(QCoreApplication.translate("PredictWindow", u"\u0645\u0646\u0637\u0642\u0647 :", None))
        self.label_meter.setText(QCoreApplication.translate("PredictWindow", u"\u0645\u062a\u0631\u0627\u0698 :", None))
        self.label_bedroom.setText(QCoreApplication.translate("PredictWindow", u"\u062a\u0639\u062f\u0627\u062f \u0627\u062a\u0627\u0642 :", None))
        self.label_year.setText(QCoreApplication.translate("PredictWindow", u"\u0633\u0627\u0644 \u0633\u0627\u062e\u062a :", None))
        self.label_predict_price.setText(QCoreApplication.translate("PredictWindow", u"\u0642\u06cc\u0645\u062a \u067e\u06cc\u0634\u0628\u06cc\u0646\u06cc \u0634\u062f\u0647 \u062e\u0627\u0646\u0647 \u0645\u0648\u0631\u062f \u0646\u0638\u0631 :", None))
        self.label_network_information.setText(QCoreApplication.translate("PredictWindow", u"\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u0634\u0628\u06a9\u0647 \u06cc\u0627\u062f\u06af\u06cc\u0631\u06cc", None))
        self.label_train_data_number.setText(QCoreApplication.translate("PredictWindow", u"Number of train data : ", None))
        self.label_test_data_number.setText(QCoreApplication.translate("PredictWindow", u"Number of test data : ", None))
        self.label_mse.setText(QCoreApplication.translate("PredictWindow", u"Mean squared error :", None))
        self.label_rmse.setText(QCoreApplication.translate("PredictWindow", u"Root mean squared error :", None))
        self.label_mae.setText(QCoreApplication.translate("PredictWindow", u"Mean absolute error :", None))
        self.label_mpd.setText(QCoreApplication.translate("PredictWindow", u"Mean poisson deviance :", None))
        self.label_train_data_number_value.setText(QCoreApplication.translate("PredictWindow", u"processing", None))
        self.label_test_data_number_value.setText(QCoreApplication.translate("PredictWindow", u"processing", None))
        self.label_mse_value.setText(QCoreApplication.translate("PredictWindow", u"processing", None))
        self.label_rmse_value.setText(QCoreApplication.translate("PredictWindow", u"processing", None))
        self.label_mae_value.setText(QCoreApplication.translate("PredictWindow", u"processing", None))
        self.label_mpd_value.setText(QCoreApplication.translate("PredictWindow", u"processing", None))
        self.button_search_house.setText(QCoreApplication.translate("PredictWindow", u"\u062c\u0633\u062a \u0648 \u062c\u0648\u06cc \u062e\u0627\u0646\u0647", None))
        self.button_back.setText(QCoreApplication.translate("PredictWindow", u"\u0628\u0627\u0632\u06af\u0634\u062a", None))
    # retranslateUi

