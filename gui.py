import sys
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from shabesh_website_information import ShabeshWebsiteInformation
from ui_zone_list_window import Ui_ZoneListWindow
from ui_form_predict_window import Ui_FormPredictWindow
from ui_form_search_window import Ui_FormSearchWindow
from ui_predict_window import Ui_PredictWindow
from ui_house_list_window import Ui_HouseListWindow
import resources


class ZoneListWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # setup ui
        self.ui = Ui_ZoneListWindow()
        self.ui.setupUi(self)

        # define custom font
        bnazanin_file = qtg.QFontDatabase.addApplicationFont(":/fonts/BNazanin.ttf")
        bnazanin_font = qtg.QFontDatabase.applicationFontFamilies(bnazanin_file)

        # insert items into table
        self.shabesh_info = ShabeshWebsiteInformation()
        self.ui.table_zones.setRowCount(len(self.shabesh_info.zone_list))
        for zone in self.shabesh_info.zone_list:
            self.ui.table_zones.setItem(zone[0], 0, qtw.QTableWidgetItem(str(zone[0])))
            self.ui.table_zones.item(zone[0], 0).setTextAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
            self.ui.table_zones.setItem(zone[0], 1, qtw.QTableWidgetItem(zone[1]))
            self.ui.table_zones.item(zone[0], 1).setTextAlignment(qtc.Qt.AlignmentFlag.AlignCenter)

        # set font on elements
        for c in self.children():
            if type(c) == qtw.QPushButton:
                c.setFont(qtg.QFont(bnazanin_font, 20))
            if type(c) == qtw.QLabel:
                c.setFont(qtg.QFont(bnazanin_font, 30))
            if type(c) == qtw.QTableWidget:
                c.setFont(qtg.QFont(bnazanin_font, 18))


class FormPredictWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # setup ui
        self.ui = Ui_FormPredictWindow()
        self.ui.setupUi(self)

        # define custom font
        bnazanin_file = qtg.QFontDatabase.addApplicationFont(":/fonts/BNazanin.ttf")
        bnazanin_font = qtg.QFontDatabase.applicationFontFamilies(bnazanin_file)

        # set font on elements and set validator for QLineEdits
        for c in self.children():
            if type(c) == qtw.QPushButton:
                c.setFont(qtg.QFont(bnazanin_font, 20))
            if type(c) == qtw.QLabel:
                c.setFont(qtg.QFont(bnazanin_font, 18))
            if c.objectName() == 'label_header':
                c.setFont(qtg.QFont(bnazanin_font, 30))
            if type(c) == qtw.QLineEdit:
                c.setValidator(qtg.QIntValidator(0, 10000))


class FormSearchWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # setup ui
        self.ui = Ui_FormSearchWindow()
        self.ui.setupUi(self)

        # define custom font
        bnazanin_file = qtg.QFontDatabase.addApplicationFont(":/fonts/BNazanin.ttf")
        bnazanin_font = qtg.QFontDatabase.applicationFontFamilies(bnazanin_file)

        # set font on elements and set validator for QLineEdits
        for c in self.children():
            if type(c) == qtw.QPushButton:
                c.setFont(qtg.QFont(bnazanin_font, 20))
            if type(c) == qtw.QLabel:
                c.setFont(qtg.QFont(bnazanin_font, 18))
            if c.objectName() == 'label_header':
                c.setFont(qtg.QFont(bnazanin_font, 30))
            if type(c) == qtw.QLineEdit:
                c.setValidator(qtg.QIntValidator(0, 10000))

        # set validator for input zone code
        self.ui.input_zone_code.setValidator(qtg.QIntValidator(0, 39))

        
class PredictWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # setup ui
        self.ui = Ui_PredictWindow()
        self.ui.setupUi(self)

        # define custom font
        bnazanin_file = qtg.QFontDatabase.addApplicationFont(":/fonts/BNazanin.ttf")
        bnazanin_font = qtg.QFontDatabase.applicationFontFamilies(bnazanin_file)

        # set font on elements
        for c in self.children():
            if type(c) == qtw.QPushButton:
                c.setFont(qtg.QFont(bnazanin_font, 20))
            if c.objectName() in ('label_header', 'label_network_information'):
                c.setFont(qtg.QFont(bnazanin_font, 26))

        def frame_set_font(frame, font, font_size):
            for child in frame:
                if type(child) == qtw.QLabel:
                    child.setFont(qtg.QFont(font, font_size))
                if child.children():
                    frame_set_font(child.children(), font, font_size)

        frame_set_font(self.ui.frame_predict_price.children(), bnazanin_font, 17)
        frame_set_font(self.ui.frame_network_information.children(), "Times New Roman", 14)


class HouseListWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # setup ui
        self.ui = Ui_HouseListWindow()
        self.ui.setupUi(self)

        # define custom font
        bnazanin_file = qtg.QFontDatabase.addApplicationFont(":/fonts/BNazanin.ttf")
        bnazanin_font = qtg.QFontDatabase.applicationFontFamilies(bnazanin_file)
        
        # set font on elements
        for c in self.children():
            if type(c) == qtw.QPushButton:
                c.setFont(qtg.QFont(bnazanin_font, 20))
            if type(c) == qtw.QLabel:
                c.setFont(qtg.QFont(bnazanin_font, 30))
            if type(c) == qtw.QTableWidget:
                c.setFont(qtg.QFont(bnazanin_font, 18))
        
        # move table items center
        self.table_items_alignment()
    
    def table_items_alignment(self):
        for column in range(self.ui.table_houses.columnCount()):
            self.ui.table_houses.horizontalHeader().setSectionResizeMode(column, qtw.QHeaderView.ResizeMode.Stretch)
            for row in range(self.ui.table_houses.rowCount()):
                self.ui.table_houses.item(row, column).setTextAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
                self.ui.table_houses.verticalHeader().setSectionResizeMode(row, qtw.QHeaderView.ResizeMode.Stretch)

    def remove_table_rows(self):
        for i in range(self.ui.table_houses.rowCount()):
            self.ui.table_houses.removeRow(0)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    zone_list_window = ZoneListWindow()
    form_predict_window = FormPredictWindow()
    form_search_window = FormSearchWindow()
    predict_window = PredictWindow()
    house_list_window = HouseListWindow()

    # zone_list_window.show()
    # form_predict_window.show()
    # form_search_window.show()
    # predict_window.show()
    house_list_window.show()

    sys.exit(app.exec())
