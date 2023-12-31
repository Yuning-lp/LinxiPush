# Author: lindaye
# update: 2023-08-23 8:46
# http://mr1692750884645.aidhtjj.cn/coin/index.html?mid=CR42F6WUF 【元宝阅读】看文章赚零花钱，全新玩法，提现秒到(若链接打不开，可复制到手机浏览器里打开)
# http://mr1692750916083.dsxanvq.cn/ox/index.html?mid=RG7UUSYFS 【星空阅读】看文章赚零花钱，全新玩法，提现秒到(若链接打不开，可复制到手机浏览器里打开)
# http://mr1692750963995.stijhqm.cn/user/index.html?mid=D33C7W3A3 【花花阅读】看文章赚零花钱，全新玩法，提现秒到(若链接打不开，可复制到手机浏览器里打开)
# 使用方法: 打开上面三个链接抓包获取un token值填入18 行 data
# 关注微信测试号(不关注无法推送检测文章): https://s1.ax1x.com/2023/08/23/pPJ5bnA.png
# 替换WxSend函数中的微信昵称


import requests
import re
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3461 Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5223 MMWEBSDK/20230701 MMWEBID/7925 MicroMessenger/8.0.40.2420(0x28002851) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
    'Cookie':'',
}

data = {"un":"##","token":"##","pageSize":20}


# 微信推送
def WxSend(project, status, content,turl):
    url = "https://linxi-send.run.goorm.app/"
    data = {
        "name": "林夕", # 微信昵称
        "project": project,
        "status": status,
        "content": content,
        "url":turl
    }
    result = requests.post(url, json=data).json()
    print(f"微信消息推送: {result['msg']}")


def user():
    url = domain +'/info'
    result = requests.post(url,headers=headers,json=data).json()['result']
    print(f"{ydname}账号: {result['uid']} 今日已读: {result['dayCount']} 今日积分:{result['moneyCurrent']}")
    options = [0.3, 0.5, 1, 5]  # 可选的数字列表
    max_money = max(filter(lambda x: x < (int(result['moneyCurrent'])/10000), options), default=0.3)
    return max_money

def read():
    while True:
        url = domain +'/read'
        result = requests.post(url,headers=headers,json=data).json()
        if result['code'] == 0:
            if result["result"]["status"] == 10:
                biz=''.join(re.findall('__biz=(.+)&mid',result["result"]["url"]))
                if biz in ['Mzg2Mzk3Mjk5NQ==']:
                    print("检测文章: 请在30秒内完成当前文章")
                    WxSend(f"微信阅读-{ydname}", "检测文章", "请在30秒内完成当前文章",result["result"]["url"])
                    time.sleep(30)
                    url = domain +'/submit'
                    result = requests.post(url,headers=headers,json=data).json()
                    print(result)
                else:
                    print(f"开始阅读文章-{biz}-阅读时间 6s")
                    time.sleep(6)
                    url = domain +'/submit'
                    result = requests.post(url,headers=headers,json=data).json()["result"]
                    print(f"阅读成功: 积分{result['val']} 剩余{result['progress']}篇")  
            else:
                tips = {30:'重新运行尝试一下',40:'文章还没有准备好',50:'阅读失效,黑号了',60:'已经全部阅读完了',70:'下一轮还未开启',}
                print(f'{ydname}账号提醒: {tips[result["result"]["status"]]}!')
                if result["result"]["status"] ==30:
                    time.sleep(1)
                    continue
                else:
                    break
        else:
            if result['msg'] == "请求频繁":
                time.sleep(1)
                continue
            else:
                print(f"异常: {result}")
                break

def get_money(max_money):
    print(f"================{ydname}提现==================")
    if ydname == "花花":
        t = "/wd"
    else:
        t = "/wdmoney"
    T_data = {"val":max_money,"un":data['un'],"token":data['token'],"pageSize":20}
    response = requests.post(domain+t, headers=headers, json=T_data).json()
    print(response)

for i in ['/user','/coin','/ox']:
    domain = 'http://u.cocozx.cn/api'+i # 花花 /user 元宝阅读 /coin 星空阅读 /ox
    ydlist = {'/user':'花花','/coin':'元宝','/ox':'星空'}
    ydname = ydlist[i]
    print(f"================{ydname}阅读==================")
    max_money = user()  # 提现金额
    read()
    max_money = user()  # 提现金额
    get_money(max_money)
    time.sleep(1)
