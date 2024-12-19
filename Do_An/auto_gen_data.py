import sqlite3
import time
from datetime import datetime
import random

# Tạo kết nối đến database và bảng measurements
def create_database(tendatabase):
    conn = sqlite3.connect(tendatabase)
    cursor = conn.cursor()

    # Tạo bảng measurements nếu chưa tồn tại
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS measurements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_save TEXT,
            time_save TEXT,
            temp REAL,
            humi REAL,
            co REAL,
            pm25 REAL,
            nh3 REAL,
            airpresser REAL
        )
    ''')

    conn.commit()
    conn.close()

def insert_data(tendatabase):
    conn = sqlite3.connect(tendatabase)
    cursor = conn.cursor()

    # Lấy thời gian hiện tại
    now = datetime.now()
    date_save = now.strftime("%d/%m/%Y")
    time_save = now.strftime("%H:%M:%S")

    # Sinh dữ liệu ngẫu nhiên
    temp = round(random.uniform(20.0, 35.0), 2)  # Nhiệt độ từ 20.0 đến 35.0 độ C
    humi = round(random.uniform(30.0, 80.0), 2)  # Độ ẩm từ 30.0% đến 80.0%
    co = round(random.uniform(0.0, 10.0), 2)     # CO từ 0.0 đến 10.0 ppm
    pm25 = round(random.uniform(0.0, 50.0), 2)   # PM2.5 từ 0.0 đến 50.0 µg/m3
    nh3 = round(random.uniform(0.0, 5.0), 2)     # NH3 từ 0.0 đến 5.0 ppm
    airpresser = round(random.uniform(950.0, 1050.0), 2)  # Áp suất khí quyển từ 950.0 đến 1050.0 hPa

    # Chèn dữ liệu vào bảng
    cursor.execute('''
        INSERT INTO measurements (date_save, time_save, temp, humi, co, pm25, nh3, airpresser)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (date_save, time_save, temp, humi, co, pm25, nh3, airpresser))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database("database1.db")
    create_database("database2.db")
    create_database("database3.db")
    try:
        while True:
            insert_data("database1.db")
            insert_data("database2.db")
            insert_data("database3.db")
            print("Dữ liệu đã được ghi vào database.")
            time.sleep(20)  # Chờ 20 giây
    except KeyboardInterrupt:
        print("Chương trình đã dừng.")