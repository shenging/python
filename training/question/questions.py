# 問答程式
# 隨機從 questions.json 抽 5 題 作答 每題恭喜答對和訂正 最後計算答對題數
import json
import random
# 建立問題類別
class Question:
    def __init__(self, description, answer):
        self.description=description
        self.answer=answer
    def check_correct(self):
        # 取得使用者的答案
        user_answer=input(self.description)
        # 比對是否正確
        if user_answer.lower()==self.answer:
            # 正確
            return True
        else:
            return False
# 讀取 json 檔案
with open ("questions.json", mode="r", encoding="utf-8") as file:
    # 讀取檔案
    questions=file.read()
    # 將 json 檔案轉為 python 格式
    questions=json.loads(questions)
    # 隨機抽 5 題不重複的題目
    questions=random.sample(questions, k=10)
    # 建立答對題數變數
    correct=0
    for number in range(0, 10):
        question=Question(questions[number]["description"], questions[number]["answer"])
        if question.check_correct():
            print("恭喜答對啦~")
            correct+=1
        else:
            print(f"哎呀，答錯了，答案是{question.answer}")
    print(f"總共答對了{correct}題")