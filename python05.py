#กำหนดให้ m และ n เป็นตัวแปรชนิดจำนวนเต็ม ให้รับค่าตัวเลขเข้ามา 2 จำนวน แล้วแสดงผลลบของทั้ง 2 จำนวน
num1 = int(input("num1 = "))
num2 = int(input("num2 = "))
print("Result = %d" %(num1-num2))

#จงเขียนโปรแกรม รับค่า ชื่อ นามสกุล และ อายุ พร้อมแสดงผลดังตัวอย่าง
name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
age = int(input("Enter your age : "))
print("Hello %s %s\nYou're %d years old" % (name, last_name, age))