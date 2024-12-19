from customtkinter import *
from login import LoginForm  # Import lớp LoginForm
from PIL import Image
from db_excel import *
from datetime import datetime
import random
from realtime_chart import *
from day_chart import *
from month_chart import *
from db_excel import *
from lastest_data_show import *

class MainApp(CTk):
    def __init__(self):
        super().__init__()
        self.title("Chương trình chính")
        self.geometry("400x300")
        set_appearance_mode("dark")  # Modes: system (default), light, dark
        set_default_color_theme("blue")

        self.day_choose_bieu_do_ngay = ""

        # Hiện form đăng nhập
        self.show_login()

    def show_login(self):
        # Mở cửa sổ đăng nhập
        login_form = LoginForm(on_success=self.open_dashboard)
        login_form.mainloop()

    def open_dashboard(self):
        # Tạo cửa sổ Dashboard
        root = CTkToplevel(self)
        set_appearance_mode("dark")  # Modes: system (default), light, dark
        set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        root.title("My GUI")
        root.geometry("1350x700")

        frame_left = CTkFrame(root)
        frame_left.grid(column=0, row=0, padx=10, pady=6, sticky="NW")
        frame_left_1 = CTkFrame(frame_left)
        frame_left_1.grid(column=0, row=0, padx=10, pady=6)
        # TODO Create image
        my_image = CTkImage(light_image=Image.open("logo.png"),
                            dark_image=Image.open("logo.png"),
                            size=(150, 150))
        # TODO Tao lable de chua anh
        my_logo = CTkLabel(frame_left_1,
                           text="",
                           image=my_image)
        my_logo.grid(column=0, row=0, padx=10, pady=6)
        my_name = CTkLabel(frame_left_1,
                           text="Cristiano Ronaldo",
                           font=("Arial", 12))
        my_name.grid(column=0, row=1, padx=10, pady=6, sticky="W")
        my_class = CTkLabel(frame_left_1,
                            text="Lớp ABC XYZ K61",
                            font=("Arial", 12))
        my_class.grid(column=0, row=2, padx=10, pady=6, sticky="W")
        my_school = CTkLabel(frame_left_1,
                             text="Trường Đại học Thủy Lợi",
                             font=("Arial", 12))
        my_school.grid(column=0, row=3, padx=10, pady=6, sticky="W")

        # Frame cho radio chọn khu vực
        frame_left_2 = CTkFrame(frame_left)
        frame_left_2.grid(column=0, row=1, padx=10, pady=(10, 20), ipadx=33, ipady=20)

        def radiobt_area_handle():
            value = radiobt_value.get()
            if value == 1:
                print("Kv1")
            elif value == 2:
                print("Kv2")
            elif value == 3:
                print("Kv3")
            print(radiobt_value.get())

        radiobt_lable = CTkLabel(frame_left_2, text="Chọn khu vực",
                                 font=("Arial", 16))
        radiobt_lable.grid(column=0, row=0, padx=5, pady=(20, 10))

        radiobt_value = IntVar(value=0)
        radiobt_area_1 = CTkRadioButton(frame_left_2,
                                        text="Khu vực 1",
                                        value=1,
                                        variable=radiobt_value,
                                        font=("Arial", 12),
                                        command=radiobt_area_handle,
                                        radiobutton_width=20,
                                        radiobutton_height=20,
                                        )
        radiobt_area_1.grid(column=0, row=1, padx=5, pady=10)

        radiobt_area_2 = CTkRadioButton(frame_left_2,
                                        text="Khu vực 2",
                                        value=2,
                                        variable=radiobt_value,
                                        font=("Arial", 12),
                                        command=radiobt_area_handle,
                                        radiobutton_width=20,
                                        radiobutton_height=20,
                                        )
        radiobt_area_2.grid(column=0, row=2, padx=5, pady=10)

        radiobt_area_3 = CTkRadioButton(frame_left_2,
                                        text="Khu vực 3",
                                        value=3,
                                        variable=radiobt_value,
                                        font=("Arial", 12),
                                        command=radiobt_area_handle,
                                        radiobutton_width=20,
                                        radiobutton_height=20,
                                        )
        radiobt_area_3.grid(column=0, row=3, padx=5, pady=10)
        radiobt_value.set(1)  # set giá trị đầu là 1

        # Nút nhấn đăng xuất
        def button_logout_handle():
            print("dang xuat")

        button_logout = CTkButton(root, text="Đăng xuất",
                                  command=button_logout_handle,
                                  font=("Arial", 12),
                                  corner_radius=0,
                                  height=35,
                                  width=190)
        # button_logout.grid(column=0, row=2, padx=10, pady=6, sticky="S")
        button_logout.place(relx=0, rely=1, x=10, y=-20, anchor="sw")

        #######################################################################
        # TODO Tạo tabview
        frame_right = CTkFrame(root)
        frame_right.grid(column=1, row=0, padx=10, pady=10, sticky="NW")
        tab_view = CTkTabview(frame_right,
                              anchor="center",
                              width=1050,
                              height=650,
                              corner_radius=5,
                              border_width=1
                              )
        # create tabs
        tab_1 = tab_view.add("Dữ liệu Realtime và Map")
        tab_2 = tab_view.add("Biểu đồ Realtime")
        tab_3 = tab_view.add("Biểu đồ ngày")
        tab_4 = tab_view.add("Biểu đồ tháng")
        tab_5 = tab_view.add("Xuất Excel")
        tab_view.grid(row=0, column=0, padx=20, pady=10)


        display_Sensor = SensorApp(tab_1)
        display_Sensor.pack(fill="both")

        display_RealtimeChartApp = RealtimeChartFrame(tab_2)
        display_RealtimeChartApp.pack(fill="both")

        display_DayChartFrame = DayChartFrame(tab_3)
        display_DayChartFrame.pack(fill="both")

        display_DatabaseExcel = DatabaseExcel(tab_5)
        display_DatabaseExcel.pack(fill="both")

        display_MonthChartApp = MonthChartApp(tab_4)
        display_MonthChartApp.pack(fill="both")







# Chạy chương trình
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
