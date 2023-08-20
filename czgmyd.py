# Author: lindaye
# update: 2023-08-20 18:31
# 充值购买阅读(钢镚阅读)
# 入口: http://2496831.y1bn.0749apd1a845l.cloud/?p=2496831

import re
import time
import hashlib
import random
import requests

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
    return current_time,sign

# 检查 xwytoken 是否存在
if cookie is None:
    print("你没有填入ydtoken，咋运行？")
else:
    # 输出当前正在执行的账号
    print(f"\n=======开始执行账号=======")
    current_time,sign = get_sign()
    url = "http://2477726.neavbkz.jweiyshi.r0ffky3twj.cloud/share"
    data = {"time": current_time, "sign": sign}
    response = requests.get(url, headers=headers, json=data).json()
    share_link = response["data"]["share_link"][0]
    p_value = share_link.split("=")[1].split("&")[0]

    url = "http://2477726.neavbkz.jweiyshi.r0ffky3twj.cloud/read/info"
    response = requests.get(url, headers=headers, json=data).json()
    if response["code"] == 0:
        remain = response["data"]["remain"]
        read = response["data"]["read"]
        print(f"ID:{p_value}-----钢镚余额:{remain}\n今日阅读量::{read}\n推广链接:{share_link}")
    else:
        print(response["message"])

    print("============开始执行阅读文章============")
    for i in range(30):
        # 计算 sign
        current_time,sign = get_sign()
        data = {"time": current_time, "sign": sign}
        url = "http://2477726.9o.10r8cvn6b1.cloud/read/task"
        response = requests.get(url, headers=headers, json=data).json()
        if response["code"] == 1:
            print(response["message"])
            break
        else:
            try:
                mid = response["data"]["link"].split("&mid=")[1].split("&")[0]
                s = random.randint(10,15)
                print(f"获取文章成功---{mid}---阅读时间{s}")
                time.sleep(s)
                url = "http://2477726.9o.10r8cvn6b1.cloud/read/finish"
                response = requests.post(url, headers=headers, data=data).json()
                if response["code"] == 0:
                    if response["data"]["check"] is False:
                        gain = response["data"]["gain"]
                        print(f"阅读文章成功---获得钢镚[{gain}]")
                    else:
                        # response = requests.post(url, headers=headers, data=data).json()
                        print("check=True,请手动阅读过检测")
                        print(response)
                        break
                else:
                    print(f"{response['message']}")
                    break

            except KeyError:
                print(f"获取文章失败,错误未知{response}")
    print(f"============开始微信提现============")
    url = "http://2477726.84.8agakd6cqn.cloud/withdraw/wechat"

    response = requests.get(url, headers=headers, json=data).json()
    if response["code"] == 0:
        print(response["message"])
    elif response["code"] == 1:
        print(response["message"])
    else:
        print(f"错误未知{response}")
