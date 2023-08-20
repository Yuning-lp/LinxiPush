# Author: lindaye
# update: 2023-08-20 18:31
# 1.修复提现
# 2.新增多账户
# 小小阅读
# 入口: https://fia.douyifang.top:10263/yunonline/v1/auth/1c3da9bd1689d78a51463138d634512f?codeurl=fia.douyifang.top:10263&codeuserid=2&time=1692525245

import requests
import re
import time
import random

# 仅填写uid_list内容即可(抓包获取Cookie中的ysm_uid的值填入##)
# 单账号 uid_list = ['##']
# 多账号 uid_list = ['##','##']
uid_list = ['##','##']

ysm_uid = ''

headers = {
    'Cookie': '',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue'
}


def ts ():
    return str (int (time .time ()))+'000'


def signin():
    url = 'http://1692416143.3z2rpa.top/'
    result = requests.get(url,headers=headers).text
    signid = re.findall(r'id\'\) \|\| "(.*?)";',result)
    if signid == []:
        print ('初始化失败,账号异常')
    else:
        print ('初始化成功,账号登陆成功!')
        return signid


def get_money(signid):
    url = f'http://1692429080.3z2rpa.top/yunonline/v1/exchange?unionid={ysm_uid}&request_id={signid}&qrcode_number=&addtime='
    result = requests.get(url,headers=headers).text
    money = re.findall(r'id="exchange_gold">(.*?)</p>',result)
    if money == []:
        print ('金币获取失败,账号异常')
    else:
        if int(money[0]) >= 3000:
            money = (int(money[0]) // 3000) * 3000
            print(f"提交体现金币: {money}")
            t_url = 'http://1692429080.3z2rpa.top/yunonline/v1/user_gold'
            t_data = {'unionid':ysm_uid,'request_id':signid,'gold':money}
            t_result = requests.post(t_url,headers=headers,json=t_data).json()
            if t_result['errcode'] == 0:
                print(f"金币转金额成功: {t_result['data']['money']}")
            else:
                print(f"金币转金额失败: {t_result['msg']}")
            j_url = 'http://1692422733.3z2rpa.top/yunonline/v1/withdraw'
            j_data = {'unionid':ysm_uid,'signid':signid,'ua':0,'ptype':0,'paccount':'','pname':''}
            j_result = requests.post(j_url,headers=headers,data=j_data).json()
            print(f"体现结果: {j_result}")
        else:
            print(f'还未到达提现最低金币 当前金币: {money[0]}')



def user_info():
    url = f'http://1692416143.3z2rpa.top/yunonline/v1/sign_info?time={ts()}000&unionid={ysm_uid}'
    result = requests.get(url,headers=headers).json()
    if result['errcode'] == 0:
        pass
    else:
        print ('获取用户信息失败，账号异常')

def hasWechat():
    url = f'http://1692416143.3z2rpa.top/yunonline/v1/hasWechat?unionid={ysm_uid}'
    result = requests.get(url,headers=headers).json()
    if result['errcode'] == 0:
        pass
    else:
        print ('获取用户信息失败，账号异常')

def gold():
    url = f'http://1692416143.3z2rpa.top/yunonline/v1/gold?unionid={ysm_uid}&time={ts()}000'
    result = requests.get(url,headers=headers).json()
    if result['errcode'] == 0:
        print(f"今日积分: {result['data']['day_gold']} 已阅读: {result['data']['day_read']}篇 剩余: {result['data']['remain_read']}篇")
    else:
        print ('获取用户信息失败，账号异常')


def get_Key():
    url = 'http://1692416143.3z2rpa.top/yunonline/v1/wtmpdomain'
    data = {'unionid':ysm_uid}
    result = requests.post(url,headers=headers,json=data).json()
    uk = re.findall(r'uk=([^&]+)',result['data']['domain'])
    print(f"获取到KEY: {uk[0]}")
    do_read(uk[0])

def do_read(uk):
    while True:
        url = f'https://nsr.zsf2023e458.cloud/yunonline/v1/do_read?uk={uk}'
        result = requests.get(url,headers=headers).json()
        if result['errcode'] == 0:
            link = result['data']['link']
            l_result = requests.get(link,headers=headers,allow_redirects=False).status_code
            s = random.randint(7,15)
            print (f'本次模拟读{s}秒')#line:141
            time.sleep(s)
            rurl = f'https://nsr.zsf2023e458.cloud/yunonline/v1/get_read_gold?uk={uk}&time={s}&timestamp={ts()}'
            r_result = requests.get(rurl,headers=headers).json()
            if r_result['errcode'] == 0:
                print(f"阅读已完成: 获得{r_result['data']['gold']}积分")
            else:
                print(f"阅读失败: {r_result}")
        else:
            print (f"阅读提醒: {result['msg']}")
            break
   

print(f"=================获取到{len(uid_list)}个账号==================")
for id in range(len(uid_list)):
    print(f"当前为第{id+1}个账号")
    ysm_uid = uid_list[id]
    headers['Cookie'] = f'ysm_uid={ysm_uid}'
    signid = signin()
    user_info()
    hasWechat()
    gold()
    get_Key()
    gold()
    get_money(signid)
