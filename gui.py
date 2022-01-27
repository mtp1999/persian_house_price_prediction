from tkinter import *

# import from developer project files
from shabesh_info import zone_codes, zone, main_url
from machine_learning import training_and_testing, prediction
from web_scraping import get_data_from_web

window = Tk()

window.title("اپلیکیشن شابش")
window.geometry("800x500")
window.resizable(width=False, height=False)
window.config(bg="#B3A9C4")
for w in window.winfo_children():
    w.config(bg="#B3A9C4")


def base_widgets():
    for w in window.winfo_children():
        if type(w) is Frame:
            for f in w.winfo_children():
                f.grid_forget()
                f.pack_forget()
        w.grid_forget()
        w.pack_forget()
    # base widgets
    for w in window.winfo_children():
        if type(w) is Button:
            w.config(bg="#8E001C", fg="white", bd=10, activebackground="#F08080")
        if type(w) is Label:
            w.config(bg="#B3A9C4", fg="black")
        if type(w) is Frame:
            for i in w.winfo_children():
                if type(i) is Button:
                    i.config(bg="#8E001C", fg="white", bd=10, activebackground="#F08080")
                if type(i) is Label:
                    i.config(bg="#B3A9C4", fg="black")
            w.config(bg="#B3A9C4")


def main_window():
    base_widgets()
    label_main.pack(fill=BOTH)
    button_price_predict.pack(side=RIGHT, padx=40)
    button_show_houses.pack(side=RIGHT, padx=40)
    button_show_zones.pack(side=RIGHT, padx=40)


def show_zones_window():
    base_widgets()
    zones = zone_codes()
    label0 = Label(window, height="0", width="40", bg="#B3A9C4")
    label1 = Label(window, height="0", width="40", bg="#B3A9C4")
    label2 = Label(window, height="0", width="40", bg="#B3A9C4")
    label0.grid(row=0, column=0)
    label1.grid(row=0, column=1)
    label2.grid(row=0, column=2)
    for i in range(len(zones)):
        txt = "{} : {}".format(zones[i][0], zones[i][1])
        zone_label = Label(window, text=txt, font=("B Titr", 10), fg="black", bg="#B3A9C4")
        if i <= 13:
            zone_label.grid(row=i, column=2)
        elif 14 <= i <= 26:
            zone_label.grid(row=i - 14, column=1)
        else:
            zone_label.grid(row=i - 27, column=0)
    button_return_to_main.grid(row=i-24, column=0)


def get_input_data(func):
    if func == show_houses_window:
        input_zone = intvar_zone.get()
        input_min_area = intvar_min_area.get()
        input_max_area = intvar_max_area.get()
        input_min_price = intvar_min_price.get()
        input_max_price = intvar_max_price.get()
        return [input_zone, input_min_area, input_max_area, input_min_price, input_max_price]
    elif func == show_predict_window:
        input_zone = intvar_zone.get()
        input_area = intvar_area.get()
        input_bedroom = intvar_bedroom.get()
        input_year = intvar_year.get()
        return [input_zone, input_area, input_bedroom, input_year]


def show_houses_window():
    input_zone, input_min_area, input_max_area, input_min_price, input_max_price = get_input_data(show_houses_window)
    data = get_data_from_web(input_zone)
    if data is False:
        base_widgets()
        Label(window, text=".متاسفانه برنامه با مشکل مواجه شد", font=("B Titr", 15), bg="#B3A9C4",
              fg="black").pack(pady=10, fill=BOTH)
        Label(window, text=".ممکن است برنامه به بروز رسانی نیاز داشته باشد", font=("B Titr", 15), bg="#B3A9C4",
              fg="black").pack(pady=10, fill=BOTH)
        button_return_to_input_search.pack(pady=150)
    else:
        price, price_per_meter, area, bedroom, year = data
        output_list = []
        for i in range(len(price)):
            if input_min_price <= price[i] <= input_max_price:
                if input_min_area <= area[i] <= input_max_area:
                    output_list.append([price[i], price_per_meter[i], area[i], bedroom[i], year[i]])
        base_widgets()
        if len(output_list) > 0:
            scrollbar.pack(side=RIGHT, fill=BOTH)
            list_box.delete(0, END)
            list_box.pack(expand=True, fill=BOTH)
            list_box.insert(END, "")
            list_box.insert(END, ".قیمت ها بر حسب تومان میباشد")
            for i in output_list:
                list_box.insert(END, "")
                list_box.insert(END, "قیمت : {} ___ قیمت هر متر : {} ___ متراژ : {} ___ تعداد اتاق : {} ___ سال ساخت : {}".format(i[0], i[1], i[2], i[3], i[4]))
            list_box.insert(END, "")
            list_box.insert(END, "تعداد آگهی یافت شده : {}".format(len(output_list)))
            list_box.insert(END, "")
            list_box.insert(END, ": جهت کسب اطلاعات بیشتر یا اقدام به خرید خانه، به آدرس اینترنتی زیر مراجه فرمایید")
            list_box.insert(END, main_url.format(zone[input_zone], "1"))
            scrollbar.config(command=list_box.yview)
            button_return_to_input_search.pack(pady=20)
        else:
            Label(window, text=".متاسفانه خانه ای با مشخصات وارد شده یافت نشد", font=("B Titr", 15), bg="#B3A9C4", fg="black").pack(pady=10, fill=BOTH)
            button_return_to_input_search.pack(pady=200)


