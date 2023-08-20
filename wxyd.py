import requests
#加密
from Crypto.Cipher import AES
import base64
# 随机值
import random
# 正则匹配
import re
# 时间
import time

# 入口: https://entry-1318684421.cos.ap-nanjing.myqcloud.com/cos_b.html?openId=oiDdr5xiVUIwNQVvj1sADz2rb5Mg
authtoken = '###'

headers = {
    'Cookie': f'authtoken={authtoken}; snapshot=0',
    'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 MicroMessenger/5.2.380'
}

def aes_encrypt(data):
    block_size = AES.block_size  # 获取AES块大小
    padding = lambda s: s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size)  # 填充函数，使得数据长度为块大小的整数倍
    key = b'5e4332761103722eb20bb1ad53907c6e'  # 密钥，需要根据实际情况修改
    cipher = AES.new(key, AES.MODE_ECB)  # 使用ECB模式创建AES对象
    encrypted_data = cipher.encrypt(padding(data).encode())  # 对数据进行加密
    encrypted_data_base64 = base64.b64encode(encrypted_data).decode()  # 对加密后的数据进行base64编码
    return encrypted_data_base64

def get_readhome():
    url = 'https://sss.mvvv.fun/app/enter/read_home'
    result = requests.get(url,headers=headers).json()
    if result['code'] == 0:
        url = "http://" + re.findall('//(.*?)/',result['data']['location'])[0]
        get_read(url)
    else:
        print("获取阅读域名失败!")
        get_read("http://5x034gb8z4.qqaas.fun")


def get_read(url):
    result = requests.get(url+"/app/user/myPickInfo",headers=headers).json()['data']
    # print(result)
    data = aes_encrypt(f'{{"moneyPick":{result["goldNow"]}}}')
    result = requests.post(url+"/app/user/pickAuto",headers=headers,json=data).json()
    print(f"兑换结果: {result['msg']}")
    result = requests.get(url+"/app/user/myInfo",headers=headers).json()['data']
    print(f"用户: {result['nameNick']} 今日已读: {result['completeTodayCount']}篇  获得积分: {result['completeTodayGold']}")
    if result['remainSec'] == 0:
        print ('当前是读文章的状态')#line:93
        get_myinfo(url)
    else :#line:94
        ttime =int (result['remainSec'] /60 )#line:95
        print ('当前不是是读文章的状态,距离下次阅读还有',ttime ,'分钟')#line:96
    
    
def get_myinfo(url):
    result = requests.get(url+"/app/read/get",headers=headers).json()['data']['location']
    u = re.findall(r'u=([^&]+)',result)[0]
    print(f"获取到KEY: {u}")
    result = requests.get(f'https://sss.mvvv.fun/app/task/doRead?u={u}&type=1',headers=headers).json()['data']
    if (result['bizCode']) !=0 or (result['taskKey'] == None):
        print('文章正在更新中。请稍后重试。')
    else:
        print(f"阅读任务ID: {result['taskKey']}")
        s = random.randint (10 ,15 )
        print(f"随机阅读 {s} 秒")
        time.sleep(s)
        do_read(u,result['taskKey'])


def do_read(u,taskKey):
    for i in range(30):
        url = f'https://sss.mvvv.fun/app/task/doRead?u={u}&type=1&key={taskKey}'
        result = requests.get(url,headers=headers).json()['data']
        if result['bizCode'] == 0:
            print(f"阅读结果: {result['detail']}")
            if result['detail'] == "检测中":
                print("遇到检测文章,重新阅读")
                result = requests.get(url,headers=headers).json()['data']
            taskKey = result['taskKey']
            print(f"阅读任务ID: {taskKey}")
            s = random.randint (20 ,30 )
            print(f"随机阅读 {s} 秒")
            time.sleep(s)
        else:
            print(f"任务刷爆了: {result['detail']}")
            break


get_readhome()
