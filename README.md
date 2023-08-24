# ymscript
## 注意: 当前微信推送调用次数被冲爆了,暂时无法使用(9:44)
## 仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断。

> ### 微信测试号
[![pPJ5bnA.png](https://s1.ax1x.com/2023/08/23/pPJ5bnA.png)](https://imgse.com/i/pPJ5bnA)
> #### 推送使用示例:
> ```python
> # 微信推送(先关注再使用)
> def WxSend(project, status, content,turl):
>     url = "https://linxi-send.run.goorm.app/"
>     data = {
>         "name": "XX", # 微信昵称
>         "project": project, #项目名称
>         "status": status, # 项目状态
>         "content": content, # 详细内容
>         "url":turl # 点击访问链接
>     }
>     result = requests.post(url, json=data).json()
>     print(f"微信消息推送: {result['msg']}")
> ```
> #### 阅读文章验证使用示例
> ```python
> import requests
> import time
> 
> tsurl = 'https://linxi-send.run.goorm.app'
> 
> def test():
>     result = requests.post(tsurl+"/task",json={"biz":"test","url":"http://baidu.com"}).json()
>     WxSend("测试回调", "状态", "内容",tsurl+"/read/"+"test")
>     for i in range(30):
>         result = requests.get(tsurl+"/back/"+"test").json()
>         if result['status'] == True:
>             print("过检测成功!")
>             break
>         else:
>             print("等待检测中...", end="\r", flush=True)
>         time.sleep(1)
>     if result['status'] == False:
>         print("过检测失败!")
> 
> 
> # 微信推送
> def WxSend(project, status, content,turl):
>     data = {
>         "name": "林夕", # 微信昵称
>         "project": project,
>         "status": status,
>         "content": content,
>         "url":turl
>     }
>     result = requests.post(tsurl, json=data).json()
>     print(f"微信消息推送: {result['msg']}")
> 
> if __name__ == "__main__":
>    test()
## 您必须在下载后的24小时内从计算机或手机中完全删除以上内容
