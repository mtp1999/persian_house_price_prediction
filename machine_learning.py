from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_poisson_deviance

# import from developer project files
from web_scraping import ShabeshWebsiteWebScraping


# class MachineLearning:
#
#     web_scraping = ShabeshWebsiteWebScraping()
#
#     def data_split(self, zone_code):
#         data = self.web_scraping.get_data_from_website(zone_code)
#         if data is False:
#             return False
#         else:
#             price, price_per_meter, area, bedroom, year = data
#             area_bedroom_year = list()
#             for i in range(len(area)):
#                 area_bedroom_year.append([area[i], bedroom[i], year[i]])
#             x_train, x_test, y_train, y_test = train_test_split(area_bedroom_year, price, test_size=0.33, random_state=42)
#             return [x_train, x_test, y_train, y_test]
#
#     def training_and_testing(self, zone_code):
#         data = self.data_split(zone_code)
#         if data is False:
#             return False
#         else:
#             x_train, x_test, y_train, y_test = data
#             clf = self.decision_tree(x_train, y_train)
#             y_predict = clf.predict(x_test)
#             mae = mean_absolute_error(y_test, y_predict)
#             mse = mean_squared_error(y_test, y_predict)
#             rmse = mse ** 0.5
#             mpd = mean_poisson_deviance(y_test, y_predict)
#             return [clf, mae, mse, rmse, mpd, len(x_train), len(x_test)]
#
#     @staticmethod
#     def decision_tree(features, target):
#         clf = DecisionTreeRegressor()
#         clf = clf.fit(features, target)
#         return clf
#
#     @staticmethod
#     def prediction(clf, input_area, input_bedroom, input_year):
#         predict = int(clf.predict([[input_area, input_bedroom, input_year]]))
#         return predict


class MachineLearning:

    web_scraping = ShabeshWebsiteWebScraping()

    def get_data_from_website(self, zone_code):
        data_list = self.web_scraping.get_data_from_website(zone_code)
        if data_list is False:
            return False
        else:
            return data_list

    @staticmethod
    def data_split(data_list):
        price_list, price_per_meter_list, area_list, bedroom_list, year_list = data_list
        area_bedroom_year_list = list()
        for i in range(len(area_list)):
            area_bedroom_year_list.append([area_list[i], bedroom_list[i], year_list[i]])
        x_train, x_test, y_train, y_test = train_test_split(area_bedroom_year_list, price_list, test_size=0.33,
                                                            random_state=42)
        return x_train, x_test, y_train, y_test

    def training_and_testing(self, x_train, x_test, y_train, y_test):
        clf = self.decision_tree(x_train, y_train)
        y_predict = clf.predict(x_test)
        mae = mean_absolute_error(y_test, y_predict)
        mse = mean_squared_error(y_test, y_predict)
        rmse = mse ** 0.5
        mpd = mean_poisson_deviance(y_test, y_predict)
        return clf, mae, mse, rmse, mpd, len(x_train), len(x_test)

    @staticmethod
    def decision_tree(features, target):
        clf = DecisionTreeRegressor()
        clf = clf.fit(features, target)
        return clf

    @staticmethod
    def prediction(clf, input_area, input_bedroom, input_year):
        predict = int(clf.predict([[input_area, input_bedroom, input_year]]))
        return predict


if __name__ == '__main__':
    ml = MachineLearning()
    data_list = ml.get_data_from_website(10)
    x_train, x_test, y_train, y_test = ml.data_split(data_list)
    clf, mae, mse, rmse, mpd, len_x_train, len_x_test = ml.training_and_testing(x_train, x_test, y_train, y_test)
    predict = ml.prediction(clf, 120, 3, 1390)
    print(predict)
