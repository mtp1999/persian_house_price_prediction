from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_poisson_deviance

# import from developer project files
from web_scraping import get_data_from_web


def decision_tree(features, target):
    clf = tree.DecisionTreeRegressor()
    clf = clf.fit(features, target)
    return clf


def prediction(clf, input_area, input_bedroom, input_year):
    predict = int(clf.predict([[input_area, input_bedroom, input_year]]))
    return predict


def data_split(input_zone):
    data = get_data_from_web(input_zone)
    if data is False:
        return False
    else:
        price, price_per_meter, area, bedroom, year = data
        area_bedroom_year = list()
        for i in range(len(area)):
            area_bedroom_year.append([area[i], bedroom[i], year[i]])
        x_train, x_test, y_train, y_test = train_test_split(area_bedroom_year, price, test_size=0.33, random_state=42)
        return [x_train, x_test, y_train, y_test]


def training_and_testing(input_zone):
    data = data_split(input_zone)
    if data is False:
        return False
    else:
        x_train, x_test, y_train, y_test = data
        clf = decision_tree(x_train, y_train)
        y_predict = clf.predict(x_test)
        mae = mean_absolute_error(y_test, y_predict)
        mse = mean_squared_error(y_test, y_predict)
        rmse = mse ** 0.5
        mpd = mean_poisson_deviance(y_test, y_predict)
        return [clf, mae, mse, rmse, mpd, len(x_train), len(x_test)]








