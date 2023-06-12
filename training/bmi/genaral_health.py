# 綜合健康計算機
# bmi
def bmi():
    height=float(input("請輸入您的身高： "))
    weight=float(input("請輸入您的體重： "))
    result=round(weight/((height/100)**2), 1)
    return result
# bmr
def bmr():
    gender=input("請輸入您的性別： ")
    age=int(input("請輸入您的年齡： "))
    height=float(input("請輸入您的身高： "))
    weight=float(input("請輸入您的體重： "))
    if gender=="男":
        # 66＋( 13.7*體重kg＋5*身高cm－6.8*年齡)
        result=66+(13.7*weight+5*height-6.8*age)
        return round(result, 2)
    elif gender=="女":
        # 女：655＋( 9.6*體重kg＋1.8*身高cm－4.7*年齡)
        result=655+(9.6*weight+1.8*height-4.7*age)
        return round(result, 2)
    else:
        return ("error")
# tdee
def tdee():
    """
    活動量	活動量描述	TDEE計算方法
    輕量活動	每周運動1-3天	TDEE = 1.375 x BMR
    中度活動量	每周運動3-5天	TDEE = 1.55 x BMR
    高度活動量	每周運動6-7天	TDEE = 1.725 x BMR
    非常高度活動量	無時無刻都在運動XD	TDEE = 1.9 x BMR
    """
    BMR=bmr()
    # 取得使用者每周活動量
    activity=input("""\n請輸入您的每周活動量描述：\n
(1)每周運動1-3天
(2)每周運動3-5天
(3)每周運動6-7天
(4)無時無刻都在運動
(輸入 1 or 2 or 3 or 4): """)
    if activity=="1":
        tdee=1.375*BMR
    elif activity=="2":
        tdee=1.55*BMR
    elif activity=="3":
        tdee=1.725*BMR
    elif activity=="4":
        tdee=1.9*BMR
    else:
        return ("error")
    return round(tdee, 2)
print("""歡迎使用綜合健康計算機
(1) 計算bmi
(2) 計算基礎代謝率(bmr)
(3) 計算總熱量消耗(tdee)""")
user_selection=input("請選擇要計算的項目 (輸入 1 or 2 or 3): ")
if user_selection=="1":
    result=bmi()
    print(f"bmi: {result}")
elif user_selection=="2":
    result=bmr()
    print(f"bmr: {result}")
elif user_selection=="3":
    result=tdee()
    print(f"tdee: {result}")
else:
    print("error")