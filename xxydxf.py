# Author: lindaye
# update: 2023-08-24 13:32
# 1.修复提现
# 2.新增多账户
# 3.新增100篇推送信息
# 4.优化代码
# 小小阅读
# 微信测试号: https://s1.ax1x.com/2023/08/23/pPJ5bnA.png
# 入口: https://fia.douyifang.top:10263/yunonline/v1/auth/1c3da9bd1689d78a51463138d634512f?codeurl=fia.douyifang.top:10263&codeuserid=2&time=1692525245
# 使用教程: 1.填入uid_list值(仅需ysm_uid=后的内容) 2.扫码关注微信测试号 3.填写微信昵称
# V1.4(测试版)

import requests
import re
import time
import random

# 保持连接,重复利用
ss = requests.session()
# 推送域名
tsurl = 'https://linxi-send.run.goorm.app'
# 临时用户名
temp_user = ""
# 微信昵称
wxname = 'XX'
# 仅填写uid_list内容即可(抓包获取Cookie中的ysm_uid的值填入##)
# 单账号 uid_list = ['##']
# 多账号 uid_list = ['##','##']
uid_list = ['##','##']

ysm_uid = ''

# 检测文章列表
check_list = [
    "MzkxNTE3MzQ4MQ==",
    "Mzg5MjM0MDEwNw==",
    "MzUzODY4NzE2OQ==",
    "MzkyMjE3MzYxMg==",
    "MzkxNjMwNDIzOA==",
    "Mzg3NzUxMjc5Mg==",
    "Mzg4NTcwODE1NA==",
    "Mzk0ODIxODE4OQ==",
    "Mzg2NjUyMjI1NA==",
    "MzIzMDczODg4Mw==",
    "Mzg5ODUyMzYzMQ==",
    "MzU0NzI5Mjc4OQ==",
]

headers = {
    'Cookie': '',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue'
}


def ts ():
    return str (int (time .time ()))+'000'


def signin():
    result = ss.get('http://1692416143.3z2rpa.top/',headers=headers).text
    signid = re.findall(r'id\'\) \|\| "(.*?)";',result)
    if signid == []:
        print ('初始化失败,账号异常')
    else:
        print ('初始化成功,账号登陆成功!')
        return signid


