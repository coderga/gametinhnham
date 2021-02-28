import random
import time
import os
import sys
os.system('clear')

def delete_last_line():
    #cursor up one line
    sys.stdout.write('\x1b[1A')
    #delete last line
    sys.stdout.write('\x1b[2K')

def countdown(t):
    while t > 0:
        # print(t, end="\r")
        print(t)
        delete_last_line()
        t -= 1
        time.sleep(1)
    print("START")
    

soluongso = [5,10,20]
thoigian = [2,1,0.5]
sochuso = [1,2,4]
pheptinh = [1,-1]
def songaunhien(capdokho,thoigian,soluong,sochuso):
    sum = 0
    listnum = []
    for sluong in range(0,soluong):
        num = random.randint(10**(sochuso-1),10**sochuso-1)#*random.choice(pheptinh)
        sum = sum + num
        print(str(num) + "  <= Số thứ " + str(sluong+1))
        listnum.append(num)
        time.sleep(thoigian)
        # os.system('clear')
        delete_last_line()
    t = int(input("Nhập vào kết quả của bạn: "))
    if t == sum:
        print("Kết quả của bạn đúng.")
    else:
        print("Kết quả của bạn sai")
    print("Danh sách các số: ", listnum)
    print("Tổng của tất cả các số là: ", sum)


# print(songaunhien(2,5))
print("Chương trình tính nhẩm siêu tốc")
dk = int(input("Nhập vào cấp độ khó bạn muốn chơi: "))
print("Độ khó cấp: ",dk)
print("====================================")
countdown(3)
delete_last_line()
time.sleep(1)
songaunhien(dk,thoigian[dk-1],soluongso[dk-1],sochuso[dk-1])