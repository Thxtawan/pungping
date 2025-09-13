from tkinter import *
import pyqrcode
import png
from PIL import ImageTk, Image

# ฟังก์ชันสร้าง QR Code
def generate_qr():
    name = name_entry.get()      # ดึงชื่อไฟล์จากช่องกรอก
    url = link_entry.get()       # ดึง URL จากช่องกรอก

    if name and url:
        qr = pyqrcode.create(url)
        qr.png(name + ".png", scale=8)  # สร้าง QR เป็นไฟล์ PNG

        # โหลดภาพ QR Code และแสดงบนแอพ
        qr_image = Image.open(name + ".png")
        qr_image = qr_image.resize((200, 200))
        qr_photo = ImageTk.PhotoImage(qr_image)

        qr_label.config(image=qr_photo)
        qr_label.image = qr_photo  # ต้องเก็บอ้างอิงไว้ ไม่งั้นภาพจะหาย

        status_label.config(text="สร้าง QR Code สำเร็จ!", fg="green")
    else:
        status_label.config(text="กรุณากรอกชื่อและ URL", fg="red")

# เริ่มต้นหน้าต่างแอพ
root = Tk()
root.title("QRCode Generator")

canvas = Canvas(root, width=400, height=550)
canvas.pack()

# หัวข้อ
app_label = Label(root, text="QRCode Generator", font=('Arial', 20, 'bold'))
canvas.create_window(200, 50, window=app_label)

# Label และ Text Entry สำหรับชื่อ
name_label = Label(root, text="ชื่อไฟล์ QR Code")
canvas.create_window(200, 100, window=name_label)

name_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)

# Label และ Text Entry สำหรับ URL
link_label = Label(root, text="URL")
canvas.create_window(200, 160, window=link_label)

link_entry = Entry(root)
canvas.create_window(200, 190, window=link_entry)

# ปุ่มสร้าง QR Code
button = Button(text="สร้างคิวอาร์โค้ด", command=generate_qr)
canvas.create_window(200, 230, window=button)

# ป้ายแสดงสถานะการทำงาน
status_label = Label(root, text="", font=('Arial', 10))
canvas.create_window(200, 270, window=status_label)

# ป้ายสำหรับแสดงภาพ QR Code
qr_label = Label(root)
canvas.create_window(200, 400, window=qr_label)

# เริ่มโปรแกรม
root.mainloop()
