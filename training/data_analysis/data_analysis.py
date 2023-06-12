# 引入 pandas 計算學校男生比例與女生比例的排序
import pandas
# 讀取檔案
data=pandas.read_csv("data_analysis/college.csv")
# 每間學校的學生數與男學生數和女學生數加總
data=data.groupby("學校名稱")[["在學學生數小計", "在學學生數男", "在學學生數女"]].sum()
# 新增在學學生數男比例列
data["在學學生數男比例"]=round((data["在學學生數男"]/data["在學學生數小計"]*100), 0)
# 新增在學學生數女比例列
data["在學學生數女比例"]=round((data["在學學生數女"]/data["在學學生數小計"]*100), 0)
# 依在學學生數男比例排序，由小到大
data=data.sort_values(by="在學學生數男比例", ascending=True)
# 轉換 int
data["在學學生數男比例"]=data["在學學生數男比例"].astype(int)
data["在學學生數女比例"]=data["在學學生數女比例"].astype(int)
# 轉換 string
data["在學學生數男比例"]=data["在學學生數男比例"].astype(str)
data["在學學生數女比例"]=data["在學學生數女比例"].astype(str)
# 加上 %
data["在學學生數男比例"]=data["在學學生數男比例"]+"%"
data["在學學生數女比例"]=data["在學學生數女比例"]+"%"
# 輸出檔案
data.to_csv("data_analysis/new_data.csv", encoding="utf_8_sig")