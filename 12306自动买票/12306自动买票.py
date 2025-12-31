from DrissionPage import ChromiumPage
from DrissionPage.common import Actions,Keys
from pypinyin import pinyin,Style
import requests
import json
def To_pinyin(chinese):
    Chinese = pinyin(chinese,style=Style.NORMAL)
    Spinyin = "".join([i[0] for i in Chinese])
    return Spinyin

def Buy_ticket(Go_station,To_station,Date,Ticket_index):
    auto = ChromiumPage()
    auto.get("https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E6%B3%89%E5%B7%9E,QYS&ts=%E7%A6%8F%E5%B7%9E,FZS&date=2025-07-04&flag=N,N,Y")

    action = Actions(auto)
    # 出发地
    action.move_to("css:#fromStationText").click()
    auto.ele("css:#fromStationText").clear()
    action.move_to("css:#fromStationText").click().type(To_pinyin(Go_station))
    auto.ele("css:#fromStationText").input(Keys.ENTER)
    # 目的地
    action.move_to("css:#toStationText").click()
    auto.ele("css:#toStationText").clear()
    action.move_to("css:#toStationText").click().type(To_pinyin(To_station))
    auto.ele("css:#toStationText").input(Keys.ENTER)
    # 出发日期
    auto.ele("css:#train_date").clear()
    auto.ele("css:#train_date").input(Date)
    # 进行查询
    auto.ele("css:#query_ticket").click()
    # 进行购票
    auto.ele(f"css:#queryLeftTable tr:nth-child({int(Ticket_index) * 2 - 1}) .btn72").click()


    # 登录判断
    login = auto.ele("css:#login_user").text
    if login == "登录":
        phone = input("请输入手机号：")
        auto.ele("css:#J-userName").input(phone)

        passwd = input("请输入密码：")
        auto.ele("css:#J-password").input(passwd)
        auto.ele("css:#J-login").click()    # 登录

        Id = input("请输入身份证后四位：")
        auto.ele("css:#id_card").input(Id)

        auto.ele("css:#verification_code").click()  # 获取验证码

        code = input("请输入验证码：")
        auto.ele("css:#code").input(code)

        auto.ele("css:#sureClick").click()  # 验证登录
    else:
        name = auto.ele("css:#login_user").text
        print(f"{name}已登录")


file = open("station.json",encoding = 'utf-8').read()   # 获取站台名称
station = json.loads(file)

go_station = input("出发地: ")
to_station = input("目的地: ")
date = input("出发日期(yyyy-MM-dd): ")

url = f"https://kyfw.12306.cn/otn/leftTicket/queryU?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={station[go_station]}&leftTicketDTO.to_station={station[to_station]}&purpose_codes=ADULT"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Cookie":"_uab_collina=175161775262015573617665; JSESSIONID=46427780E852D810AD62804DB95E72BE; BIGipServerotn=1524171018.24610.0000; BIGipServerpassport=1005060362.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; route=c5c62a339e7744272a54643b3be5bf64; _jc_save_fromStation=%u798F%u5DDE%2CFZS; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2025-07-04; _jc_save_toDate=2025-07-04; _jc_save_wfdc_flag=dc",
    "Referer":"https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E7%A6%8F%E5%B7%9E,FZS&ts=%E4%B8%8A%E6%B5%B7,SHH&date=2025-07-04&flag=N,N,Y"
}
res = requests.get(url,headers=headers)
json = res.json()
data = json["data"]["result"]   # 数据

count = 0
for i in data:
    count += 1
    clsdata = i.split("|")
    # 通过下标取值
    # index = 0
    # for j in clsdata:
    #     print(f"{j} -> index: {index}")
    #     index += 1
    dic = {"车次":clsdata[3],"出发时间":clsdata[8],"到达时间":clsdata[9],"行驶时间":clsdata[10],"商务座":clsdata[32],"一等座":clsdata[31]  ,"二等座":clsdata[30]}
    print(f"【{count}】：{dic}")
print(f"共有：{count} 班车")

ticket_index = input("选择购买的车次序号:")
Buy_ticket(Go_station = go_station,To_station = to_station,Date = date,Ticket_index = ticket_index)