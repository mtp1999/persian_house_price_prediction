import sys
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
import gui
from shabesh_website_information import ShabeshWebsiteInformation
from web_scraping import ShabeshWebsiteWebScraping
from machine_learning import MachineLearning
import resources


class ZoneListWindow(gui.ZoneListWindow):
    def __init__(self):
        super().__init__()

        # set title
        stacked_widget.setWindowTitle('شابش(مناطق تهران)')

        # connect buttons
        self.ui.button_predict_price.clicked.connect(self.button_predict_price_clicked)
        self.ui.button_search_house.clicked.connect(self.button_search_house_clicked)

        self.show()

    @staticmethod
    def button_predict_price_clicked():
        stacked_widget.setWindowTitle('شابش(فرم اطلاعات)')
        stacked_widget.setCurrentIndex(1)

    @staticmethod
    def button_search_house_clicked():
        stacked_widget.setWindowTitle('شابش(فرم اطلاعات)')
        stacked_widget.setCurrentIndex(2)


class FormPredictWindow(gui.FormPredictWindow):

    signal = qtc.Signal(dict)

    def __init__(self):
        super().__init__()

        # connect buttons
        self.ui.button_zone_list.clicked.connect(self.button_zone_list_clicked)
        self.ui.button_search_house.clicked.connect(self.button_search_house_clicked)
        self.ui.button_submit.clicked.connect(self.button_submit_clicked)

    @staticmethod
    def button_zone_list_clicked():
        stacked_widget.setWindowTitle('شابش(مناطق تهران)')
        stacked_widget.setCurrentIndex(0)

    @staticmethod
    def button_search_house_clicked():
        stacked_widget.setWindowTitle('شابش(فرم اطلاعات)')
        stacked_widget.setCurrentIndex(2)

    def button_submit_clicked(self):
        house_information = {}
        for c in self.children():
            if type(c) == qtw.QLineEdit:
                if c.text() != '':
                    if c.objectName() == 'input_zone_code':
                        house_information['zone'] = int(c.text())
                    if c.objectName() == 'input_meter':
                        house_information['meter'] = int(c.text())
                    if c.objectName() == 'input_year':
                        house_information['year'] = int(c.text())
                    if c.objectName() == 'input_bedroom':
                        house_information['bedroom'] = int(c.text())
                else:
                    return
        stacked_widget.setCurrentIndex(3)
        stacked_widget.currentWidget().get_house_information(house_information)


class MachineLearningThread(qtc.QThread):
    zone_code = None
    done = qtc.Signal(tuple)

    def run(self):
        data_list = MachineLearning().get_data_from_website(self.zone_code)
        x_train, x_test, y_train, y_test = MachineLearning().data_split(data_list)
        learning_information = MachineLearning().training_and_testing(x_train, x_test, y_train, y_test)
        self.done.emit(learning_information)

    def get_zone_code(self, zone_code):
        self.zone_code = zone_code


class PredictWindow(gui.PredictWindow):
    def __init__(self):
        super().__init__()

        # house information dictionary(information given by user)
        self.house_information = None

        # define a thread to train the learning network
        self.thread = None

        # default values used for labels
        self.default_value_en = 'processing'
        self.default_value_fa = 'در حال پردازش'

        # connect buttons
        self.ui.button_back.clicked.connect(self.button_back_clicked)
        self.ui.button_search_house.clicked.connect(self.button_search_house_clicked)

    @staticmethod
    def button_back_clicked():
        stacked_widget.setWindowTitle('شابش(فرم اطلاعات)')
        stacked_widget.setCurrentIndex(1)

    @staticmethod
    def button_search_house_clicked():
        stacked_widget.setWindowTitle('شابش(فرم اطلاعات)')
        stacked_widget.setCurrentIndex(2)

    def get_house_information(self, house_information):
        self.house_information = house_information
        self.set_label_default_values()
        self.thread = MachineLearningThread()
        self.thread.get_zone_code(self.house_information['zone'])
        self.thread.start()
        self.thread.done.connect(self.get_learning_information)

    def get_learning_information(self, learning_information):
        self.thread.finished.connect(self.thread.deleteLater)
        self.clf, self.mae, self.mse, self.rmse, self.mpd, self.len_x_train, self.len_x_test = learning_information
        self.predict_price()
        self.set_label_values()

    def predict_price(self):
        self.predicted_price = MachineLearning().prediction(self.clf, self.house_information['meter'], self.house_information['bedroom'], self.house_information['year'])
        self.predicted_price = str(self.predicted_price / 1000000000) + 'میلیارد تومان'

    def set_label_default_values(self):
        # frame1
        self.ui.label_zone_value.setText(self.default_value_fa)
        self.ui.label_meter_value.setText(self.default_value_fa)
        self.ui.label_year_value.setText(self.default_value_fa)
        self.ui.label_bedroom_value.setText(self.default_value_fa)
        self.ui.label_predict_price_value.setText(self.default_value_fa)
        # frame2
        self.ui.label_mae_value.setText(self.default_value_en)
        self.ui.label_mse_value.setText(self.default_value_en)
        self.ui.label_rmse_value.setText(self.default_value_en)
        self.ui.label_mpd_value.setText(self.default_value_en)
        self.ui.label_train_data_number_value.setText(self.default_value_en)
        self.ui.label_test_data_number_value.setText(self.default_value_en)

    def set_label_values(self):
        # frame1
        self.ui.label_zone_value.setText(ShabeshWebsiteInformation().zone_list[self.house_information['zone']][1])
        self.ui.label_meter_value.setText(str(self.house_information['meter']))
        self.ui.label_year_value.setText(str(self.house_information['year']))
        self.ui.label_bedroom_value.setText(str(self.house_information['bedroom']))
        self.ui.label_predict_price_value.setText(str(self.predicted_price))
        # frame2
        self.ui.label_mae_value.setText(str(self.mae))
        self.ui.label_mse_value.setText(str(self.mse))
        self.ui.label_rmse_value.setText(str(self.rmse))
        self.ui.label_mpd_value.setText(str(self.mpd))
        self.ui.label_train_data_number_value.setText(str(self.len_x_train))
        self.ui.label_test_data_number_value.setText(str(self.len_x_test))


