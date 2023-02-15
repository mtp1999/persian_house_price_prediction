# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zone_list_window.ui'
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

class Ui_ZoneListWindow(object):
    def setupUi(self, ZoneListWindow):
        if not ZoneListWindow.objectName():
            ZoneListWindow.setObjectName(u"ZoneListWindow")
        ZoneListWindow.resize(900, 800)
        ZoneListWindow.setMinimumSize(QSize(900, 800))
        ZoneListWindow.setLayoutDirection(Qt.LeftToRight)
        ZoneListWindow.setStyleSheet(u"")
        self.grid_layout = QGridLayout(ZoneListWindow)
        self.grid_layout.setObjectName(u"grid_layout")
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setSpacing(15)
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.vertical_layout.setContentsMargins(50, 0, 50, 50)
        self.label_header = QLabel(ZoneListWindow)
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

        self.table_zones = QTableWidget(ZoneListWindow)
        if (self.table_zones.columnCount() < 2):
            self.table_zones.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_zones.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_zones.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.table_zones.rowCount() < 3):
            self.table_zones.setRowCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_zones.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_zones.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_zones.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_zones.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_zones.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_zones.setItem(1, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_zones.setItem(1, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_zones.setItem(2, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_zones.setItem(2, 1, __qtablewidgetitem10)
        self.table_zones.setObjectName(u"table_zones")
        self.table_zones.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_zones.sizePolicy().hasHeightForWidth())
        self.table_zones.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        self.table_zones.setFont(font1)
        self.table_zones.setAcceptDrops(False)
        self.table_zones.setLayoutDirection(Qt.RightToLeft)
        self.table_zones.setAutoFillBackground(False)
        self.table_zones.setStyleSheet(u"background-color: white;\n"
"color: dimgray;\n"
"\n"
"")
        self.table_zones.setFrameShape(QFrame.Box)
        self.table_zones.setFrameShadow(QFrame.Sunken)
        self.table_zones.setLineWidth(1)
        self.table_zones.setMidLineWidth(3)
        self.table_zones.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.table_zones.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_zones.setTabKeyNavigation(False)
        self.table_zones.setProperty("showDropIndicator", False)
        self.table_zones.setDragDropOverwriteMode(False)
        self.table_zones.setAlternatingRowColors(True)
        self.table_zones.setSelectionMode(QAbstractItemView.NoSelection)
        self.table_zones.setTextElideMode(Qt.ElideMiddle)
        self.table_zones.setShowGrid(True)
        self.table_zones.setGridStyle(Qt.SolidLine)
        self.table_zones.setSortingEnabled(False)
        self.table_zones.setWordWrap(True)
        self.table_zones.setCornerButtonEnabled(True)
        self.table_zones.setRowCount(3)
        self.table_zones.horizontalHeader().setVisible(True)
        self.table_zones.horizontalHeader().setCascadingSectionResizes(False)
        self.table_zones.horizontalHeader().setMinimumSectionSize(200)
        self.table_zones.horizontalHeader().setDefaultSectionSize(200)
        self.table_zones.horizontalHeader().setHighlightSections(True)
        self.table_zones.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_zones.horizontalHeader().setStretchLastSection(True)
        self.table_zones.verticalHeader().setVisible(False)
        self.table_zones.verticalHeader().setCascadingSectionResizes(False)
        self.table_zones.verticalHeader().setMinimumSectionSize(70)
        self.table_zones.verticalHeader().setDefaultSectionSize(70)
        self.table_zones.verticalHeader().setHighlightSections(True)
        self.table_zones.verticalHeader().setProperty("showSortIndicator", False)
        self.table_zones.verticalHeader().setStretchLastSection(True)

        self.vertical_layout.addWidget(self.table_zones)

        self.horizontal_layout_buttons = QHBoxLayout()
        self.horizontal_layout_buttons.setSpacing(30)
        self.horizontal_layout_buttons.setObjectName(u"horizontal_layout_buttons")
        self.button_search_house = QPushButton(ZoneListWindow)
        self.button_search_house.setObjectName(u"button_search_house")
        font2 = QFont()
        font2.setPointSize(14)
        self.button_search_house.setFont(font2)
        self.button_search_house.setStyleSheet(u"background-color: lightgray;\n"
"color: teal;")

        self.horizontal_layout_buttons.addWidget(self.button_search_house)

        self.button_predict_price = QPushButton(ZoneListWindow)
        self.button_predict_price.setObjectName(u"button_predict_price")
        self.button_predict_price.setFont(font2)
        self.button_predict_price.setStyleSheet(u"background-color: lightgray;\n"
"color: teal;")

        self.horizontal_layout_buttons.addWidget(self.button_predict_price)


        self.vertical_layout.addLayout(self.horizontal_layout_buttons)


        self.grid_layout.addLayout(self.vertical_layout, 0, 0, 1, 1)


        self.retranslateUi(ZoneListWindow)

        QMetaObject.connectSlotsByName(ZoneListWindow)
    # setupUi

    def retranslateUi(self, ZoneListWindow):
        ZoneListWindow.setWindowTitle(QCoreApplication.translate("ZoneListWindow", u"\u067e\u06cc\u0634\u0628\u06cc\u0646\u06cc \u0642\u06cc\u0645\u062a \u062e\u0627\u0646\u0647", None))
        self.label_header.setText(QCoreApplication.translate("ZoneListWindow", u"\u0645\u0646\u0627\u0637\u0642 \u0634\u0647\u0631 \u062a\u0647\u0631\u0627\u0646", None))
        ___qtablewidgetitem = self.table_zones.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ZoneListWindow", u"\u06a9\u062f \u0645\u0646\u0637\u0642\u0647", None));
        ___qtablewidgetitem1 = self.table_zones.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ZoneListWindow", u"\u0646\u0627\u0645 \u0645\u0646\u0637\u0642\u0647", None));
        ___qtablewidgetitem2 = self.table_zones.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ZoneListWindow", u"New Row", None));
        ___qtablewidgetitem3 = self.table_zones.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ZoneListWindow", u"New Row", None));
        ___qtablewidgetitem4 = self.table_zones.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ZoneListWindow", u"New Row", None));

        __sortingEnabled = self.table_zones.isSortingEnabled()
        self.table_zones.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.table_zones.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ZoneListWindow", u"dadsda", None));
        ___qtablewidgetitem6 = self.table_zones.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ZoneListWindow", u"adadadadad", None));
        ___qtablewidgetitem7 = self.table_zones.item(1, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ZoneListWindow", u"ffffffffffa", None));
        ___qtablewidgetitem8 = self.table_zones.item(1, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ZoneListWindow", u"wadadsfsef", None));
        ___qtablewidgetitem9 = self.table_zones.item(2, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ZoneListWindow", u"addwafggr", None));
        ___qtablewidgetitem10 = self.table_zones.item(2, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("ZoneListWindow", u"gdgdgtdgdg", None));
        self.table_zones.setSortingEnabled(__sortingEnabled)

        self.button_search_house.setText(QCoreApplication.translate("ZoneListWindow", u" \u062c\u0633\u062a \u0648 \u062c\u0648\u06cc \u062e\u0627\u0646\u0647", None))
        self.button_predict_price.setText(QCoreApplication.translate("ZoneListWindow", u"\u067e\u06cc\u0634\u0628\u06cc\u0646\u06cc \u0642\u06cc\u0645\u062a", None))
    # retranslateUi

