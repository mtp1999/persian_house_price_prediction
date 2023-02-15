from bs4 import BeautifulSoup
import requests
import re
import bs4

# import from developer project files
from shabesh_website_information import ShabeshWebsiteInformation


class ShabeshWebsiteWebScraping:

    @staticmethod
    def __data_cleaner(*args):
        """search if there is any digits in the
        strings, taken by web scraping.
        if not, return false.
        """
        l = []
        for arg in args:
            if type(arg) == bs4.element.Tag:
                if not re.search(r'\d', arg.get_text()):
                    return False
            else:
                return False
            arg = int(re.sub(r'\D', '', arg.get_text()))
            l.append(arg)
        if len(l) != len(args):
            return False
        else:
            return l

    @staticmethod
    def __web_scraping(s):
        """get specific html elements using web scraping.
        elements are related to price, price_per_meter, area, bedroom, year.
        s : soup using BeautifulSoup   
        """
        houses = s.find_all('div',
                            attrs={'class': 'list_announceListContainer__MBWBR h-100 list_rent___v0E4 false'})
        for house in houses:
            area_bedroom = house.find_all('span', attrs={'class': 'd-inline-flex ps-2 align-items-center'})
            if len(area_bedroom) == 2:
                area, bedroom = area_bedroom[0], area_bedroom[1]
                price = house.find('span', attrs={'class': 'list_infoItem__8EH57 list_infoPrice___aJXK d-block'})
                price_per_meter = house.find('span', attrs={
                    'class': 'list_infoItem__8EH57 font-14 global_colorGray1__i1u0y d-block'
                })
                year = house.find('span', attrs={'class': 'd-inline-flex align-items-center'})
                yield [price, price_per_meter, area, bedroom, year]

    def get_data_from_website(self, zone_index):
        """send request using main_url and get house data using web scraping.
        in the end returns data_list that is defined below.
        """
        price_list, price_per_meter_list, area_list, bedroom_list, year_list = [], [], [], [], []
        shabesh = ShabeshWebsiteInformation()
        for page_number in range(1, 10):
            r = requests.get(shabesh.main_url.format(shabesh.zone_list[zone_index][1], str(page_number)))
            if r.status_code == 200:
                s = BeautifulSoup(r.text, 'html.parser')
                for i in self.__web_scraping(s):
                    price, price_per_meter, area, bedroom, year = i[0], i[1], i[2], i[3], i[4]
                    clean_data = self.__data_cleaner(price, price_per_meter, area, bedroom, year)
                    if clean_data is not False:
                        price, price_per_meter, area, bedroom, year = clean_data
                        price_list.append(price)
                        price_per_meter_list.append(price_per_meter)
                        area_list.append(area)
                        bedroom_list.append(bedroom)
                        year_list.append(year)

        data_list = [price_list, price_per_meter_list, area_list, bedroom_list, year_list]
        for i in data_list:
            if len(i) == 0:
                return False
        return data_list


if __name__ == "__main__":
    obj = ShabeshWebsiteWebScraping()
    # price, price_per_meter, area, bedroom, year = obj.get_data_from_website(12)
    # print(len(price), len(price_per_meter), len(area), len(bedroom), len(year))
    # print(price[0], price_per_meter[0], area[0], bedroom[0], year[0])
