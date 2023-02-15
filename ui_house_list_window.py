# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'house_list_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_HouseListWindow(object):
    def setupUi(self, HouseListWindow):
        if not HouseListWindow.objectName():
            HouseListWindow.setObjectName(u"HouseListWindow")
        HouseListWindow.resize(900, 800)
        HouseListWindow.setMinimumSize(QSize(900, 800))
        HouseListWindow.setLayoutDirection(Qt.LeftToRight)
        HouseListWindow.setStyleSheet(u"")
        self.grid_layout = QGridLayout(HouseListWindow)
        self.grid_layout.setObjectName(u"grid_layout")
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setSpacing(15)
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.vertical_layout.setContentsMargins(50, 0, 50, 50)
        self.label_header = QLabel(HouseListWindow)
        self.label_header.setObjectName(u"label_header")
        font = QFont()
        font.setPointSize(16)
        self.label_header.setFont(font)
        self.label_header.setStyleSheet(u"color:dimgray")
        self.label_header.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_header.setWordWrap(False)
        self.label_header.setMargin(10)
        self.label_header.setIndent(0)

        self.vertical_layout.addWidget(self.label_header)

        self.table_houses = QTableWidget(HouseListWindow)
        if (self.table_houses.columnCount() < 5):
            self.table_houses.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_houses.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_houses.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_houses.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_houses.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_houses.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.table_houses.rowCount() < 3):
            self.table_houses.setRowCount(3)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_houses.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_houses.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_houses.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_houses.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_houses.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_houses.setItem(0, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_houses.setItem(0, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_houses.setItem(0, 4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_houses.setItem(1, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_houses.setItem(1, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_houses.setItem(1, 2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_houses.setItem(1, 3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_houses.setItem(1, 4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_houses.setItem(2, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_houses.setItem(2, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_houses.setItem(2, 2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_houses.setItem(2, 3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_houses.setItem(2, 4, __qtablewidgetitem22)
        self.table_houses.setObjectName(u"table_houses")
        self.table_houses.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_houses.sizePolicy().hasHeightForWidth())
        self.table_houses.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        self.table_houses.setFont(font1)
        self.table_houses.setAcceptDrops(False)
        self.table_houses.setLayoutDirection(Qt.RightToLeft)
        self.table_houses.setAutoFillBackground(False)
        self.table_houses.setStyleSheet(u"background-color: white;\n"
"color: dimgray;\n"
"\n"
"")
        self.table_houses.setFrameShape(QFrame.Box)
        self.table_houses.setFrameShadow(QFrame.Sunken)
        self.table_houses.setLineWidth(1)
        self.table_houses.setMidLineWidth(3)
        self.table_houses.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.table_houses.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_houses.setTabKeyNavigation(False)
        self.table_houses.setProperty("showDropIndicator", False)
        self.table_houses.setDragDropOverwriteMode(False)
        self.table_houses.setAlternatingRowColors(True)
        self.table_houses.setSelectionMode(QAbstractItemView.NoSelection)
        self.table_houses.setTextElideMode(Qt.ElideMiddle)
        self.table_houses.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table_houses.setShowGrid(True)
        self.table_houses.setGridStyle(Qt.SolidLine)
        self.table_houses.setSortingEnabled(False)
        self.table_houses.setWordWrap(True)
        self.table_houses.setCornerButtonEnabled(True)
        self.table_houses.setRowCount(3)
        self.table_houses.horizontalHeader().setVisible(True)
        self.table_houses.horizontalHeader().setCascadingSectionResizes(True)
        self.table_houses.horizontalHeader().setMinimumSectionSize(145)
        self.table_houses.horizontalHeader().setDefaultSectionSize(145)
        self.table_houses.horizontalHeader().setHighlightSections(True)
        self.table_houses.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_houses.horizontalHeader().setStretchLastSection(True)
        self.table_houses.verticalHeader().setVisible(False)
        self.table_houses.verticalHeader().setCascadingSectionResizes(False)
        self.table_houses.verticalHeader().setMinimumSectionSize(70)
        self.table_houses.verticalHeader().setDefaultSectionSize(70)
        self.table_houses.verticalHeader().setHighlightSections(True)
        self.table_houses.verticalHeader().setProperty("showSortIndicator", False)
        self.table_houses.verticalHeader().setStretchLastSection(True)

        self.vertical_layout.addWidget(self.table_houses)

        self.horizontal_layout_buttons = QHBoxLayout()
        self.horizontal_layout_buttons.setSpacing(30)
        self.horizontal_layout_buttons.setObjectName(u"horizontal_layout_buttons")
        self.button_predict_price = QPushButton(HouseListWindow)
        self.button_predict_price.setObjectName(u"button_predict_price")
        font2 = QFont()
        font2.setPointSize(14)
        self.button_predict_price.setFont(font2)
        self.button_predict_price.setStyleSheet(u"background-color: lightgray;\n"
"color: teal;")

        self.horizontal_layout_buttons.addWidget(self.button_predict_price)

        self.button_back = QPushButton(HouseListWindow)
        self.button_back.setObjectName(u"button_back")
        self.button_back.setFont(font2)
        self.button_back.setStyleSheet(u"background-color: lightgray;\n"
"color: teal;")

        self.horizontal_layout_buttons.addWidget(self.button_back)


        self.vertical_layout.addLayout(self.horizontal_layout_buttons)


        self.grid_layout.addLayout(self.vertical_layout, 0, 0, 1, 1)


        self.retranslateUi(HouseListWindow)

        QMetaObject.connectSlotsByName(HouseListWindow)
    # setupUi

    def retranslateUi(self, HouseListWindow):
        HouseListWindow.setWindowTitle(QCoreApplication.translate("HouseListWindow", u"\u067e\u06cc\u0634\u0628\u06cc\u0646\u06cc \u0642\u06cc\u0645\u062a \u062e\u0627\u0646\u0647", None))
        self.label_header.setText(QCoreApplication.translate("HouseListWindow", u"\u062e\u0627\u0646\u0647 \u0647\u0627\u06cc \u06cc\u0627\u0641\u062a \u0634\u062f\u0647 \u062f\u0631 \u0645\u0646\u0637\u0642\u0647 \u0633\u0639\u0627\u062f\u062a \u0622\u0628\u0627\u062f", None))
        ___qtablewidgetitem = self.table_houses.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("HouseListWindow", u"\u0642\u06cc\u0645\u062a(\u062a\u0648\u0645\u0627\u0646)", None));
        ___qtablewidgetitem1 = self.table_houses.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("HouseListWindow", u"\u0642\u06cc\u0645\u062a \u0647\u0631 \u0645\u062a\u0631(\u062a\u0648\u0645\u0627\u0646)", None));
        ___qtablewidgetitem2 = self.table_houses.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("HouseListWindow", u"\u0645\u062a\u0631\u0627\u0698", None));
        ___qtablewidgetitem3 = self.table_houses.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("HouseListWindow", u"\u062a\u0639\u062f\u0627\u062f \u0627\u062a\u0627\u0642", None));
        ___qtablewidgetitem4 = self.table_houses.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("HouseListWindow", u"\u0633\u0627\u0644 \u0633\u0627\u062e\u062a", None));
        ___qtablewidgetitem5 = self.table_houses.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("HouseListWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.table_houses.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("HouseListWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.table_houses.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("HouseListWindow", u"New Row", None));

        __sortingEnabled = self.table_houses.isSortingEnabled()
        self.table_houses.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.table_houses.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("HouseListWindow", u"11000000000", None));
        ___qtablewidgetitem9 = self.table_houses.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("HouseListWindow", u"150000000", None));
        ___qtablewidgetitem10 = self.table_houses.item(0, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("HouseListWindow", u"200", None));
        ___qtablewidgetitem11 = self.table_houses.item(0, 3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("HouseListWindow", u"4", None));
        ___qtablewidgetitem12 = self.table_houses.item(0, 4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("HouseListWindow", u"1401", None));
        ___qtablewidgetitem13 = self.table_houses.item(1, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("HouseListWindow", u"15661661616", None));
        ___qtablewidgetitem14 = self.table_houses.item(1, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("HouseListWindow", u"522550000", None));
        ___qtablewidgetitem15 = self.table_houses.item(1, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("HouseListWindow", u"150", None));
        ___qtablewidgetitem16 = self.table_houses.item(1, 3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("HouseListWindow", u"3", None));
        ___qtablewidgetitem17 = self.table_houses.item(1, 4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("HouseListWindow", u"1392", None));
        ___qtablewidgetitem18 = self.table_houses.item(2, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("HouseListWindow", u"15550000000", None));
        ___qtablewidgetitem19 = self.table_houses.item(2, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("HouseListWindow", u"100000000", None));
        ___qtablewidgetitem20 = self.table_houses.item(2, 2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("HouseListWindow", u"175", None));
        ___qtablewidgetitem21 = self.table_houses.item(2, 3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("HouseListWindow", u"4", None));
        ___qtablewidgetitem22 = self.table_houses.item(2, 4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("HouseListWindow", u"1369", None));
        self.table_houses.setSortingEnabled(__sortingEnabled)

        self.button_predict_price.setText(QCoreApplication.translate("HouseListWindow", u"\u067e\u06cc\u0634\u0628\u06cc\u0646\u06cc \u0642\u06cc\u0645\u062a", None))
        self.button_back.setText(QCoreApplication.translate("HouseListWindow", u"\u0628\u0627\u0632\u06af\u0634\u062a", None))
    # retranslateUi

