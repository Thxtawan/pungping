import tkinter as tk
from tkinter import messagebox

def calculate_area():
    try:
        base = float(entry_base.get())
        height = float(entry_height.get())
        
        if base <= 0 or height <= 0:
            messagebox.showerror("ข้อผิดพลาด", "ฐานและสูงต้องเป็นเลขบวกเท่านั้น")
            return
        
        area = 0.5 * base * height
        label_result.config(text=f"พื้นที่สามเหลี่ยม = {area:.2f} หน่วย")
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกตัวเลขฐานและสูงให้ถูกต้อง")

# สร้างหน้าต่างหลัก
window = tk.Tk()
window.title("โปรแกรมคำนวณพื้นที่สามเหลี่ยม")

# ป้ายและช่องกรอกฐาน
label_base = tk.Label(window, text="ฐาน (Base):")
label_base.pack()
entry_base = tk.Entry(window)
entry_base.pack()

# ป้ายและช่องกรอกสูง
label_height = tk.Label(window, text="สูง (Height):")
label_height.pack()
entry_height = tk.Entry(window)
entry_height.pack()

# ปุ่มคำนวณ
button_calc = tk.Button(window, text="คำนวณพื้นที่", command=calculate_area)
button_calc.pack(pady=10)

# ป้ายแสดงผลลัพธ์
label_result = tk.Label(window, text="")
label_result.pack()

# เริ่มโปรแกรม
window.mainloop()
