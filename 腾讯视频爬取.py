import requests
import re
from tqdm import tqdm

get_m3u8_url = "https://apd-vlive.apdcdn.tc.qq.com/……"    # 获取切片路径
head = get_m3u8_url.split("gzc")[0]    # 获取网页必要路径
res = requests.get(get_m3u8_url)    # 获取m3u8文件内容
m3u8_ts = re.sub("#E.*","",res.text).strip().split("\n")    # 数据清洗

with open("video.ts","wb")as f:    # 写入并保存
    for i in tqdm(m3u8_ts):
        if i != "":
            res = requests.get(head + i).content
            f.write(res)
f.close()
