

import re

# Email Validation
email = input("Enter an email: ")

pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

if re.match(pattern, email):
    print("✅ Valid email address.")
else:
    print("❌ Invalid email address.")

#check the phone number, either it valid or not 
import re

phone = input("Enter Bangladeshi phone number: ")

pattern = r'^(\+8801[3-9]\d{8}|01[3-9]\d{8})$'

if re.match(pattern, phone):
    print("✅ Valid Bangladeshi mobile number.")
else:
    print("❌ Invalid number.")
import random

# Example list
items = ["apple", "banana", "cherry", "date", "elderberry"]
random_index = random.randint(0, len(items) - 1)
removed_item = items.pop(random_index)
print(f"Removed item: {removed_item}")

print(f"Updated list: {items}")


#check rgistration number
import re

def is_valid_vehicle_number(number):
    # Example: DHAKA METRO-BA-11-1234
    pattern = r'^[A-Z]{3,10}\sMETRO-[A-Z]{1,2}-\d{2}-\d{4}$'
    return bool(re.match(pattern, number))

# Test
vehicle_num = input("Enter vehicle registration number: ").strip().upper()
if is_valid_vehicle_number(vehicle_num):
    print("✅ Valid Vehicle Registration Number")
else:
    print("❌ Invalid Vehicle Registration Number")
import re

def is_valid_vehicle_number(number):
    # Example: DHAKA METRO-BA-11-1234
    pattern = r'^[A-Z]{3,10}\sMETRO-[A-Z]{1,2}-\d{2}-\d{4}$'
    return bool(re.match(pattern, number))

# Test
vehicle_num = input("Enter vehicle registration number: ").strip().upper()
if is_valid_vehicle_number(vehicle_num):
    print("✅ Valid Vehicle Registration Number")
else:
    print("❌ Invalid Vehicle Registration Number")


#password strong or not 

import re

def is_strong_password(password):
    if (len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'\d', password) and
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
        return True
    return False

# Test
password = input("Enter your password: ")
if is_strong_password(password):
    print("✅ Strong Password")
else:
    print("❌ Weak Password")
