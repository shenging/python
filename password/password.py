# 密碼產生器
import random
letters_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                 "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]

letters_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+"]

needs_upper=int(input("請輸入要幾個大寫字母? "))
needs_lower=int(input("請輸入要幾個小寫字母? "))
needs_number=int(input("請輸入要幾個數字? "))
needs_symbol=int(input("請輸入要幾個特殊符號? "))
# 需要的隨機大寫
new_upper=random.sample(letters_upper, needs_upper)
# 需要的隨機小寫
new_lower=random.sample(letters_lower, needs_lower)
# 需要的隨機數字
new_number=random.sample(numbers, needs_number)
# 需要的隨機符號
new_symbol=random.sample(symbols, needs_symbol)
# 將所有需要的拼湊起來
new_password=new_upper+new_lower+new_number+new_symbol
# 打亂 new_password
random.shuffle(new_password)
result="".join(new_password)
print(f"你的密碼: {result}")