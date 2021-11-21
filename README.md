# 美团限时红包,神券自动获取 
![visitors](https://visitor-badge.glitch.me/badge?page_id=MeituanRedenvelope)

## 1. 本项目优点
- 部署简单,支持本地，青龙，腾讯云函数等部署方式
- 简化参数设置
- 优化代码
- 自动遍历全国主要城市的红包池
  
## 2. TODO

- [ ]  多账户支持，看是否有需要

# 使用方法

## 3. token的获取和设置
### 3.1 获取token
登录后在美团首页F12检查，点击network，刷新网页，拖进度条点击第一个请求，然后复制请求头中cookie 的token字段，注意只要token字段，格式为"token={token};"中的 **{token}** 字段，不带分号，更不是整个cookie。

比如原本Cookies中的token字段为 token="1234";只需要1234就行,字符串格式。

**注意** 用账号密码登陆！！！短线验证码登陆的ck 时效短，很快就过期了

### 3.2 设置token
方法一:可直接修改脚本中的`token`字段
方法二:设置环境变量 `meituantoken`

## 4. 开启tg推送
因为tg确实方便好用,又没限制，就只写了tg的推送。
建议脚本部署在国内网络环境中,我默认脚本中内置我自己的一个tg推送的 API反代，方便大家使用。

### 4.1 启用tg推送
修改`USE_TG`为 `USE_TG = True`.

然后就是 `TG_BOT_TOKEN`为你的bot的token.
`TG_USER_ID`是你的用户id，如果不会获取的可以点击这个[机器人](https://t.me/myidbot?start=botostore)获取.

## 启动设置

定时设置建议为`0 11,14,15,16,17,21,0,1,2,3 * * *`

# Thanks 
[Vonalien](https://github.com/Vonalien/meituan-shenquan)，[Vonalier](https://github.com/Vonalier/meituan-shenquan) 等脚本
