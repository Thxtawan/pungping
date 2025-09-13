import tkinter as tk

def show_info():
    # แสดงข้อความใน Label
    label_result.config(text="ชื่อ : ฐตวรรณ พงษ์พยัคฆ์\nชั้น : 5/8\nเลขที่ : 15")

# สร้างหน้าต่างหลัก
window = tk.Tk()
window.title("ข้อมูลนักเรียน")

# สร้างปุ่มกด
button = tk.Button(window, text="กดเพื่อแสดงข้อมูล", command=show_info)
button.pack(pady=20)

# สร้าง Label เพื่อแสดงข้อความ
label_result = tk.Label(window, text="")
label_result.pack()

# เริ่มโปรแกรม
window.mainloop()