def get_money(signid):
    result = ss.get(f'http://1692429080.3z2rpa.top/yunonline/v1/exchange?unionid={ysm_uid}&request_id={signid}&qrcode_number=&addtime=').text
    money = re.findall(r'id="exchange_gold">(.*?)</p>',result)
    if money == []:
        print ('金币获取失败,账号异常')
    else:
        if int(money[0]) >= 3000:
            money = (int(money[0]) // 3000) * 3000
            print(f"提交体现金币: {money}")
            t_data = {'unionid':ysm_uid,'request_id':signid,'gold':money}
            t_result = ss.post('http://1692429080.3z2rpa.top/yunonline/v1/user_gold',json=t_data).json()
            if t_result['errcode'] == 0:
                print(f"金币转金额成功: {t_result['data']['money']}")
            else:
                print(f"金币转金额失败: {t_result['msg']}")
            j_data = {'unionid':ysm_uid,'signid':signid,'ua':0,'ptype':0,'paccount':'','pname':''}
            j_result = ss.post('http://1692422733.3z2rpa.top/yunonline/v1/withdraw',data=j_data).json()
            print(f"体现结果: {j_result['msg']}")
        else:
            print(f'还未到达提现最低金币 当前金币: {money[0]}')



def user_info():
    result = ss.get(f'http://1692416143.3z2rpa.top/yunonline/v1/sign_info?time={ts()}000&unionid={ysm_uid}').json()
    if result['errcode'] == 0:
        pass
    else:
        print ('获取用户信息失败，账号异常')

def hasWechat():
    result = ss.get(f'http://1692416143.3z2rpa.top/yunonline/v1/hasWechat?unionid={ysm_uid}').json()
    if result['errcode'] == 0:
        pass
    else:
        print ('获取用户信息失败，账号异常')

def gold():
    result = ss.get(f'http://1692416143.3z2rpa.top/yunonline/v1/gold?unionid={ysm_uid}&time={ts()}000').json()
    if result['errcode'] == 0:
        print(f"今日积分: {result['data']['day_gold']} 已阅读: {result['data']['day_read']}篇 剩余: {result['data']['remain_read']}篇")
    else:
        print ('获取用户信息失败，账号异常')


def get_Key():
    data = {'unionid':ysm_uid}
    result = ss.post('http://1692416143.3z2rpa.top/yunonline/v1/wtmpdomain',json=data).json()
    uk = re.findall(r'uk=([^&]+)',result['data']['domain'])
    print(f"获取到KEY: {uk[0]}")
    do_read(uk[0])

def do_read(uk):
    while True:
        result = ss.get(f'https://nsr.zsf2023e458.cloud/yunonline/v1/do_read?uk={uk}').json()
        if result['errcode'] == 0:
            link = result['data']['link']
            l_result = ss.get(link,headers=headers).text
            biz = re.findall("biz=(.*?)&mid",l_result)[0]
            s = random.randint(6,8)
            print (f'获取文章成功,本次模拟读{s}秒')
            if biz in check_list:
                print("阅读文章检测--100篇检测---已推送至微信")
                link = re.findall('msg_link = "(.*?)";',l_result)[0]
                # 过检测
                check = test(link)
                if check == True:
                    print("检测文章-过检测成功啦!")
                    r_result = ss.get(f'https://nsr.zsf2023e458.cloud/yunonline/v1/get_read_gold?uk={uk}&time={s}&timestamp={ts()}').json()
                    if r_result['errcode'] == 0:
                        print(f"阅读已完成: 获得{r_result['data']['gold']}积分")
                    else:
                        print(f"阅读失败,获取到未收录检测BIZ:{biz}")
                        print(r_result)
                        break
                else:
                    print("检测文章-过检测失败啦!")
                    break
            else:
                time.sleep(s)
                r_result = ss.get(f'https://nsr.zsf2023e458.cloud/yunonline/v1/get_read_gold?uk={uk}&time={s}&timestamp={ts()}').json()
                if r_result['errcode'] == 0:
                    print(f"阅读已完成: 获得{r_result['data']['gold']}积分")
                else:
                    print(r_result)
                    break
        else:
            if result['msg'] == "任务重复":
                print("阅读失败: 阅读重复重新获取文章")
            else:
                print (f"阅读提醒: {result['msg']}")
                break


def test(link):
    result = ss.post(tsurl+"/task",json={"biz":temp_user,"url":link}).json()
    WxSend("微信阅读-小阅阅读", "检测文章", "请在30秒内完成当前文章",tsurl+"/read/"+temp_user)
    check = ''
    for i in range(30):
        result = ss.get(tsurl+"/back/"+temp_user).json()
        if result['status'] == True:
            check = True 
            break
        else:
            print("等待检测中...", end="\r", flush=True)
        time.sleep(1)
    if result['status'] == False:
        print("手动检测超时,验证失败!")
        check = False 
    return check


# 微信推送
def WxSend(project, status, content,turl):
    data = {
        "name": wxname, # 微信昵称
        "project": project,
        "status": status,
        "content": content,
        "url":turl
    }
    result = ss.post(tsurl, json=data).json()
    print(f"微信消息推送: {result['msg']}")
    if result['msg'] == "林夕推送助手: 微信API每日调用已上限!":
        print(f"请手动完成验证吧: {turl}")


print(f"=================获取到{len(uid_list)}个账号==================")
for id in range(len(uid_list)):
    print(f"当前为第{id+1}个账号")
    ysm_uid = uid_list[id]
    temp_user = ysm_uid
    headers['Cookie'] = f'ysm_uid={ysm_uid}'
    signid = signin()
    user_info()
    hasWechat()
    gold()
    get_Key()
    gold()
    get_money(signid)
