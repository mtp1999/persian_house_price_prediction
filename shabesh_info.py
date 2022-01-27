import re

main_url = 'https://shabesh.com/search/خرید-فروش/آپارتمان/{}-تهران?page={}'

zone = ['سعادت آباد', 'زعفرانیه', 'ولنجک', 'بلوار فردوس', 'پاسداران',
        'شهرک غرب', 'نیاوران', 'پونک', 'فرمانیه', 'دروس', 'جنت آباد جنوبی',
        'سازمان برنامه', 'الهیه', 'صادقیه', 'فرشته', 'هروی',
        'جردن', 'ستارخان', 'جنت آباد مرکزی', 'قیطریه', 'محمودیه', 'شهران', 'جیحون',
        'اختیاریه', 'ازگل', 'چیتگر', 'شهر زیبا', 'استاد معین', 'مرزداران', 'میرداماد',
        'آیت الله کاشانی', 'پیروزی', 'جنت آباد شمالی', 'باغ فیض', 'دولت', 'ظفر',
        'سهروردی شمالی', 'اقدسیه', 'امیرآباد', 'کامرانیه']

for z in range(len(zone)):
    zone[z] = re.sub(r' ', '-', zone[z])


# assign code to zones
def zone_codes():
    zone_list = list()
    for i in range(len(zone)):
        zone_list.append([i, zone[i]])
    return zone_list


def input_zone():
    iz = int(input('please type zone number:'))
    return iz
