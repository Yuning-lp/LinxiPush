# Author: lindaye
# update: 2023-08-23 6:40
# 充值购买阅读(钢镚阅读)
# 1.新增手动验证文章(关注微信测试号[https://s1.ax1x.com/2023/08/23/pPJ5bnA.png] 替换Wxsend函数中微信昵称)
# 入口: http://2496831.y1bn.0749apd1a845l.cloud/?p=2496831
# V1.1

import re
import time
import hashlib
import random
import requests
import base64

# 抓包获取Cookie完全填入cookie替换###
cookie = "###"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
    "Cookie": cookie,
}


def get_sign():
    current_time = str(int(time.time()))
    # 计算 sign
    sign_str = f"key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={current_time}"
    sha256_hash = hashlib.sha256(sign_str.encode())
    sign = sha256_hash.hexdigest()
    data = f'time={current_time}&sign={sign}'
    return data

def home():
    url = "http://2477726.neavbkz.jweiyshi.r0ffky3twj.cloud/share"
    response = requests.get(url, headers=headers, data=get_sign()).json()
    share_link = response["data"]["share_link"][0]
    p_value = share_link.split("=")[1].split("&")[0]
    url = "http://2477726.neavbkz.jweiyshi.r0ffky3twj.cloud/read/info"
    response = requests.get(url, headers=headers, data=get_sign()).json()
    if response["code"] == 0:
        remain = response["data"]["remain"]
        read = response["data"]["read"]
        print(f"ID:{p_value}   钢镚余额:{remain}\n今日阅读量:{read} 篇\n推广链接:{share_link}")
    else:
        print(response["message"])


def read():
    for i in range(30):
        url = "http://2477726.9o.10r8cvn6b1.cloud/read/task"
        response = requests.get(url, headers=headers, data=get_sign()).json()
        if response["code"] == 1:
            if "秒" in response['message']:
                s = re.findall('请(.*?)秒',response['message'])[0]
                time.sleep(int(s))
            else:
                print(response["message"])
                break
        else:
            try:
                s = random.randint(10,15)
                # 检测是否是检测文章
                biz = re.findall("biz=(.*?)&",response["data"]["link"])
                biz = base64.b64decode(biz[0]).decode('utf-8')
                print(f"获取文章成功---{biz}---阅读时间{s}")
                if biz in ['3923296810','3933296470','3895583124','3877697845','3599816852','3889696883','3258705834']:
                    print(f"获取到检测文章,已推送到微信 30s")
                    WxSend("微信阅读-钢镚阅读", "检测文章", "请在30秒内完成当前文章",response['data']['link'])
                    time.sleep(30)
                    response = requests.post("http://2477726.9o.10r8cvn6b1.cloud/read/finish", headers=headers, data=get_sign()).json()
                    if response["code"] == 0:
                        print(f"(检测中)阅读文章成功---获得钢镚[{gain}]")
                    else:
                        print(response)
                    url = "http://2477726.9o.10r8cvn6b1.cloud/read/task"
                    response = requests.get(url, headers=headers, data=get_sign()).json()
                    if 'link' in response:
                        print(f"获取文章成功---{biz}---阅读时间{s}")
                        time.sleep(s)
                        response = requests.post("http://2477726.9o.10r8cvn6b1.cloud/read/finish", headers=headers, data=get_sign()).json()
                        if response['code'] == 0:
                            if response['data']['check'] is False:
                                gain = response['data']['gain']
                                print(f"(验证成功)阅读文章成功---获得钢镚[{gain}]")
                        else:
                            print(f"验证失败: {response}")
                            break
                    else:
                        print(response)
                        break

                else:
                    time.sleep(s)
                    url = "http://2477726.9o.10r8cvn6b1.cloud/read/finish"
                    response = requests.post(url, headers=headers, data=get_sign()).json()
                    # print(response)
                    if response["code"] == 0:
                        if response["data"]["check"] is False:
                            gain = response["data"]["gain"]
                            print(f"阅读文章成功---获得钢镚[{gain}]")
                        else:
                            print(f"获取到未收录检测: {biz} 将自动停止脚本")
                            break
                    else:
                        if response['message'] == "记录无效":
                            print("记录无效,重新阅读")
                        else:
                            print(response)
                            break

            except KeyError:
                if response['code'] == 801:
                    print(f"今日任务已完成: {response['message']}")
                    break
                else:
                    print(f"获取文章失败,错误未知{response}")
                    break



def get_money():
    print("============开始微信提现============")
    url = "http://2477726.84.8agakd6cqn.cloud/withdraw/wechat"
    response = requests.get(url, headers=headers, data=get_sign()).json()
    if response["code"] == 0:
        print(response["message"])
    elif response["code"] == 1:
        print(response["message"])
    else:
        print(f"错误未知{response}")



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


home()
read()
get_money()
