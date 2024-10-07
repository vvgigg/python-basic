#input and output02
print("*")
print("*"*2)
print("*"*3)
print("*"*50)

#รับค่าตัวเลขเข้ามา 2 จำนวน แล้วทำการหาผลรวมของสองตัวเลข
a = int(input())
b = int(input())
print("sum = %d" %(a+b))

#รับค่า * เข้ามาหนึ่งครั้ง จากนั้นรับตัวเลขจำนวนเต็ม แล้วให้แสดงผลลัพธ์ดังนี
star = input("Enter star: ")
num = int(input("Enter number : "))
print("Result = %s" %(star*num))

#รับค่าตัวเลขจำนวนเต็ม 3 จำนวน จากนั้นทำการหาค่าเฉลี่ย
num1 = int(input("num1 = "))
num2 = int(input("num2 = "))
num3 = int(input("num3 = "))
print("average = %.2f" %((num1+num2+num3)/3))
