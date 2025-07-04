import requests
import re
from tqdm import tqdm

# 获取切片路径
get_m3u8_url = "https://apd-vlive.apdcdn.tc.qq.com/defaultts.tc.qq.com/B_fe3i2LFRVSYybJTzF0kZKM01h170qDM9QVPKVcLr6jJKrOKH7WSNnkYCEgpPvCH-u63d2NW6Z1Svqh64ElGsEHwSSBAkCG0V4pwdNWm39HOWTC14YQYnFSQX0XGFnHAyvKa2H12xmnRPg53rC0v9N_DYhHeYdSgq2JHGIV-DNk4/svp_50112/dh1Y48pPeZ-0bJfcBGTtQxc_wV-sjL-mjVo904HAcl4mNkqYb3chzhsU8WARxAO5qJTFxXtZF09j-dp4XqFkuHA9Seam9Mg_VeKyimBswJSWZqJCI5-FPt-GaH2fZJ1O8MLOd-c_a0YpUMzCRbnIXgn5e5SitnqCTahG03qq4yk9BM6aw2A-Zs6F4vFneuyDyu0573ADlEPguZ63wHA4vopO8lk63gm2QbqHKYUhhxYmcqDZkfv9JA/gzc_1000102_0b53c4apmaaatuapzh33tfsmaf6d6ynqb4sa.f321002.ts.m3u8?ver=4"
head = get_m3u8_url.split("gzc")[0]    # 获取网页必要路径
res = requests.get(get_m3u8_url)    # 获取m3u8文件内容
m3u8_ts = re.sub("#E.*","",res.text).strip().split("\n")    # 数据清洗

with open("video.ts","wb")as f:    # 写入并保存
    for i in tqdm(m3u8_ts):
        if i != "":
            res = requests.get(head + i).content
            f.write(res)
f.close()
