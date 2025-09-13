import tkinter as tk

# สร้างหน้าต่างหลัก
window = tk.Tk()
window.title("นับถอยหลังแล้วแสดงข้อมูล")
window.geometry("400x300")

# ตัวแปรเก็บเวลาถอยหลัง
count = 10

# ป้ายแสดงผล
label = tk.Label(window, text="", font=("TH SarabunPSK", 24))
label.pack(pady=30)

def countdown():
    global count
    if count > 0:
        label.config(text=str(count))
        count -= 1
        window.after(1000, countdown)  # รอ 1000 ms แล้วเรียกตัวเองซ้ำ
    else:
        show_info()

def show_info():
    info = (
        "ชื่อ: ฐตวรรณ\n"
        "นามสกุล: พงษ์พยัคฆ์\n"
        "ชื่อเล่น: ปุ้ง\n"
        "ห้องเรียน: 5/8\n"
        "แผนการเรียน: เทคโนโลยี\n"
        "อยากเรียนคณะ: วิศวะคอม"
    )
    label.config(text=info, font=("TH SarabunPSK", 18))

# เริ่มนับถอยหลัง
countdown()

# เริ่ม GUI
window.mainloop()
