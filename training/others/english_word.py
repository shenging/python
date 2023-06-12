# 英文單字練習機
import random
eng_dic = {
    "蘋果": "apple",
    "香蕉": "banana",
    "貓": "cat",
    "狗": "dog",
    "蛋": "egg",
    "食物": "food",
    "遊戲": "game",
    "手": "hand",
    "冰": "ice",
    "果醬": "jam",
    "國王": "king",
    "標籤": "label",
    "郵件": "mail",
    "脖子": "neck",
    "油": "oil",
    "豬": "pig",
    "皇后": "queen"
}
# 使用者要練習的題數
user_practice=int(input("請問你要練習幾題阿? "))
# 根據題數隨機取題
exams=random.sample(list(eng_dic), k=user_practice)
correct_answer=0
for exam in exams:
    user_answer=input(f"\n請問 {exam} 的英文是? ")
    if user_answer.lower()!=eng_dic[exam]:
        print(f"哎呀，你答錯了呢，答案是 {eng_dic[exam]}")
    elif user_answer.lower()==eng_dic[exam]:
        print("恭喜答對壓~")
        correct_answer+=1
    else:
        print("錯誤")
print(f"\n總共答對了 {correct_answer} 題")
    