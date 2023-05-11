# ------------------------------模組------------------------------------
# 解析處理命令行參數
import argparse
# 下載 youtebe
import pytube
# 系統平台
import platform
# pytube 發送請求
import pytube.request
# 取得作業系統資訊
import os
# -----------------------------函式-------------------------------------
# 主程式
def main():
    # 建立解析命令行物件
    parser=argparse.ArgumentParser()
    # 指定 youtube 網址
    parser.add_argument("url", help="指定 youtube 網址")
    # 一般畫質
    parser.add_argument("-sd", action="store_true", help="480p")
    # 高畫質
    parser.add_argument("-hd", action="store_true", help="720p")
    # 高清畫質
    parser.add_argument("-fhd", action="store_true", help="1080p")
    # 解析參數
    args=parser.parse_args()
    # 建立 youtube 物件，呼叫進度條函式
    yt=pytube.YouTube(args.url, on_progress_callback=onProgress)
    # 下載影片函式
    download_video(yt, args)
# 進度條 (無法下載中讀取)
def onProgress(stream, chunk, bytes_remaining):
    # chunk 更改為 1mb (github 的方法)
    pytube.request.default_range_size=8
    # 檔案大小
    file_total=stream.filesize
    # 下載進度數字
    progress_number=round((file_total-bytes_remaining)/file_total*100, 2)
    print(f"下載中...{progress_number}%")
# 下載影片
def download_video(yt, args):
    if args.sd: # 選擇一般畫質
        target=yt.streams.filter(type="video", resolution="480p").first()
    elif args.hd: # 選擇高畫質
        target=yt.streams.filter(type="video", resolution="720p").first()
    elif args.fhd: # 選擇高清畫質
        target=yt.streams.filter(type="video", resolution="1080p").first()
    # 下載影片
    if target: # 如果有此畫質
        target.download(output_path=pytube_folder())
    else:
        pd_list=pd_selection(yt) # 選擇有的畫質
        print(f"指定的畫質並沒有提供，以下是此影片提供的畫質:")
        for pd in pd_list:
            print(pd)
        try:
            user_selection=int(input("請選擇: "))
        except:
            print("請輸入整數")
        else:
            for number in range(1, len(pd_list)+1):
                if user_selection==number: # 選擇以後
                    res=pd_list[number-1][3:]
                    target=yt.streams.filter(type="video", resolution=res).first()
                    # 下載影片
                    target.download(output_path=pytube_folder())
# 選擇該影片的畫質
def pd_selection(yt):
    pd_list=[]
    if yt.streams.filter(res="360p"): # 該影片有 360p
        pd_list.append("360p")
    if yt.streams.filter(res="480p"): # 該影片有 480p
        pd_list.append("480p")
    if yt.streams.filter(res="720p"): # 該影片有 720p
        pd_list.append("720p")
    if yt.streams.filter(res="1080p"): # 該影片有 1080p
        pd_list.append("1080p")
    for number in range(1, len(pd_list)+1):
        # 將影片提供的畫質加入編號
        pd_list[number-1]=f"{number}) {pd_list[number-1]}"
    return pd_list
# 辨別系統平台
def pytube_folder():
    # 系統
    sys=platform.system()
    # 使用者家目錄
    home=os.path.expanduser("~")
    if sys=="Windows": # 若是 windows
        # 串接路徑
        folder=os.path.join(home, "Videos", "pytube")
    elif sys=="Darwin": # mac os
        folder=os.path.join(home, "Videos", "pytube")
    # 若沒有此資料夾，才做新增
    if not os.path.isdir(folder):
        os.mkdir(folder)
    return folder # 回傳資料夾路徑
# -----------------------------主程式-----------------------------------
main()