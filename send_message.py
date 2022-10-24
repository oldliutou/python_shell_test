# encoding: utf-8
import requests
import json
import time
import datetime
import random
'''
把你从微信公众平台获取到的
appid、
secret、
微信用户id、
模板id、
城市id
替换成你自己的，就能运行了，代码里的信息我处理过了，不替换是不能直接跑的
然后模板那边再自定义一下就实现了你的专属消息提醒
'''
def main(even,s):
    import time
    print(even,s)
    appid = 'wx9dsdsd627c7'
    secret = 'b9708dsad'
    touser = ['orKVg5_j4dasdMRY_jU']  # 微信用户id
    template_id = 'rFFFRcK2asdsaQzhHN7FaRg'  # 模板id
    city_id = '32523523'  # 城市天气id
    # birthday = "1995-04-10"
    # 考研日期，懒得改变量名了
    birthday = '2023-10-12'

    List_A = ['干饭人，干饭魂','人是铁，饭是钢，一顿不吃饿得慌','身体是革命的本钱，记得吃饭','玩玩乐乐吃吃喝喝，做个可爱迷人的小甜豆','恋爱可以慢慢谈，肉必须趁热吃','按时吃饭，早睡早起，自律如昔，能扛大事','天要下雨 ，菜要下饭','吃货的最高境界 ——眼见为食','世界这么大，我们去吃吃看','尊敬的客户：现已到吃饭时间，你已较长时间没有进食了，请抓紧时间吃饭，逾期将收取滞纳期限','你的胃来求我，让我告诉你，好好吃饭吧，别虐待我','火锅、烧烤、啤酒，不是很贵，但很对胃','人生苦短,再来一碗','人生得意须尽欢，胡吃海塞需尽兴']
    # List_A = ['天要下雨 ，菜要下饭。','吃货的最高境界 ——眼见为食。']
    e = List_A[random.randint(0,len(List_A)-1)]  # 底部信息

    grant_type = 'client_credential'
    url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type={grant_type}&appid={appid}&secret={secret}'
    response = requests.get(url).json()
    access_token = ''
    if response['expires_in'] == 7200:
        # 获取token
        access_token = response['access_token']
        # 天气获取
        # headers = {
        #     # 'Referer': 'http://www.weather.com.cn/',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        # }
        # url = f'http://d1.weather.com.cn/weather_index/{city_id}.html?_=' + str(int(round(time.time() * 1000)))
        url = f"http://t.weather.sojson.com/api/weather/city/{city_id}"
        # 日期计算
        r = requests.get(url).text
        print(r)
        # r.encoding = "utf8"
        r = json.loads(r)
        res = r["data"]['forecast'][0]
        print(res)
        time = r["data"]['forecast'][0]["ymd"]
        year = time[0:4]
        month = time[5:7]
        day = time[8:10]
        week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
        week = week_list[datetime.date(int(year), int(month), int(day)).weekday()]
        date = f'{year}年{month}月{day}日  {week}'
        print(date)

        # 你活了多久
        birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")
        curr_datetime = datetime.datetime.now()
        # minus_datetime = curr_datetime - birthday_date
        minus_datetime = birthday_date - curr_datetime
        # 发送消息
        sendMessage_url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={access_token}"
        for user in touser:
            data = {
                "touser": user,
                "template_id": template_id,
                "appid": appid,
                "data": {
                    "demo": {
                        "value": "每日吃饭提醒",
                        "color": "#FF7F50"
                    },
                    "live": {
                        "value": minus_datetime.days,
                        "color": "#FF7F50"
                    },
                    # "date2": {
                    #     "value": date2,
                    #     "color": "#6B6A66"
                    # },
                    "date": {
                        "value": date,
                        "color": "#000000"
                    },
                    "city": {
                        "value": "济南市",
                        "color": "#000000"
                    },
                    "weather": {
                        "value": res['type'],
                        "color": "#000000"
                    },
                    "tempn": {
                        "value": res['low'],
                        "color": "#000000"
                    },
                    "temp": {
                        "value": res['high'],
                        "color": "#000000"
                    },
                    # "wd": {
                    #     "value": info,
                    #     "color": "#FF7F50"
                    # },
                    'english': {
                        "value": e,
                        "color": "#FF6347"
                    }

                }
            }

            getTemp = requests.post(sendMessage_url, data=json.dumps(data)).json()
            print(getTemp)
    else:
        print("appid或secret错误")

if __name__ == "__main__":
    even = ''
    s = ''
    main(even,s)
