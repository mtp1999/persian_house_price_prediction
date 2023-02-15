import re


class ShabeshWebsiteInformation:
    
    # use this url for web scraping
    # place zone name in the main_url using zone_list, before send it to the server 
    main_url = 'https://shabesh.com/search/خرید-فروش/آپارتمان/{}-تهران?page={}'

    # a list of 40 zones supports in shabesh website 
    __zone_list = ['سعادت آباد', 'زعفرانیه', 'ولنجک', 'بلوار فردوس', 'پاسداران',
                   'شهرک غرب', 'نیاوران', 'پونک', 'فرمانیه', 'دروس', 'جنت آباد جنوبی',
                   'سازمان برنامه', 'الهیه', 'صادقیه', 'فرشته', 'هروی',
                   'جردن', 'ستارخان', 'جنت آباد مرکزی', 'قیطریه', 'محمودیه', 'شهران', 'جیحون',
                   'اختیاریه', 'ازگل', 'چیتگر', 'شهر زیبا', 'استاد معین', 'مرزداران', 'میرداماد',
                   'آیت الله کاشانی', 'پیروزی', 'جنت آباد شمالی', 'باغ فیض', 'دولت', 'ظفر',
                   'سهروردی شمالی', 'اقدسیه', 'امیرآباد', 'کامرانیه']

    # replace space with dash in zone list (because of using them in the main_url)
    for z in range(len(__zone_list)):
        __zone_list[z] = re.sub(r' ', '-', __zone_list[z])

    @property
    def zone_list(self):
        # output ==> [[index, zone_name], [index, zone_name], [index, zone_name], ...]
        zone_list = list()
        for i in range(len(self.__zone_list)):
            zone_list.append([i, self.__zone_list[i]])
        return zone_list


if __name__ == '__main__':
    shabesh = ShabeshWebsiteInformation()
    print(shabesh.zone_list)