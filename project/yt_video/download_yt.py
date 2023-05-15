import pytube
# youtube 網址
yt_url="https://www.youtube.com/watch?v=h4s4MAmwqN0"
# 建立 youtube 物件
yt_obj=pytube.YouTube(yt_url)
# 影片標題
title=yt_obj.title
# 全部檔案格式
all_format=yt_obj.streams
# 篩選畫質為 1080p 的影片
fhd_format=yt_obj.streams.filter(resolution="1080p").first()
fhd_format.download()