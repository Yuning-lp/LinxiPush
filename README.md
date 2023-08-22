# ymscript

## 仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断。

> ### 微信测试号
[![pPJ5bnA.png](https://s1.ax1x.com/2023/08/23/pPJ5bnA.png)](https://imgse.com/i/pPJ5bnA)
> #### 使用示例:
> ```python
> # 微信推送(先关注再使用)
> def WxSend(project, status, content,turl):
>     url = "https://linxi-send.run.goorm.app/"
>     data = {
>         "name": "林夕", # 微信昵称
>         "project": project, #项目名称
>         "status": status, # 项目状态
>         "content": content, # 详细内容
>         "url":turl # 点击访问链接
>     }
>     result = requests.post(url, json=data).json()
>     print(f"微信消息推送: {result['msg']}")
## 您必须在下载后的24小时内从计算机或手机中完全删除以上内容
