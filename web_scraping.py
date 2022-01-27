from bs4 import BeautifulSoup
import requests
import re
import bs4

# import from developer project files
from shabesh_info import main_url, zone


def data_cleaner(*args):
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


def web_scraping_from_shabesh(s):
    houses = s.find_all('div',
                        attrs={'class': 'list_announceListContainer__MBWBR h-100 list_rent___v0E4 false'})
    for house in houses:
        AREA_BEDROOM = house.find_all('span', attrs={'class': 'd-inline-flex ps-2 align-items-center'})
        if len(AREA_BEDROOM) == 2:
            AREA, BEDROOM = AREA_BEDROOM[0], AREA_BEDROOM[1]
            PRICE = house.find('span', attrs={'class': 'list_infoItem__8EH57 list_infoPrice___aJXK d-block'})
            PRICE_PER_METER = house.find('span', attrs={
                'class': 'list_infoItem__8EH57 font-14 global_colorGray1__i1u0y d-block'
            })
            YEAR = house.find('span', attrs={'class': 'd-inline-flex align-items-center'})
            yield [PRICE, PRICE_PER_METER, AREA, BEDROOM, YEAR]


def get_data_from_web(ZONE_CODE):
    price, price_per_meter, area, bedroom, year = [], [], [], [], []
    for page_number in range(1, 10):
        r = requests.get(main_url.format(zone[ZONE_CODE], str(page_number)))
        if r.status_code == 200:
            s = BeautifulSoup(r.text, 'html.parser')
            for i in web_scraping_from_shabesh(s):
                PRICE, PRICE_PER_METER, AREA, BEDROOM, YEAR = i[0], i[1], i[2], i[3], i[4]
                clean_data = data_cleaner(PRICE, PRICE_PER_METER, AREA, BEDROOM, YEAR)
                if clean_data is not False:
                    PRICE, PRICE_PER_METER, AREA, BEDROOM, YEAR = clean_data
                    price.append(PRICE)
                    price_per_meter.append(PRICE_PER_METER)
                    area.append(AREA)
                    bedroom.append(BEDROOM)
                    year.append(YEAR)

    data_list = [price, price_per_meter, area, bedroom, year]
    for i in data_list:
        if len(i) == 0:
            return False
    return data_list


# this func is just used for test, not in project
def test_web_scraping(ZONE_CODE):
    price, price_per_meter, area, bedroom, year = get_data_from_web(ZONE_CODE)
    return [len(price), len(price_per_meter), len(area), len(bedroom), len(year)]
