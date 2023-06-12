# 引入執行緒模組
import threading
# 引入時間模組
import time
# 計算平方
def caculate_square(data):
    time.sleep(0.5)
    return data**2
# 計算平方根
def caculate_root(data):
    time.sleep(0.5)
    return data**0.5
# 程式開始時間
start_time=time.time()
data=9
# 建立執行緒物件
t1=threading.Thread(target=caculate_square, args=[data])
t2=threading.Thread(target=caculate_root, args=(data,))
# 啟動執行緒
t1.start()
t2.start()
print(f"進行中的執行緒: {threading.active_count()}")
t1.join() # 等待 t1 執行完畢
t2.join() # 等待 t2 執行完畢
print(f"結束了，花費: {time.time()-start_time}")
print(f"進行中的執行緒: {threading.active_count()}")
print("主程式結束")