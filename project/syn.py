# 取得作業系統資訊
import os
# 系統介面工具程式
import shutil
# 接收處理命令行參數
import argparse
# sys 程式庫
import sys
# 處理時間
import time
# 當前路徑的容量、已使用空間以及可使用空間 byte
def disk_capacity(path):
    total, used, free=shutil.disk_usage(path)
    gb=2**30 # gb 單位
    total=round(total/gb, 2) # 總容量
    used=round(used/gb, 2) # 已使用空間
    free=round(free/gb, 2) # 可使用空間
    print(f"磁碟總空間: {total} GB")
    print(f"已使用空間: {used} GB")
    print(f"可使用總空間: {free} GB")
# 解析命令行參數
def getArgs():
    # 建立解析命令物件
    parser=argparse.ArgumentParser()
    # 新增命令行參數
    parser.add_argument("src", help="來源路徑")
    parser.add_argument("aim", help="目標路徑")
    # 解析命令行參數
    args=parser.parse_args()
    # 如果命令行參數輸入錯誤
    if not os.path.isdir(args.src): # 若參數不是輸入資料夾路徑
        print(f"{args.src} 不是資料夾路徑")
        # 退出程式
        sys.exit(2)
    if not os.path.isdir(args.aim): # 若參數不是輸入資料夾路徑
        print(f"{args.aim} 不是資料夾路徑")
        # 退出程式
        sys.exit(2)
    return {"src":args.src, "aim":args.aim}
# 取得檔案的修改時間
def modification_time(file_path):
    # 檔案最後修改時間
    ticks=int(os.path.getmtime(file_path))
    # 解析並結構化為本地時間資料
    # now=time.localtime(ticks)
    # # 格式化時間
    # file_time=time.strftime("%Y年%m月%d日 %H時%M分%S秒", now)
    # print(f"檔案最後修改時間: {file_time}")
    return ticks
# 備份檔案
def backup_file(src, aim):
    # 取得來源路徑的所有檔案路徑
    for dir_path, dir_names, file_name in os.walk(src):
        # 取得路徑的資料夾名稱
        folder_name=dir_path.replace(src, "")
        if folder_name!="": # 如果有資料夾
            # 合併目標路徑與資料夾名稱
            aim_path=rf"{aim}{folder_name}"
            # 當目標路徑沒有該資料夾
            if not os.path.isdir(aim_path):
                # 新增資料夾
                os.mkdir(aim_path)
        for f in file_name: # 各個檔案
            # 原來檔案路徑
            src_path=os.path.join(dir_path, f)
            # 目的檔案路徑
            save_path=os.path.join(aim_path, f)
            # 如果目的檔案路徑沒有檔案
            if not os.path.isfile(save_path):
                # 複製檔案
                shutil.copy2(src_path, save_path)
            else: # 有同檔名的檔案
                # 判斷最後修改時間
                src_time=modification_time(src_path)
                save_time=modification_time(save_path)
                if src_time>save_time: # 如果來源路徑修改時間最晚
                    # 複製檔案
                    shutil.copy2(src_path, save_path)
# 接收 youtube 網址的命令行參數
def selection_youtube():
    # 建立解析命令行物件
    parser=argparse.ArgumentParser()
    # 參數
    parser.add_argument("url", help="youtube 網址")
    # 影片畫質參數
    parser.add_argument("-hd", action="store_true", help="hd(720p)")
    # 影片標題
    parser.add_argument("-t", "--title", action="store", help="影片標題")
    # 解析命令行參數
    args=parser.parse_args()
    # 印出 youtube 網址
    print(f"網址: {args.url}")
    # 如果有選擇影片畫質
    if args.hd:
        print("影片畫質: 720p")
    # 如有打上影片標題
    if args.title:
        print(f"影片標題: {args.title}")
# 將命令行參數加總
def command_sum():
    # 建立解析命令行物件
    parser=argparse.ArgumentParser()
    # 加總
    parser.add_argument("-s", "--sum", type=int, required=True, nargs="+", help="計算加總")
    # 解析命令行參數
    args=parser.parse_args()
    # 建立加總變數
    total=0
    for value in args.sum:
        total+=value
    # 印出數值
    print(f"總和為: {total}")
# 字串串接
def str_concatenated(self_introduction, *args, seq):
    # 確認參數內容是否為字串
    assert isinstance(self_introduction, str), "第一個參數必須是字串且必填"
    # 用 seq 串接字串
    result=f"next: {self_introduction} {seq.join(args)}"
    return result
args=getArgs()
backup_file(args["src"], args["aim"])
