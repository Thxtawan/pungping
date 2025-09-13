def add(a, b):
    return a + b

def square(a):
    return a ** 2

def get_month_name(month_number):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    if 1 <= month_number <= 12:
        return months[month_number - 1]
    else:
        return "Invalid month number"

def concat_strings(str1, str2, str3):
    return str1 + str2 + str3

def apply_discount(price, discount):
    return price - (price * discount / 100)
