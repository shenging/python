# 拉麵點餐機
print("""歡迎使用拉麵點餐機\n
(1)豚骨拉麵 $180
(2)牡蠣拉麵 $220
(3)醬油拉麵 $170""")
# 取得使用者的選擇
user_selection=input("\n請選擇拉麵口味 (輸入 1 or 2 or 3): ")
if user_selection=="1":
    price=180
elif user_selection=="2":
    price=220
elif user_selection=="3":
    price=170
else:
    print("error")
# 取得使用者是否加價購其他品項
add=input("是否加大? 豚骨口味 + $30 ，其他 + $50 (輸入 Y or N) ")
egg=input("是否加糖心蛋? + $10 (輸入 Y or N) ")
pork=input("是否加叉燒肉? + $40 (輸入 Y or N)")
# 如果有加大
if add.upper()=="Y":
    if user_selection=="1": # 有加大且吃的是豚骨拉麵
        price+=30
    elif user_selection=="2" or user_selection=="3":
        price+=50
    else:
        print("error")
# 如果有加蛋
if egg.upper()=="Y":
    price+=10
elif egg.upper()=="N":
    price+=0
else:
    print("error")
# 如果有加叉燒
if pork.upper()=="Y":
    price+=40
elif pork.upper()=="N":
    price+=0
else:
    print("error")

print(f"\n\n總金額是{price}，謝謝光臨")
