print("1. for i in range(1, 101)")
count = 0
for i in range(1, 101):
    count += 1
print("ทำงานทั้งหมด:", count, "รอบ")
print("ค่า i สุดท้าย:", i)
print("-" * 30)

print("2. for i in range(7, 77, 7)")
count = 0
for i in range(7, 77, 7):
    count += 1
print("ทำงานทั้งหมด:", count, "รอบ")
print("ค่า i สุดท้าย:", i)
print("-" * 30)

print("3. for i in range(20, 1, -2)")
count = 0
for i in range(20, 1, -2):
    count += 1
print("ทำงานทั้งหมด:", count, "รอบ")
print("ค่า i สุดท้าย:", i)
print("-" * 30)

print("4. for i in range(2, 18, 3)")
count = 0
for i in range(2, 18, 3):
    count += 1
print("ทำงานทั้งหมด:", count, "รอบ")
print("ค่า i สุดท้าย:", i)
print("-" * 30)

print("5. for i in range(55, 0, -11)")
count = 0
for i in range(55, 0, -11):
    count += 1
print("ทำงานทั้งหมด:", count, "รอบ")
print("ค่า i สุดท้าย:", i)
print("-" * 30)

print("6. for i in range(1, 0)")
count = 0
for i in range(1, 0):
    count += 1
if count == 0:
    print("ลูปไม่ทำงานเลย")
    print("ไม่มีค่าของ i")
else:
    print("ทำงานทั้งหมด:", count, "รอบ")
    print("ค่า i สุดท้าย:", i)
print("-" * 30)
