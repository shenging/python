# BMI 計算機
height=float(input("請輸入您的身高： "))
weight=float(input("請輸入您的體重： "))
result=round(weight/((height/100)**2), 1)
print(f"您的 BMI 是: {result}")