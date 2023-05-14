import pickle
data=[
    {
        "紅色": "red", 
        "黃色": "yellow",
        "藍色": "blue"
    }
]
try:
    with open ("data.dat", mode="wb") as file:
        pickle.dump(data, file)
        print("新增成功")
except:
    print("新增失敗")
else:
    with open ("data.dat", mode="rb") as file:
        d=pickle.load(file)
    print(d)