# 剪刀石頭布
import random
data=[
    '''
        _______
    ---'   ____)______
                ______)
            __________)
            (____)
     ---.__(___)
    '''
    ,
    '''
        _______
    ---'   ____)
         (_____)
         (_____)
         (____)
    ---.__(___)
    '''
    ,
    '''
        _______
    ---'   ____)____
                ______)
                _______)
                _______)
        ---.__________)
    '''
]
# 隨機取 0~2 0:剪刀 1:石頭 2:布
number=random.randint(0, 2)
computer_answer=data[number]
# 取得使用者的猜拳
user_answer=input("準備開始 剪刀石頭布~ (輸入剪刀、石頭、或布): ")
# 判斷結果
if user_answer=="剪刀":
    user_answer=data[0]
    if number==0:
        result="哎呀，平手了呢"
    elif number==1:
        result="你輸了哈哈"
    elif number==2:
        result="挖賽 怎麼贏了 好猛喔"
    else:
        result="錯誤"
elif user_answer=="石頭":
    user_answer=data[1]
    if number==1:
        result="哎呀，平手了呢"
    elif number==2:
        result="你輸了哈哈"
    elif number==0:
        result="挖賽 怎麼贏了 好猛喔"
    else:
        result="錯誤"
elif user_answer=="布":
    user_answer=data[2]
    if number==2:
        result="哎呀，平手了呢"
    elif number==0:
        result="你輸了哈哈"
    elif number==1:
        result="挖賽 怎麼贏了 好猛喔"
    else:
        result="錯誤"
else:
    print("錯誤")

print(f"電腦出: \n{computer_answer}")
print(f"你出: \n{user_answer}")
print(result)