def input_search_window():
    base_widgets()
    label_input.pack(side=TOP)
    frame1.pack(side=TOP, fill=BOTH)
    frame2.pack(side=TOP, fill=BOTH)
    frame3.pack(side=TOP, fill=BOTH)
    frame4.pack(side=TOP, fill=BOTH)
    frame5.pack(side=TOP, fill=BOTH)
    frame6.pack(side=TOP, fill=BOTH)
    # inputs
    label_input_zone.pack(side=RIGHT, pady=10, padx=100)
    entry_zone.pack(side=LEFT, pady=10, padx=100)
    label_input_min_area.pack(side=RIGHT, pady=10, padx=100)
    entry_min_area.pack(side=LEFT, pady=10, padx=100)
    label_input_max_area.pack(side=RIGHT, pady=10, padx=100)
    entry_max_area.pack(side=LEFT, pady=10, padx=100)
    label_input_min_price.pack(side=RIGHT, pady=10, padx=100)
    entry_min_price.pack(side=LEFT, pady=10, padx=100)
    label_input_max_price.pack(side=RIGHT, pady=10, padx=100)
    entry_max_price.pack(side=LEFT, pady=10, padx=100)
    button_submit.config(command=show_houses_window)
    button_submit.pack(side=LEFT, pady=10, padx=100)
    button_return_to_main.pack()


def input_predict_window():
    base_widgets()
    label_input.pack(side=TOP)
    frame1.pack(side=TOP, fill=BOTH)
    frame2.pack(side=TOP, fill=BOTH)
    frame3.pack(side=TOP, fill=BOTH)
    frame4.pack(side=TOP, fill=BOTH)
    frame6.pack(side=TOP, fill=BOTH)
    # inputs
    label_input_zone.pack(side=RIGHT, pady=10, padx=100)
    entry_zone.pack(side=LEFT, pady=10, padx=100)
    label_input_area.pack(side=RIGHT, pady=10, padx=100)
    entry_area.pack(side=LEFT, pady=10, padx=100)
    label_input_bedroom.pack(side=RIGHT, pady=10, padx=100)
    entry_bedroom.pack(side=LEFT, pady=10, padx=100)
    label_input_year.pack(side=RIGHT, pady=10, padx=100)
    entry_year.pack(side=LEFT, pady=10, padx=100)
    button_submit.config(command=show_predict_window)
    button_submit.pack(side=LEFT, pady=10, padx=100)
    button_return_to_main.pack()


last_zone, last_clf, last_mae, last_mse, last_rmse, last_mpd = None, None, None, None, None, None
last_train_data, last_test_data = None, None


def show_predict_window():
    base_widgets()
    input_zone, input_area, input_bedroom, input_year = get_input_data(show_predict_window)
    global last_zone, last_clf, last_mae, last_mse, last_rmse, last_mpd, last_train_data, last_test_data
    if input_zone != last_zone:
        data = training_and_testing(input_zone)
        if data is False:
            base_widgets()
            Label(window, text=".متاسفانه برنامه با مشکل مواجه شد", font=("B Titr", 15), bg="#B3A9C4",
                  fg="black").pack(pady=10, fill=BOTH)
            Label(window, text=".ممکن است برنامه به بروز رسانی نیاز داشته باشد", font=("B Titr", 15), bg="#B3A9C4",
                  fg="black").pack(pady=10, fill=BOTH)
            button_return_to_input_predict.pack(pady=150)
        else:
            clf, mae, mse, rmse, mpd, train_data, test_data = data
            last_zone, last_clf, last_mae, last_mse, last_rmse, last_mpd = input_zone, clf, mae, mse, rmse, mpd
            last_train_data, last_test_data = train_data, test_data
            resault = prediction(clf, input_area, input_bedroom, input_year)
    else:
        resault = prediction(last_clf, input_area, input_bedroom, input_year)
        mae, mse, rmse, mpd = last_mae, last_mse, last_rmse, last_mpd
        train_data, test_data = last_train_data, last_test_data
    resault = resault/1000000000
    str0 = "منطقه : {} ___ متراژ : {} ___ تعداد اتاق : {} ___ سال ساخت : {}"
    str0 = str0.format(zone[input_zone], input_area, input_bedroom, input_year)
    str1 = "قیمت پیشبینی شده خانه مورد نظر : {} میلیارد تومان".format(resault)
    main_str = str0 + "\n" + str1
    str_train_data = "number of train data : " + str(train_data)
    str_test_data = "number of test data : " + str(test_data)
    str_mae = "mean absolute error : " + str(mae)
    str_mse = "mean squared error : " + str(mse)
    str_rmse = "root mean squared error : " + str(rmse)
    str_mpd = "mean poisson deviance : " + str(mpd)
    Label(window, font=("B Titr", 18), text=main_str, bg="#B3A9C4", fg="black", height="3").pack(fill=BOTH, expand=True)
    Label(window, font=("verdana", 13), text=str_train_data, bg="#B3A9C4", fg="black", height="1").pack(fill=BOTH, expand=True)
    Label(window, font=("verdana", 13), text=str_test_data, bg="#B3A9C4", fg="black", height="1").pack(fill=BOTH, expand=True)
    Label(window, font=("verdana", 13), text=str_mse, bg="#B3A9C4", fg="black", height="1").pack(fill=BOTH, expand=True)
    Label(window, font=("verdana", 13), text=str_rmse, bg="#B3A9C4", fg="black", height="1").pack(fill=BOTH, expand=True)
    Label(window, font=("verdana", 13), text=str_mae, bg="#B3A9C4", fg="black", height="1").pack(fill=BOTH, expand=True)
    Label(window, font=("verdana", 13), text=str_mpd, bg="#B3A9C4", fg="black", height="1").pack(fill=BOTH, expand=True)
    button_return_to_input_predict.pack(pady=60)