class FormSearchWindow(gui.FormSearchWindow):
    def __init__(self):
        super().__init__()

        # connect buttons
        self.ui.button_zone_list.clicked.connect(self.button_zone_list_clicked)
        self.ui.button_predict_price.clicked.connect(self.button_predict_price_clicked)
        self.ui.button_submit.clicked.connect(self.button_submit_clicked)

    @staticmethod
    def button_zone_list_clicked():
        stacked_widget.setWindowTitle('شابش(مناطق تهران)')
        stacked_widget.setCurrentIndex(0)

    @staticmethod
    def button_predict_price_clicked():
        stacked_widget.setWindowTitle('شابش(فرم اطلاعات)')
        stacked_widget.setCurrentIndex(1)

    def button_submit_clicked(self):
        house_information = {}
        for c in self.children():
            if type(c) == qtw.QLineEdit:
                if c.text() != '':
                    if c.objectName() == 'input_zone_code':
                        house_information['zone'] = int(c.text())
                    if c.objectName() == 'input_min_meter':
                        house_information['min_meter'] = int(c.text())
                    if c.objectName() == 'input_max_meter':
                        house_information['max_meter'] = int(c.text())
                    if c.objectName() == 'input_min_price':
                        house_information['min_price'] = int(c.text())
                    if c.objectName() == 'input_max_price':
                        house_information['max_price'] = int(c.text())
                else:
                    return
        stacked_widget.setCurrentIndex(4)
        stacked_widget.currentWidget().get_house_information(house_information)


class SearchThread(qtc.QThread):
    house_information = None
    done = qtc.Signal(list)

    def run(self):
        price_list, price_per_meter_list, area_list, bedroom_list, year_list = ShabeshWebsiteWebScraping().get_data_from_website(self.house_information['zone'])
        house_list = []
        for i in range(len(price_list)):
            if price_list[i] >= self.house_information['min_price'] * 1000000000:
                if price_list[i] <= self.house_information['max_price'] * 1000000000:
                    if area_list[i] >= self.house_information['min_meter']:
                        if area_list[i] <= self.house_information['max_meter']:
                            house_list.append([
                                price_list[i],
                                price_per_meter_list[i],
                                area_list[i],
                                bedroom_list[i],
                                year_list[i]
                            ])
        self.done.emit(house_list)

    def get_house_information(self, house_information):
        self.house_information = house_information


class HouseListWindow(gui.HouseListWindow):
    def __init__(self):
        super().__init__()

        # house information dictionary(information given by user)
        self.house_information = None

        # define a thread to search desired houses
        self.thread = None

        # connect buttons
        self.ui.button_back.clicked.connect(self.button_back_clicked)
        self.ui.button_predict_price.clicked.connect(self.button_predict_price_clicked)

    @staticmethod
    def button_back_clicked():
        stacked_widget.setWindowTitle('شابش(فرم اطلاعات)')
        stacked_widget.setCurrentIndex(2)

    @staticmethod
    def button_predict_price_clicked():
        stacked_widget.setWindowTitle('شابش(فرم اطلاعات)')
        stacked_widget.setCurrentIndex(1)

    def get_house_information(self, house_information):
        self.house_information = house_information
        self.remove_table_rows()
        self.ui.label_header.setText('خانه های یافت شده در منطقه {}'.format(ShabeshWebsiteInformation().zone_list[self.house_information['zone']][1]))
        self.thread = SearchThread()
        self.thread.get_house_information(house_information)
        self.thread.start()
        self.thread.done.connect(self.insert_house_list_into_table)

    def insert_house_list_into_table(self, house_list):
        self.thread.finished.connect(self.thread.deleteLater)
        if house_list:
            self.ui.table_houses.setRowCount(len(house_list))
            for i in range(len(house_list)):
                for j in range(0, 5):
                    self.ui.table_houses.setItem(i, j, qtw.QTableWidgetItem(str(house_list[i][j])))

            self.table_items_alignment()
        else:
            self.ui.label_header.setText('خانه ی مورد نظر در منطقه {} یافت نشد.'.format(ShabeshWebsiteInformation().zone_list[self.house_information['zone']][1]))


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    stacked_widget = qtw.QStackedWidget()
    stacked_widget.setWindowIcon(qtg.QIcon(':/icons/house.png'))

    # index 0
    stacked_widget.addWidget(ZoneListWindow())
    # index 1
    stacked_widget.addWidget(FormPredictWindow())
    # index 2
    stacked_widget.addWidget(FormSearchWindow())
    # index 3
    stacked_widget.addWidget(PredictWindow())
    # index 4
    stacked_widget.addWidget(HouseListWindow())

    stacked_widget.show()
    sys.exit(app.exec())
