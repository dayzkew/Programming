#!/usr/bin/env python
# coding: utf-8

# 1.กำหนดให้ brand_cars = ("Toyota", "Honda", "Benz", "BMW", "Tesla", "Ford", "KIA", "Volvo" )
# 
# 1.1 ให้เขียนคำสั่งโปรแกรมแสดงตำแหน่งของ Benz, Ford และ Volvo
# 1.2 ให้เขียนคำสั่งโปรแกรมแสดงจำนวนข้อมูลทั้งหมดในทูเพิล
# 1.3 ให้เขียนคำสั่งโปรแกรมตรวจสอบมียี่ห้อรถ Suzuki, Ferrari, Ford อยู่ใน cars หรือไม่

# In[1]:


brand_cars = ("Toyota", "Honda", "Benz", "BMW", "Tesla", "Ford", "KIA", "Volvo" )
print("ตำแหน่งของยี่ห้อ Volvo คือ",brand_cars.index("Volvo"))
print("ตำแหน่งของ KIA คือ",brand_cars.index("KIA"))
print("ตำแหน่งของ Ford คือ",brand_cars.index("Ford"))
print("จำนวนข้อมูลทั้งหมดในทูเพิล คือ",len(brand_cars),"รายการ")
print("มียี่ห้อรถ Tesla อยู่ใน brand_cars หรือไม่ =","Teslai" in brand_cars)
print("มียี่ห้อรถ BMW อยู่ใน brand_cars หรือไม่ =","BMWi" in brand_cars)
print("มียี่ห้อรถ Honda อยู่ใน brand_cars หรือไม่ =","Honda" in brand_cars)


# In[ ]:




