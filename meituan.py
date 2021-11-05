#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: n0thing2speak

import urllib.request
import ssl
import json
import os
import datetime
import random
import requests

# 使用脚本需要修改的部分 ⬇️
token = ""

TG_BOT_TOKEN = '' # 通过 @BotFather 申请获得，示例：1077xxx4424:AAFjv0FcqxxxxxxgEMGfi22B4yh15R5uw
TG_USER_ID = ''  # 用户、群组或频道 ID，示例：129xxx206
TG_API_HOST = 'tgpusher.shybee.cf'  # 这是我自建的推送api反代，国内可以访问
# TG_API_HOST = 'api.telegram.org'  # 这是官方的推送API地址
USE_TG = False
# ⬆️

# 关闭ssl校验，用于抓包调试请求
ssl._create_default_https_context = ssl._create_unverified_context

CITY_DICT = {
    "沈阳": [123429092, 41796768],
    "长春": [125324501, 43886841],
    "哈尔滨": [126642464, 45756966],
    "北京": [116405289, 39904987],
    "天津": [117190186, 39125595],
    "呼和浩特": [111751990, 40841490],
    "银川": [106232480, 38486440],
    "太原": [112549248, 37857014],
    "石家庄": [114502464, 38045475],
    "济南": [117000923, 36675808],
    "郑州": [113665413, 34757977],
    "西安": [108948021, 34263161],
    "武汉": [114298569, 30584354],
    "南京": [11876741, 32041546],
    "合肥": [117283043, 31861191],
    "上海": [121472641, 31231707],
    "长沙": [112982277, 2819409],
    "南昌": [115892151, 28676493],
    "杭州": [12015358, 30287458],
    "福州": [119306236, 26075302],
    "广州": [11328064, 23125177],
    "海口": [110199890, 20044220],
    "南宁": [108320007, 2282402],
    "重庆": [106504959, 29533155],
    "成都": [104065827, 30657401],
    "昆明": [10271225, 25040609],
    "贵阳": [106713478, 26578342],
    "兰州": [103834170, 36061380],
    "青岛": [120190000, 36060000]
}

n_time = datetime.datetime.now()
d_time0 = datetime.datetime.strptime(
    str(datetime.datetime.now().date()) + '11:00', '%Y-%m-%d%H:%M')
d_time3 = datetime.datetime.strptime(
    str(datetime.datetime.now().date()) + '17:00', '%Y-%m-%d%H:%M')  # 每天的17点
d_time4 = datetime.datetime.strptime(
    str(datetime.datetime.now().date()) + '20:49', '%Y-%m-%d%H:%M')  # 么天的时间

d_time5 = datetime.datetime.strptime(
    str(datetime.datetime.now().date()) + '21:00', '%Y-%m-%d%H:%M')
d_time6 = datetime.datetime.strptime(
    str(datetime.datetime.now().date()) + '23:59', '%Y-%m-%d%H:%M')
d_time7 = datetime.datetime.strptime(
    str(datetime.datetime.now().date()) + '11:00', '%Y-%m-%d%H:%M')  # 每天的11点


def telegram(desp):
    data = (('chat_id', TG_USER_ID), ('text', '🎉美团神券自动兑换脚本🎉\n\n' + desp))
    response = requests.post('https://' + TG_API_HOST + '/bot' + TG_BOT_TOKEN +
                             '/sendMessage',
                             data=data)
    if response.status_code != 200:
        print('Telegram Bot 推送失败')
    else:
        print('Telegram Bot 推送成功')


# def telegram(desp):
#     data = {'chat_id': TG_USER_ID, 'text': '🎉美团神券自动兑换脚本🎉\n\n' + desp}
#     textmod = json.dumps(data).encode(encoding='utf-8')
#     header_dict = {
#         'Accept': 'application/json',
#         'Content-Type': 'application/json'
#     }
#     url = 'https://' + TG_API_HOST + '/bot' + TG_BOT_TOKEN + '/sendMessage'
#     req = urllib.request.Request(url=url, data=textmod, headers=header_dict)
#     res = urllib.request.urlopen(req)
#     res = res.read()
#     res.decode(encoding='utf-8')


def random_dic(dicts):
    dict_key_ls = list(dicts.keys())
    random.shuffle(dict_key_ls)
    new_dic = {}
    for key in dict_key_ls:
        new_dic[key] = dicts.get(key)
    return new_dic


class MeiTuan:
    desp = ""  # tg推送的文本
    # 定义短期(半年以上)不会变的量
    parActivityId = "Gh1tkq-wvFU2xEP_ZPzHPQ"
    wm_ctype = "mtandroid"
    # 以下portraitId参数含义未知，用于每日浏览天天神卷30s后可领30豆的请求
    portraitId = 498
    # 定义红包豆攒到多少数量才会执行兑换必中符脚本，以免一直兑换减5元的必中符
    setexchangedou = 1800
    propId = 5  # 要兑换的propID，推荐是5
    exchangeCoinNumber = 1800  # propId为5的时候需要的豆子数量
    # 若在您自定义的抢大额红包时间段中，您无法通过10元以上必中符抢到任何红包！！，则请将下面两行数值改大些，如改成10左右的数字
    ten_left = 0
    fifteen_left = 0
    thirty_left = 0
    fifty_left = 0

    # 标记这四类红包数量不为空，用来在有10元以上必中符时循环判断红包池余量抢购大额元红包，若您不需该功能，请自行将下一行的1改为0
    eight = ten = fifteen = thirty = fifty = 1
    propIdforuse = 2
    counttime = 0
    wm_latitude = 0
    wm_longitude = 0
    showPriceNumber = "1"
    header = {
        "Host": "i.waimai.meituan.com",
        "User-Agent": "MeituanGroup/11.9.208",
        "x-requested-with": "XMLHttpRequest",
        "content-type": "application/x-www-form-urlencoded"
    }
    # 定义美团外卖服务器地址
    baseurl = r"https://i.waimai.meituan.com"
    cityname = None

    def __init__(self) -> None:
        tmptoken = os.environ.get("meituantoken")
        if isinstance(tmptoken, str):
            self.token = tmptoken
        elif len(token) != 0:
            self.token = token
        else:
            self.log("没有获取到美团的token，请手动设置\n")

            self.exit_and_push()

    def signForBeans(self):
        """签到，并判断token是否生效
        """
        self.log("**开始执行签到领豆函数:** \n")

        datas = "token=" + self.token
        url_signforbeans = r"/cfeplay/playcenter/batchgrabred/drawPoints/v2"

        result2 = self.request(url_signforbeans, datas)
        if (result2["code"] == 0):
            self.log("👴%s\n" % (result2["msg"]))

        elif (result2["code"] == 1):
            self.log("👴未到领取时间或已经领取完了(每天可领7次,每次间隔需半小时)！\n")

        elif (result2["code"] == 7):
            self.log("token已失效，请重新设置token\n")
            self.exit_and_push()
        else:
            self.log("请求接口失效或网络不佳，请稍后再试!\n")

    def is_has_redpool(self, infos) -> bool:
        for k in infos:
            if "leftStock" in k:
                return True
        return False

    def queryredpool(self):
        # todo 优化
        self.log("**开始执行查询红包池详情脚本:**\n")
        for k, v in random_dic(CITY_DICT).items():
            # 没主要到用了这么多次， 临时解决一下
            if isinstance(self.cityname, str):
                if k != self.cityname:
                    continue
            wm_latitude = v[1]
            wm_longitude = v[0]

            datas = "parActivityId=" + self.parActivityId + "&wm_latitude=" + str(
                wm_latitude) + "&wm_longitude=" + str(
                    wm_longitude) + "&token=" + str(
                        token) + "&wm_ctype=" + self.wm_ctype
            url_myredbeanRecords = r"/cfeplay/playcenter/batchgrabred/corepage"
            result2 = self.request(url_myredbeanRecords, datas)
            if (result2["code"] == 0 and result2["subcode"] == 0
                    and len(result2["data"]["awardInfos"])):
                if not self.is_has_redpool(result2["data"]["awardInfos"]):
                    # 没有红包池，continue
                    self.log("目前{}没有红包池\n".format(k))
                    continue
                # 设置经纬度
                self.wm_latitude = wm_latitude
                self.wm_longitude = wm_longitude
                if not isinstance(self.cityname, str):
                    self.cityname = k
                self.log("\n当前领券使用城市为:{},经纬度:({},{})\n\n".format(
                    self.cityname, self.wm_latitude, self.wm_longitude))

                for k in result2["data"]["awardInfos"]:
                    # if "leftStock" not in k:
                    #     print("该地区没有红包池，脚本异常退出！")

                    # if (round(float(k["showPriceNumberYuan"]))==8 and k["leftStock"]==eight_left):
                    #     eight = 0
                    if (round(float(k["showPriceNumberYuan"])) == 10
                            and k["leftStock"] == self.ten_left):
                        self.ten = 0
                    if (round(float(k["showPriceNumberYuan"])) == 15
                            and k["leftStock"] == self.fifteen_left):
                        self.fifteen = 0
                    if (round(float(k["showPriceNumberYuan"])) == 30
                            and k["leftStock"] == self.thirty_left):
                        self.thirty = 0
                    if (round(float(k["showPriceNumberYuan"])) == 50
                            and k["leftStock"] == self.fifty_left):
                        self.fifty = 0
                    # if self.counttime < 3:
                    self.log("*红包池中%s元总量:%d张,已被领取:%d张,剩余%d张*\n" %
                             (k["showPriceNumberYuan"], k["totalStock"],
                              k["sendStock"], k["leftStock"]))

                    # self.counttime = self.counttime + 1
                return  # TODO 考虑这里返回是否合适

            elif (result2["code"] == 1 and result2["subcode"] == -1):
                log_text1 = "token失效,导致获取活动信息失败！%s\n" % (result2["msg"])
                self.desp += log_text1
                print(log_text1)
                self.exit_and_push()
            else:
                print("该红包池未开放，等待中!\n")
                continue

    def getbatchId(self):
        """获取batch id
        """
        self.log("**开始执行获取batchId脚本:**\n")
        datas = "parActivityId=" + self.parActivityId + "&wm_ctype=" + self.wm_ctype + "&wm_latitude=" + str(
            self.wm_latitude) + "&wm_longitude=" + str(
                self.wm_longitude) + "&token=" + self.token

        url_getbatchId = r"/cfeplay/playcenter/batchgrabred/corepage"
        result2 = self.request(url_getbatchId, datas)
        if (result2["code"] == 0):
            if "batchId" in result2["data"]:
                self.log("batchId:%s\n" % (result2["data"]["batchId"]))

                self.batchId = result2["data"]["batchId"]  # 这里是获取batchid的部分
            else:
                self.log("获取batchId失败👀，当前非限时抢红包时间段,无法进行下一步，但已为您签到完毕🙏!\n")

                self.exit_and_push()

        elif (result2["code"] == 1):
            # 这里可能是失效
            self.log("%s,接口需提交的token参数已改变👀,请修改后重新运行一遍脚本！\n" % (result2["msg"]))

            self.exit_and_push()

        else:
            self.log("获取batchId错误👀，请检查网络，否则为接口失效！\n")

    def doAction(self):
        """每日签到领必中符
        """
        self.log("**开始执行每日签到领必中符🧧的脚本:**\n")
        datas = "parActivityId=" + self.parActivityId + "&wm_latitude=" + str(
            self.wm_latitude) + "&wm_longitude=" + str(
                self.wm_longitude
            ) + "&token=" + self.token + "&action=SiginInGetProp"
        url_doaction = r"/cfeplay/playcenter/batchgrabred/doAction"
        result2 = self.request(url_doaction, datas)
        if (result2["code"] == 0 and result2["data"]["signDays"] != 0):
            self.log("签到%s\n,截止今日这周已签到%d天\n" %
                     (result2["msg"], result2["data"]["signDays"]))

        elif (result2["code"] == 0 and result2["data"]["signDays"] == 0):
            self.log("您今日已签到，请明天再来!")

        elif (result2["code"] == 7):
            self.log("参数异常或接口已失效\n")
        else:
            self.log("请求接口失效或参数异常，请稍后再试!\n")

    def myRedBeanRecords(self):
        """查询豆子详情的函数
        """
        self.log("**开始执行查询豆子变化详情参数脚本**:\n")
        datas = "parActivityId=" + self.parActivityId + "&wm_latitude=" + str(
            self.wm_latitude) + "&wm_longitude=" + str(
                self.wm_longitude) + "&token=" + str(
                    self.token) + "&userPortraitId=" + str(
                        self.portraitId) + "&pageNum=1"
        url_myredbeanRecords = r"/cfeplay/playcenter/batchgrabred/myRedBeanRecords"
        result2 = self.request(url_myredbeanRecords, datas)
        cent = 1
        if (result2["code"] == 0 and result2["subcode"] == 0
                and len(result2["data"]["redBeanRecordInfos"])):
            # 获取剩余的豆子
            self.leftdou = result2["data"]["totalObtainAmount"] - result2[
                "data"]["usedAmount"] - result2["data"]["expiredAmount"]
            self.log("**总获得红包豆:%d,已使用红包豆:%d,已过期红包豆:%d,剩余可用红包豆:%d**\n" %
                     (result2["data"]["totalObtainAmount"],
                      result2["data"]["usedAmount"],
                      result2["data"]["expiredAmount"], self.leftdou))

            for k in result2["data"]["redBeanRecordInfos"]:

                self.log(
                    "exchangeTime:%s\texchangeMessage:%s\texchangeNumber:%s\n"
                    % (k["exchangeTime"], k["exchangeMessage"],
                       k["exchangeNumber"]))

                cent = cent + 1
                if (cent > 5):
                    break
            self.log("*只显示最近五条红包豆的变化* \n")

    def change(self):
        wm_actual_latitude = str(self.wm_latitude)
        wm_actual_longitude = str(self.wm_longitude)
        while True:
            datas = "wm_actual_longitude=" + wm_actual_longitude + "&wm_actual_latitude=" + wm_actual_latitude + "&exchangeRuleId=&propId=" + str(
                self.propId
            ) + "&exchangeCoinNumber=" + str(
                self.exchangeCoinNumber
            ) + "&parActivityId=" + self.parActivityId + "&wm_ctype=" + self.wm_ctype + "&wm_latitude=" + str(
                self.wm_latitude) + "&wm_longitude=" + str(
                    self.wm_longitude) + "&token=" + self.token
            url_exchange = r"/cfeplay/playcenter/batchgrabred/exchange"
            result2 = self.request(url_exchange, datas)
            if (result2["code"] == 0 and result2["subcode"] == 0):
                self.log("%s,您设置的红包豆兑换指定额度的必中符成功!!!请查看下方道具库详情!😄\n" %
                         (result2["msg"]))
                break
            elif (result2["code"] == 1 and result2["subcode"] == 13):
                self.log("%s\n" % (result2["msg"]))

                break
            elif (result2["code"] == 1 and result2["subcode"] == -1):
                self.log("%s,您现在的红包豆不足以兑换此类必中符或者此类必中符已被抢完!\n正尝试兑换*次一等级*必中符\n" %
                         (result2["msg"]))
                if (self.propId == 5):
                    self.propId = 4
                    break
            elif (result2["code"] == 7):
                self.log("参数异常或接口已失效\n")
            else:
                self.log("请求接口失效或参数异常，请稍后再试!\n")

    def exchange_bean(self):
        """兑换红包
        """
        if self.leftdou > self.setexchangedou:
            self.change()
        else:
            self.log("您当前红包豆为%d未满预设的%d数量，不会执行红包豆兑换必中符脚本，多攒几天豆子再来吧!\n" %
                     (self.leftdou, self.setexchangedou))

    def querymyProps(self):
        """查看必中符号数量
        """
        self.log("**开始执行查询道具库中必中符🧧详情的脚本:**\n")
        datas = "parActivityId=" + self.parActivityId + "&wm_latitude=" + str(
            self.wm_latitude) + "&wm_longitude=" + str(
                self.wm_longitude) + "&token=" + self.token
        url_querymyprops = r"/cfeplay/playcenter/batchgrabred/myProps"
        result2 = self.request(url_querymyprops, datas)
        if (result2["code"] == 0 and len(result2["data"])):
            self.log("👴开始遍历道具库:\n道具库详细信息:\n红包库中共有%d个必中符道具\n" %
                     (len(result2["data"])))

            cent = 0
            count = 0
            for k in result2["data"]:
                if k["status"] == 1:

                    self.log(
                        "第%d个必中符道具有效!!!!\n必中符道具id号:%s\n必中符道具属性:%s\n过期时间:%s\n" %
                        (cent + 1, k["recordNo"], k["propName"],
                         k["expireTime"]))

                    if cent == 0:
                        self.propIdforuse = k["propId"]  # 有几个必中符号
                    print("\n")
                else:
                    count = count + 1
                cent = cent + 1
            if (count != 0):
                self.log("总计%d个必中符道具,已过期%d个😅,有效%d个\n" %
                         (cent, count, cent - count))

            if ((cent - count) != 0):
                self.log("**注意:每天中午抢红包🧧时将自动为您使用道具库中第一个道具!!** ")

            else:
                self.log(" **注意:道具库无有效道具，无法使用必中符,下次抢红包将使用默认参数抢红包(拼手气😅)!!** ")

            print("\n")
        elif (result2["code"] == 7):
            self.log("参数异常或接口已失效\n")

        else:
            self.log("必中符道具库为空，👴未帮您领取过道具!\n")

    def start(self):
        # todo 其他的步骤
        self.signForBeans()
        self.queryredpool()
        self.getbatchId()
        self.doAction()
        self.myRedBeanRecords()
        self.exchange_bean()
        self.querymyProps()

        istimeforbig1 = (n_time <= d_time4) and (n_time >= d_time3)
        istimeforbig2 = (n_time <= d_time6) and (n_time >= d_time4)
        if n_time > d_time7:  # 大于上午11点
            if istimeforbig1:
                if self.propIdforuse == 5:
                    self.log(
                        "**当前符合抢30元以上大额红包的条件**\n**正使用15元必中符为您尝试抢30元以上的红包**\n")

                    while self.fifteen == 1:
                        if not istimeforbig1:
                            self.log(
                                "*👴尽力了，等到红包池要关闭了都未等到15元以上大额红包被抢完，开始保底15元，注意查收！*\n"
                            )

                            break
                        if (self.thirty == 1 and self.fifty == 1):
                            self.log(
                                "*15有剩余，30元已被抢完，50元已被抢完，跳出监测，正在为您抢保底15元红包!*\n")
                            break
            if istimeforbig2:
                if self.propIdforuse == 5:
                    self.log("**当前符合抢30元以上大额红包的条件**\n")
                    self.log("**正使用15元必中符为您尝试抢30元以上的红包**\n")
                    # 拥有15块以上的必中符，先等待着试图抢30,要是15没了，就直接去抢30的红包，或许有可能抢到50
                    while self.fifteen == 1:
                        if not istimeforbig2:
                            self.log(
                                "*👴尽力了，等到红包池要关闭了都未等到15元以上大额红包被抢完，开始保底15元，注意查收！*\n"
                            )
                            break
                        if (self.thirty == 1 and self.fifty == 1):
                            self.log(
                                "*15有剩余，30元已被抢完，50元已被抢完，跳出监测，正在为您抢保底15元红包!*\n")
                            break
                        self.queryredpool()
            if istimeforbig1:
                if self.propIdforuse == 3:
                    self.log("**当前符合抢30元以上大额红包的条件**\n")
                    self.log("**正使用10元必中符为您尝试抢30元以上的红包**\n")
                    # 拥有10块以上的必中符，先等待着试图抢30,要是10和15都没了，就直接去抢30的红包，或许有可能抢到50

                    while self.fifteen == 1:
                        if (self.thirty == 1 and self.fifty == 1):
                            self.log(
                                "&15有剩余，30元已被抢完，50元已被抢完，跳出监测，正在为您抢保底15元红包！*\n")
                            break
                        if (br == 1):  # br不知道是啥，应该是break的标志
                            break
                        if not istimeforbig1:
                            print(
                                "*👴尽力了，等到红包池要关闭了都未等到15元以上大额红包被抢完，开始保底15元，注意查收！*\n"
                            )
                            break
                        if self.ten == 0:
                            self.queryredpool()
                        while self.ten == 1:
                            if not istimeforbig1:
                                br = 1
                                self.log(
                                    "*👴尽力了，等到红包池要关闭了都未等到任意大额红包被抢完，开始保底10元，注意查收！*\n"
                                )
                            self.queryredpool()
            if istimeforbig2:
                if self.propIdforuse == 3:
                    self.log("**当前符合抢30元以上大额红包的条件**\n")
                    self.log("**正使用10元必中符为您尝试抢30元以上的红包**\n")
                    # 拥有10块以上的必中符，先等待着试图抢30,要是10和15都没了，就直接去抢30的红包，或许有可能抢到50

                    while self.fifteen == 1:
                        if (self.thirty == 1 and self.fifty == 1):
                            self.log(
                                "&15有剩余，30元已被抢完，50元已被抢完，跳出监测，正在为您抢保底15元红包！*\n")
                            break
                        if (br == 1):
                            break
                        if not istimeforbig2:
                            self.log(
                                "*👴尽力了，等到红包池要关闭了都未等到15元以上大额红包被抢完，开始保底15元，注意查收！*\n"
                            )
                            break
                        if self.ten == 0:
                            self.queryredpool()
                        while self.ten == 1:
                            if not istimeforbig2:
                                br = 1
                                self.log(
                                    "*👴尽力了，等到红包池要关闭了都未等到任意大额红包被抢完，开始保底10元，注意查收！*\n"
                                )
                            self.queryredpool()
        if n_time < d_time7:
            self.propIdforuse = 1
        # 抢红包
        self.drawlottery()
        if int(self.showPriceNumber) < 500:
            self.redtobean()
        else:
            self.acceptRed()
        self.querymyreward()
        self.sendTaskRedBean()
        self.querymyProps()
        self.myRedBeanRecords()
        self.exit_and_push()  # 通知

    def sendTaskRedBean(self):
        self.log("**开始执行领取每日30豆的脚本:**\n")
        datas = "parActivityId=" + self.parActivityId + "&wm_latitude=" + str(
            self.wm_latitude) + "&wm_longitude=" + str(
                self.wm_longitude
            ) + "&token=" + self.token + "&portraitId=" + str(self.portraitId)
        url_sendTaskRedBean = r"/cfeplay/playcenter/batchgrabred/sendTaskRedBean"
        result2 = self.request(url_sendTaskRedBean, datas)
        if (result2["status"] == 0):
            self.log("%s\n今天领取成功%d个红包豆，请明日再来！\n" %
                     (result2["msg"], result2["sendBeanCount"]))
        elif (result2["status"] == 1):
            self.log("您今日已领取过😅,%s\n" % (result2["msg"]))
        elif (result2["status"] == -1):
            self.log("portraitId已失效,%s\n" % (result2["msg"]))
        else:
            self.log("请求接口失效或参数异常，请稍后再试!\n")

    def acceptRed(self):
        """
        定义接受红包函数
        获得红包小于5元时，不执行此函数
        并调用redtobean函数自动将红包转为红包豆
        若两个函数都不执行
        在抢红包成功5分钟左右红包会自动发放到账户
        """
        self.log("**开始执行发放天天神券🧧到红包库脚本:**\n")
        datas = "parActivityId=" + self.parActivityId + "&wm_latitude=" + str(
            self.wm_latitude) + "&wm_longitude=" + str(
                self.wm_longitude
            ) + "&token=" + self.token + "&batchId=" + self.batchId
        url_acceptRed = r"/cfeplay/playcenter/batchgrabred/acceptRed"
        result2 = self.request(url_acceptRed, datas)
        if (result2["code"] == 0):
            self.log("*👴抢到的红包已经领取成功啦，快去使用吧!*\n")
        elif (result2["code"] == 1):
            self.log("%s\n" % (result2["msg"]))
        elif (result2["code"] == 7):
            self.log("token已失效\n")
        else:
            self.log("请求接口失效或参数异常，请稍后再试!\n")

    def redtobean(self):
        """定义红包转红包豆函数，将小于5元的红包转为红包豆
        """
        self.log("**默认尝试执行面值小于5元🧧自动转红包豆脚本:**\n")
        datas = "parActivityId=" + self.parActivityId + "&wm_latitude=" + str(
            self.wm_latitude) + "&wm_longitude=" + str(
                self.wm_longitude
            ) + "&token=" + self.token + "&batchId=" + self.batchId
        url_drawlottery = r"/cfeplay/playcenter/batchgrabred/redToBean"
        result2 = self.request(url_drawlottery, datas)
        if (result2["code"] == 0):
            self.log("👴小额红包转红包豆成功!\n")
        elif (result2["code"] == 1 and result2["subcode"] == 12):
            # print("%s😅\n"%(result2["msg"]))
            self.log("没有待转换的红包😅\n")
        elif (result2["code"] == 7):
            self.log("token已失效\n")
        else:
            self.log("请求接口失效或参数异常，请稍后再试!\n")

    def drawlottery(self):
        self.log("**开始执行限时抢天天神券脚本🧧:**\n")
        datas = "parActivityId=" + self.parActivityId + "&wm_latitude=" + str(
            self.wm_latitude
        ) + "&wm_longitude=" + str(
            self.wm_longitude
        ) + "&token=" + self.token + "&batchId=" + self.batchId + "&isShareLink=true" + "&propType=1" + "&propId=" + str(
            self.propIdforuse)
        url_drawlottery = r"/cfeplay/playcenter/batchgrabred/drawlottery"
        result2 = self.request(url_drawlottery, datas)
        if (result2["code"] == 0):
            self.log(
                "领取成功!\n提示信息:%s\n红包属性:%s\n使用限制:%s\n红包价值:%s\n红包立即生效时间:%s\n红包剩余有效期:%s分钟\n"
                %
                (result2["msg"], result2["data"]["name"],
                 result2["data"]["priceLimitdesc"],
                 result2["data"]["showTitle"], result2["data"]["endTimeDesc"],
                 str(float(result2["data"]["leftTime"]) / 60000)))

            self.showPriceNumber = result2["data"]["showPriceNumber"]
            if int(self.showPriceNumber) < 500:
                self.log("**当前红包面值为%d元，小于5元，👴将自动执行小额红包转红包豆脚本!!**\n" %
                         (int(self.showPriceNumber) / 100))
            else:
                self.log("**当前红包面值为%d元，大于等于5元，👴将不会执行小额红包转红包豆脚本!!**\n" %
                         (int(self.showPriceNumber) / 100))
        elif (result2["code"] == 1 and result2["subcode"] == 3):
            self.log("%s😅\n" % (result2["msg"]))
        elif (result2["code"] == 1 and result2["subcode"] == -1):
            self.log("token错误或已失效,%s\n" % (result2["msg"]))
        elif (result2["code"] == 7):
            self.log("token已失效\n")
        else:
            self.log("请求接口失效或参数异常，请稍后再试!\n")

    def querymyreward(self):
        """查询已领取到的天天神券
        """
        datas = "parActivityId=" + self.parActivityId + "&token=" + self.token
        url_querymyreward = r"/cfeplay/playcenter/batchgrabred/myreward"
        result2 = self.request(url_querymyreward, datas)
        if (result2["code"] == 0 and len(result2["data"]["myawardInfos"])):
            self.log("👴开始遍历红包库:\n")
            self.log("红包库详细信息:\n")
            self.log("红包库中共有%d个红包\n" % (len(result2["data"]["myawardInfos"])))
            cent = 0
            count = 0
            isover15 = 0
            for k in result2["data"]["myawardInfos"]:
                if not k["status"]:
                    self.log(
                        "**第%d个红包有效!!!!**\n红包属性:%s\n使用限制:%s\n红包价值:%s元\n红包剩余有效期%s分钟\n"
                        % (cent + 1, k["name"], k["priceLimitdesc"],
                           k["showPriceNumberYuan"],
                           str(float(k["leftTime"]) / 60000)))
                    if (int(k["showPriceNumberYuan"]) > 15):
                        isover15 = 1
                    print("\n")
                else:
                    count = count + 1
                    if cent == 0:
                        self.log("**过期红包详情:**\n")

                cent = cent + 1
            if (self.propIdforuse != 5):
                self.log("总计已领取%d个红包,其中已过期%d个😅,有效%d个\n" %
                         (cent, count, cent - count))
            else:
                if isover15 == 1:
                    self.log(
                        "恭喜你领取大额限时红包,具体价值如上所示!!总计已领取%d个红包,其中已过期%d个😅,有效%d个\n" %
                        (cent, count, cent - count))
            print("\n")
        elif (result2["code"] == 1):
            self.log("%s\n" % (result2["msg"]))
        elif (result2["code"] == 7):
            self.log("token已失效\n")
        else:
            self.log("请求接口失效或参数异常，请稍后再试!\n")

    def log(self, text):
        print(text)
        self.desp += text

    def request(self, url, data):
        try:
            request = urllib.request.Request(self.baseurl + url,
                                             headers=self.header,
                                             data=data.encode("utf-8"),
                                             method="POST")
            response = urllib.request.urlopen(request)
            result = response.read().decode("utf-8")
            result2 = json.loads(result)
            return result2
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print("脚本执行失败👀，错误代码如下:\n")
                print(e.code)
            if hasattr(e, "reason"):
                print(e, "reason")

    def exit_and_push(self):
        if USE_TG:
            telegram(self.desp)
        exit(0)


def main_handler(event, context):
    m = MeiTuan()
    m.start()


if __name__ == "__main__":
    m = MeiTuan()
    m.start()
