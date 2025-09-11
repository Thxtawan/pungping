import math

# --- ข้อ 1: คำนวณค่าจอดรถ ---
hour = int(input("ชั่วโมงที่จอดรถ: "))
minute = int(input("นาทีที่จอดรถ: "))

if hour < 0 or minute < 0:
    print("โปรดใส่ข้อมูลที่ไม่ติดลบ")
else:
    total_time = hour + (1 if minute > 0 else 0)  # ถ้ามีเศษนาที ให้นับเป็นอีก 1 ชั่วโมง
    if total_time <= 1:
        fee = 0
    else:
        fee = (total_time - 1) * 30  # ชั่วโมงแรกฟรี
    print("ค่าจอดรถ:", fee, "บาท")

# --- ข้อ 2: คำนวณเงิน USD เป็น THB ---
usd = float(input("จำนวนเงิน (USD): "))

if usd > 0:
    thb = usd * 32.5
    print("จำนวนเงินเป็นบาท (THB):", thb)
else:
    print("You don’t have money")
