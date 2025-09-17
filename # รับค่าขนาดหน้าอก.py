# รับค่าขนาดหน้าอก (จำนวนเต็ม)
chest_size = int(input("กรุณาใส่ขนาดหน้าอก: "))

# ตรวจสอบขนาดเสื้อ
if chest_size <= 34:
    size = "XS"
elif chest_size <= 36:
    size = "S"
elif chest_size <= 38:
    size = "M"
elif chest_size <= 40:
    size = "L"
else:
    size = "XL"

# แสดงผล
print(f"ขนาดเสื้อโปโลที่เหมาะสมคือ: {size}")