# main window widgets
label_main = Label(window, text="به اپلیکیشن شابش خوش آمدید", height=5, font=("B Nazanin", 24))
button_show_zones = Button(window, text="کد منطقه ها", command=show_zones_window, font=("B Nazanin", 18))
button_show_houses = Button(window, text="بررسی خانه های مورد نظر", command=input_search_window, font=("B Nazanin", 18))
button_price_predict = Button(window, text="پیشبینی قیمت خانه", command=input_predict_window, font=("B Nazanin", 18))

# zone window widgets
button_return_to_main = Button(window, text="بازگشت", command=main_window, font=("B Nazanin", 14))

# show predict window widgets
button_return_to_input_predict = Button(window, text="بازگشت", command=input_predict_window, font=("B Nazanin", 14))

# show houses window widgets
button_return_to_input_search = Button(window, text="بازگشت", command=input_search_window, font=("B Nazanin", 14))

# input window widgets
frame1 = Frame(window)
frame2 = Frame(window)
frame3 = Frame(window)
frame4 = Frame(window)
frame5 = Frame(window)
frame6 = Frame(window)

label_input = Label(window, text=": لطفا اطلاعات خانه مورد نظر خود را وارد کنید", bd=5, font=("B Nazanin", 17))
label_input_zone = Label(frame1, text=": کد منطقه", font=("B Nazanin", 17))
label_input_min_area = Label(frame2, text=": حداقل متراژ", font=("B Nazanin", 17))
label_input_max_area = Label(frame3, text=": حداکثر متراژ", font=("B Nazanin", 17))
label_input_area = Label(frame2, text=": متراژ", font=("B Nazanin", 17))
label_input_bedroom = Label(frame3, text=": تعداد اتاق خواب", font=("B Nazanin", 17))
label_input_year = Label(frame4, text=": سال ساخت", font=("B Nazanin", 17))
label_input_min_price = Label(frame4, text=": حداقل میزان قیمت", font=("B Nazanin", 17))
label_input_max_price = Label(frame5, text=": حداکثر میزان قیمت", font=("B Nazanin", 17))

intvar_zone = IntVar()
intvar_area = IntVar()
intvar_min_area = IntVar()
intvar_max_area = IntVar()
intvar_bedroom = IntVar()
intvar_year = IntVar()
intvar_min_price = IntVar()
intvar_max_price = IntVar()

entry_zone = Entry(frame1, textvariable=intvar_zone, justify="center")
entry_area = Entry(frame2, textvariable=intvar_area, justify="center")
entry_min_area = Entry(frame2, textvariable=intvar_min_area, justify="center")
entry_max_area = Entry(frame3, textvariable=intvar_max_area, justify="center")
entry_bedroom = Entry(frame3, textvariable=intvar_bedroom, justify="center")
entry_year = Entry(frame4, textvariable=intvar_year, justify="center")
entry_min_price = Entry(frame4, textvariable=intvar_min_price, justify="center")
entry_max_price = Entry(frame5, textvariable=intvar_max_price, justify="center")
button_submit = Button(frame6, text="ثبت", font=("B Nazanin", 14))

scrollbar = Scrollbar(window)
list_box = Listbox(window, justify=CENTER, font=("B Titr", 13), bg="#B3A9C4", fg="black")

main_window()

window.mainloop()
