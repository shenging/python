# 猜數字遊戲
import random
print("歡迎來到猜數字遊戲")
print("答案為1~100的數字(最多猜10次)")
# 從 1~100 中隨機挑一個答案
computer_answer=random.randint(1,100)
number=1
while number<11:
    print(f"第{number}次猜")
    user_answer=int(input("猜猜看數字是多少? "))
    if number==10:
        if computer_answer==user_answer:
            print("恭喜答對啦~")
            break
        else:
            print(f"哈哈你輸了，答案是 {computer_answer}")
    elif computer_answer>user_answer:
        print("哎呀，在猜大一點呀")
    elif computer_answer<user_answer:
        print("哎呀呀，在猜小一點阿")
    elif computer_answer==user_answer:
        print("恭喜答對啦~")
        break
    else:
        print("error")
    number+=1


    