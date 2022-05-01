import websocket
import requests
import json
import time
import random
import calendar
from threading import Thread
from langconv import *


def sendd(text):

	# text:发送的内容
	head = "https://s1.ax1x.com/2022/03/27/qw2gkn.png"
	return json.dumps({"cmd":"chat","text":str(text),"head":head})


class runbox:
	def __init__(self,room,name,pas):

		# 包含了频道、bot名称、bot密码
		self.room = room
		self.name = name
		self.pas = pas

		# 记录join成员
		self.join = []

		# 写入短文本
		self.text = []

		# 推荐列表
		self.wuhu = []
		self.site = []

		# afk人员清单
		self.afk = []

		# 游戏数据及游戏成员
		self.game = []
		self.play = []
		self.by = []

		# 真心话开关
		self.true = False

		# 飞花令开关
		self.flower = False

		# 词语接龙开关
		self.word = False

		# 故事制造机开关
		self.story = False
	

	def handle(self,json_data):

		# 将对应的cmd类型和对应的函数结合
		self.data = json_data

		# 如果接受到了包含cmd的json数据
		if "cmd" in self.data:

			# 发送文本类型
			if self.data["cmd"] == "chat":
				self.chat()

			# 用户进入类型
			elif self.data["cmd"] == "onlineAdd":
				self.onlineadd()

			# 进入聊天时用户的列表
			elif self.data["cmd"] == "onlineSet":
				self.onlineset()


	def chat(self):

		# 简化列表
		jo = self.join
		te = self.text
		wu = self.wuhu
		si = self.site
		pl = self.play
		ga = self.game
		af = self.afk
		by = self.by
		name = self.name
		room = self.room
		text = self.data["text"]
		nick = self.data["nick"]


		# 随机等待时间
		zz = random.choice([0.15,0.2,0.25])
		ee = random.choice([0.45,0.5,0.55])


		# bot私聊
		n = "\n"
		nn = "·\n"
		per = "/w {} .".format(nick) + n + nn


		# 保存聊天记录的文件名及路径
		chat = time.strftime("%Y.%m.%d")
		nel = "chats/" + room + "/" + chat + ".txt"
		nell = "chats/" + chat + " " + room + ".txt"
		hc = time.strftime("%H:%M:%S ",time.localtime())
		ms = hc + nick + n + text + n*2


		# 用于排除bot昵称
		with open("record/name.txt","r") as fp:
			bot = fp.readlines()
			bot.append(name + n)


		# 随机表情
		with open("record/meme.txt","r") as fp:
			me = fp.readlines()
			meme = random.choice(me)


		# 查找相关文件夹是否存在
		with open("record/channel.txt","r") as fp:
			chan = fp.readlines()

			# 按日期和频道写入消息和发送时间
			if room + n in chan:
				with open(nel,"a+") as fp:
					fp.write(ms)

			else:
				with open(nell,"a+") as fp:
					fp.write(ms)


		# 单独存放连接
		with open("record/web.txt","r+") as fp:
			eb = fp.readlines()
			if text + n not in eb and nick + n not in bot:
				if "http" in text:
					ch = time.strftime("%Y.%m.%d %H:%M:%S ",time.localtime())
					sm = nn + ch + nick + n + text + n
					fp.write(sm)


		# 当wu中的数据为10
		if len(wu) == 10:

			# 自动清空wu
			time.sleep(ee)
			ws.send(sendd("已自动清空推荐记录"))
			wu.clear()
	

		# 当si中的数据为10
		if len(si) == 10:

			# 自动清空si
			time.sleep(ee)
			ws.send(sendd("已自动清空随机记录"))
			si.clear()


		# 为防止刷屏而屏蔽bot昵称
		if nick + n not in bot:

			# 如果成员第一次打招呼
			if text in ["hello","hi","hey","hi yo","hey yo"] and nick not in jo:
				a = "hello {}".format(nick)
				b = "hi {}".format(nick)
				c = "hey {}".format(nick)
				d = "hi yo {}".format(nick)
				e = "hey yo {}".format(nick)
				f = "{}!".format(nick)

				# bot打招呼
				time.sleep(zz)
				ws.send(sendd(random.choice([a,b,c,d,f])))

				# 保存昵称到jo
				jo.append(nick)


			if "揭示板" in text or "hcs" in text:
				with open("record/date.txt","r") as fp:
					da = str(fp.readlines())
					date = da.replace('[\'','').replace('\']','').replace('\'',' ').replace('\\n','')

					if text[4:] == "":
						with open("record/hcs.txt","r") as fp:
							hc = fp.read()
							ws.send(sendd(per + hc + date))

					elif text[4:] in date:
						with open("record/board/" + text[4:] + ".txt","r") as fp:
							ca = fp.read()
							ht = "hack.chat珍贵历史遗像" + n + "（日期 " + text[4:] + "）" + n
							ws.send(sendd(per + ht + ca))

					else:
						ws.send(sendd("请检查日期是否正确"))


			if text in ["留言板","ees"]:
				with open("record/ees.txt","r") as fp:
					ee = fp.read()
					ws.send(sendd(per + ee))


			if text in ["欢迎语","wel"]:
				with open("record/wel.txt","r") as fp:
					el = fp.read()
					ws.send(sendd(per + el))


			if text in ["机器人","bot"]:
				with open("record/bot.txt","r") as fp:
					bo = fp.read()
					ws.send(sendd(per + bo))


			if text in ["网站","web"]:
				with open("record/web.txt","r") as fp:
					we = fp.read()
					ws.send(sendd(per + we))


			if text in ["功能","order"]:
				with open("record/order.txt","r") as fp:
					er = fp.read()
					ws.send(sendd(per + er))


			if text in ["帮助","help"]:
				with open("record/help.txt","r") as fp:
					he = fp.read()
					ws.send(sendd(per + he))


			if text in ["重置","clear"]:
				time.sleep(zz)

				# 如果wu和si中无数据
				if len(wu) == 0 and len(si) == 0:
					ws.send(sendd("当前无记录 不需要清空"))

				else:
					# 清空wu和si中的所有数据
					ws.send(sendd("已清空所有随机记录"))
					wu.clear()
					si.clear()


			if text in ["聊天","chat"]:
				a = "欢迎@{} 哦".format(name)
				time.sleep(zz)
				ws.send(sendd(a))


			if text in ["IP"]:
				a = "说明：查询IP地址的信息（已挂）" + n + "使用方法：IP-IP地址"
				time.sleep(zz)
				ws.send(sendd(per + a))


			if text in ["PING"]:
				a = "说明：PING某网站的域名（已挂）" + n + "使用方法：PING-域名"
				time.sleep(zz)
				ws.send(sendd(per + a))


			if text in ["ICP"]:
				a = "说明：查询ICP备案记录" + n + "使用方法：ICP-域名"
				time.sleep(zz)
				ws.send(sendd(per + a))


			if text in ["QQ"]:
				a = "说明：查询QQ号昵称" + n + "使用方法：QQ-QQ号"
				time.sleep(zz)
				ws.send(sendd(per + a))


			if text in ["翻译","tran"]:
				a = "说明：在线翻译" + n + "使用方法：F-要翻译的句子"
				time.sleep(zz)
				ws.send(sendd(per + a))


			if text in ["搜狗","sogo"]:
				a = "说明：查询搜狗百科" + n + "使用方法：SOGO-词条名称"
				time.sleep(zz)
				ws.send(sendd(per + a))


			if text in ["百度","baidu"]:
				a = "说明：查询百度百科" + n + "使用方法：BAIDU-词条名称"
				time.sleep(zz)
				ws.send(sendd(per + a))


			if text in ["天气","city"]:
				a = "说明：获取当天的天气信息" + n + "使用方法：CITY-不带市的城市"
				time.sleep(zz)
				ws.send(sendd(per + a))


			if text in ["网易云","id"]:
				a = "说明：在线解析网易云音乐" + n + "使用方法：ID-歌曲ID"
				time.sleep(zz)
				ws.send(sendd(per + a))


			if text in ["手机号","num"]:
				a = "说明：查询手机号的信息" + n + "使用方法：N-手机号"
				time.sleep(zz)
				ws.send(sendd(per + a))


			if text in ["垃圾分类","waste"]:
				a = "说明：垃圾分类" + n + "使用方法：L-垃圾名"
				time.sleep(zz)
				ws.send(sendd(per + a))


			if text in ["推荐","wuhu"]:
				with open("record/wuhu.txt","r") as fp:
					w = fp.readlines()
					ww = random.choice(w).replace('\\n',n)

					# wuhuu中的内容在wu的情况下
					if ww in wu:
						ws.send(sendd("{}中奖了 再来一次".format(nick)))
	
					else:
						ws.send(sendd(per + ww))
						wu.append(ww)


			# hack.chat成员的友情链接
			if text in ["树洞","tree"]:
				with open("record/tree.txt","r") as fp:
					f = fp.readlines()
					ff = random.choice(f).replace('\\n',n)

					# 内容在si的情况下
					if ff in si:
						ws.send(sendd("此链接被吃了"))
				
					else:
						# 直接发送f
						ws.send(sendd(per + ff))
						si.append(ff)


			if text in ["趣站","site"]:
				with open("record/site.txt","r") as fp:
					s = fp.readlines()
					ss = random.choice(s).replace('\\n',n)

					# 内容在si的情况下
					if ss in si:
						ws.send(sendd("不给不给 不给{}".format(nick)))
	
					else:
						# 直接发送s
						ws.send(sendd(per + ss))
						si.append(ss)


			if text in ["游戏","game"]:
				with open("record/game.txt","r") as fp:
					g = fp.readlines()
					gg = random.choice(g).replace('\\n',n)

					# 内容在si的情况下
					if gg in si:
						ws.send(sendd("哼 不可以贪心哦"))
	
					else:
						# 直接发送g
						ws.send(sendd(per + gg))
						si.append(gg)


			if text in ["网盘","pan"]:
				with open("record/pan.txt","r") as fp:
					p = fp.readlines()
					pp = random.choice(p).replace('\\n',n)

					# 内容在si的情况下
					if pp in si:
						ws.send(sendd("{}再试一次呗".format(nick)))
	
					else:
						# 直接发送p
						ws.send(sendd(per + pp))
						si.append(pp)


			if text in ["聊天室","room"]:
				with open("record/room.txt","r") as fp:
					h = fp.readlines()
					hh = random.choice(h).replace('\\n',n)

					# 内容在si的情况下
					if hh in si:
						ws.send(sendd("耶 就不告诉{}".format(nick)))

					else:
						# 直接发送h
						ws.send(sendd(per + hh))
						si.append(hh)


			if text in ["一言"]:

				# api:Hitokoto
				api = "https://v1.hitokoto.cn"
				se = requests.get(api)
				res = se.json()
				word = res["from"] + " " + res["creator"] + n + "「" + res["hitokoto"] + "」"

				# api:韩小韩API
				apii = "https://api.vvhan.com/api/ian"
				see = requests.get(apii)
				ress = see.text

				# 随机选取
				b = random.choice([word,ress])

				# 如果双引号存在就替换
				if "“" in b or "”" in b:
					ws.send(sendd(per + b.replace('“','「').replace('”','」')))

				# 如果b内容是ress
				elif b == ress:
					ws.send(sendd(per + "「" + b + "」"))

				else:
					# 以上两种情况皆无
					ws.send(sendd(per + b))


			if text in ["励志"]:

				# api:SuixinAPI
				api = "http://api.botwl.cn/api/yhyl"
				se = requests.get(api)
				res = "「" + se.text + "」"
				ws.send(sendd(per + res))


			if text in ["抽签"]:
				
				# api:SuixinAPI
				api = "http://api.botwl.cn/api/qiuqian"
				se = requests.get(api)
				res = se.text.replace('[\\n]',n)
				ws.send(sendd(per + res))


			if text in ["笑话"]:
				
				# api:木小果API
				api = "https://api.muxiaoguo.cn/api/xiaohua?api_key=c2b3c8ef3925db80"
				se = requests.get(api)
				res = se.json()
				a = res["data"]
				word = "【" + a["title"] + "】" + n + a["content"]

				# api:韩小韩API
				apii = "https://api.vvhan.com/api/xh"
				see = requests.get(apii)
				ress = see.text

				# 随机选取
				b = random.choice([word,ress])

				# 如果双引号存在就替换
				if "“" in b or "”" in b:
					ws.send(sendd(per + b.replace('“',n + '「').replace('”','」' + n)))

				# 如果括号不在b中
				elif "【" not in b or "】" not in b:
					ws.send(sendd(per + "「" + b + "」"))

				else:
					# 以上两种情况皆无
					ws.send(sendd(per + b))


			if text in ["情话"]:

				# api:沙雕APP
				api = "https://api.lovelive.tools/api/SweetNothings/count/Serialization/serializationType"
				se = requests.get(api)
				res = se.json()
				word = res["returnObj"]
				a = random.choice(word)

				# api:UomgAPI
				apii = "https://api.uomg.com/api/rand.qinghua"
				see = requests.get(apii)
				ress = see.json()
				wordd = ress["content"]

				# api:韩小韩API
				apiii = random.choice(["https://api.vvhan.com/api/love","https://api.vvhan.com/api/sao"])
				seee = requests.get(apiii)
				resss = seee.text
				
				# 随机选取
				b = random.choice([a,wordd,resss])

				# 如果双引号存在就替换
				if "“" in b or "”" in b:
					ws.send(sendd(per + b.replace('“','「').replace('”','」')))

				else:
					# 以上两种情况皆无
					ws.send(sendd(per + "「" + b + "」"))
	

			if text in ["哲学"]:
				
				# api:奇远api
				api = "https://api.oddfar.com/yl/q.php?c=2011"
				se = requests.get(api)
				res = "「" + se.text + "」"
				ws.send(sendd(per + res))


			if text in ["古诗词"]:

				# api:木小果API
				api = "https://api.muxiaoguo.cn/api/Gushici?api_key=1469d017a08f2827"
				se = requests.get(api)
				res = se.json()
				a = res["data"]
				word = a["title"] + " " + a["author"] + n + "「" + a["min_content"] + "」"
				ws.send(sendd(per + word))


			if text in ["彩虹屁"]:

				# api:木小果API
				api = "https://api.muxiaoguo.cn/api/caihongpi?api_key=4acee95f422ea04a"
				se = requests.get(api)
				res = se.json()
				b = res["data"]["comment"]

				# 如果双引号存在就替换
				if "“" in b or "”" in b:
					ws.send(sendd(per + b.replace('“','「').replace('”','」')))

				else:
					# 在两边加上括号
					ws.send(sendd(per + "「" + b.replace('"','') + "」"))


			if text in ["毒鸡汤"]:

				# api:木小果API
				api = "https://api.muxiaoguo.cn/api/dujitang?api_key=e5103c1917bc4026"
				se = requests.get(api)
				res = se.json()
				a = res["data"]
				word = a["comment"]

				# api:搏天api
				apii = "http://api.btstu.cn/yan/api.php"
				see = requests.get(apii)
				ress = see.text
				
				# 随机选取并发送
				b = random.choice([word,ress])
				ws.send(sendd(per + "「" + b + "」"))


			if text in ["今日曰"]:

				# api:韩小韩API
				api = "https://api.vvhan.com/api/en"
				se = requests.get(api)
				res = se.json()
				a = res["data"]
				b = "Today Is " + a["month"] + " " + a["day"]
				word = b + n + "「" + a["zh"] + "」" + n + "「" + a["en"] + "」"
				ws.send(sendd(per + word))
	

			if text in ["猜字谜"]:
				
				# api:SuixinAPI
				api = "http://api.botwl.cn/api/miyu"
				se = requests.get(api)
				res = se.text
				ws.send(sendd(per + res.replace(' ',n)))
	

			if text in ["中二网名"]:
				
				# api:远昔API
				api = "https://www.yuanxiapi.cn/api/wangming/"
				se = requests.get(api)
				res = se.json()
				a = "「" + res["name"] + "」"
				ws.send(sendd(per + a))


			if text in ["骂人宝典"]:
				
				# api:奇远api
				api = "https://api.oddfar.com/yl/q.php?c=1009"
				se = requests.get(api)
				res = se.text
				with open("record/ma.txt","r") as fp:
					ma = fp.readlines()
					maa = random.choice(ma)
					ws.send(sendd(per + "「" + random.choice([res,maa]).replace(n,'') + "」"))


			if text in ["舔狗日记"]:

				# api:小歪API
				api = "https://api.ixiaowai.cn/tgrj/index.php"
				se = requests.get(api)
				res = "「" + se.text + "」"

				# api:木小果API
				apii = "https://api.muxiaoguo.cn/api/tiangourj?api_key=300ec8fe32c3562a"
				see = requests.get(apii)
				ress = see.json()
				a = ress["data"]
				word = "「" + a["comment"] + "」"

				# 仅为恶搞
				ee = chat + " " + room + " " + name + n
				
				# 随机选取并发送
				b = random.choice([res,word])
				ws.send(sendd(per + ee + b.replace('*','').replace('“','『').replace('”','』')))
	

			if text in ["社会语录"]:

				# api:零七生活API 奇远api
				api = random.choice(["https://api.oick.cn/yulu/api.php","https://api.oddfar.com/yl/q.php?c=1002"])
				se = requests.get(api)
				res = se.text.replace('\"','')
				word = "「" + res + "」"
				ws.send(sendd(per + word))
	

			if text in ["网易热评"]:

				# api:木小果API
				api = "https://api.muxiaoguo.cn/api/163reping?api_key=5d60829ddff7ea03"
				se = requests.get(api)
				res = se.json()
				a = res["data"]
				word = "来自 " + a["nickname"] + a["songName"] + n + "「" + a["content"] + "」"
				ws.send(sendd(per + word))
	

			if text in ["摸鱼日历"]:

				# api:韩小韩API
				api = "https://api.vvhan.com/api/moyu"
				se = requests.get(api)
				res = se.url
				ws.send(sendd(per + "![](" + res + ")"))


			if text in ["乘法口诀"]:
				with open("record/x.txt","r") as fp:
					x = fp.readlines()
					xx = random.choice(x).replace(n,'')
					time.sleep(zz)
					ws.send(sendd(per + "「" + xx + "」"))
	

			if text in ["今日的世界"]:

				# api:韩小韩API
				time.sleep(zz)
				ws.send(sendd(per + "![](https://api.vvhan.com/api/60s)"))
	

			if text in ["历史上的今天"]:

				# api:公共api
				api = "https://qqlykm.cn/api/lishi/index.php"
				se = requests.get(api)
				res = "【" + se.text + "】"
				ws.send(sendd(per + res))
	

			if text in ["七濑胡桃","heal"]:

				# api:小歪API
				api = "https://api.ixiaowai.cn/mcapi/mcapi.php"
				se = requests.get(api)
				res = se.url
				ws.send(sendd(per + "![](" + res + ")"))
	

			if text in ["每日必应","bing"]:

				# api:保罗API
				api = "https://api.vvhan.com/api/bing?type=sj"
				se = requests.get(api)
				res = se.url
				ws.send(sendd(per + "![](" + res + ")"))
	

			if text in ["小姐姐","cutie"]:

				# api:夏沫博客 SuixinAPI
				api = random.choice(["https://cdn.seovx.com/ha/?mom=302","http://api.botwl.cn/api/meinvtu?n=1"])
				se = requests.get(api)
				res = se.url
				ws.send(sendd(per + "![](" + res + ")"))
	

			if text in ["阿鲁","aru"]:

				# api:姬长信API
				api = "https://api.isoyu.com/ARU_GIF_S.php"
				se = requests.get(api)
				res = se.url
				ws.send(sendd(per + "![](" + res + ")"))


			if text in ["涩图","acg"]:

				# api:晓晴博客 樱花 MuRongPIG自建
				api = random.choice(["https://acg.toubiec.cn/random.php","https://www.dmoe.cc/random.php","https://cdn.mrpig.cf/"])
				se = requests.get(api)
				res = se.url
				ws.send(sendd(per + "![](" + res + ")"))


			if text in ["头像","head"]:

				# api:搏天api
				api = "http://api.btstu.cn/sjtx/api.php"
				se = requests.get(api)
				res = se.url
				ws.send(sendd(per + "![](" + res + ")"))
	

			if text in ["音乐","music"]:
				
				# 保罗API
				api = "https://api.paugram.com/acgm"
				se = requests.get(api)
				res = se.json()
				word = res["title"] + " " + res["artist"] + " " + n + res["link"]
				ws.send(sendd(per + word))


			if text in ["日历","cal"]:

				# 日历模块调用calendar库
				a = int(time.strftime("%Y"))
				b = int(time.strftime("%m"))
				cal = calendar.month(a,b).replace(' ','⠀').replace('⠀⠀',' ⠀')
				ws.send(sendd(per + cal))


			if text in ["农历","date"]:

				# api:木小果API
				api = "https://api.muxiaoguo.cn/api/yinlongli?api_key=dd488292c6ea462a"
				se = requests.get(api)
				res = se.json()
				a = res["data"]
				word = "日：" + a["lunar"] + n + "年：" + a["yearZodiac"] + "（" + a["lunarYearName"] + "）"
				ws.send(sendd(per + word))


			if text in ["表情","meme"]:

				# 表情参见设定部分
				ws.send(sendd(meme))


			if text in ["换色","color"]:

				# api:SuixinAPI 韩小韩API
				api = random.choice(["http://api.botwl.cn/api/sjys","https://api.vvhan.com/api/color"])
				se = requests.get(api)
				a = "/color " + se.text

				# 更换bot的颜色
				ws.send(sendd(a))

				# 发送后重新换回44FF00
				ws.send(sendd("16进制颜色：" + se.text + n + "（仅在hack.chat有效）"))
				ws.send(sendd("/color 44FF00"))


			if text in ["时间","time"]:

				# 获取计算机时间
				a = time.strftime("Time %a %Y.%m.%d %H:%M:%S",time.localtime())
				ws.send(sendd(a))


			if "HC-" in text and text[2] == "-":

				# 判断字数是否小于3
				if len(text[3:]) < 3:
					ws.send(sendd("留言的内容至少3个字 请不要氵哦"))

				else:
					# 把留言写入揭示板中
					with open("record/board/" + chat + ".txt","a+") as fp:
						ch = time.strftime("%Y.%m.%d %H:%M:%S ",time.localtime())
						an = ch + nick + "：" + n
						fp.write(nn + an + text[3:] + n)
						ws.send(sendd("已成功把{}的留言写到HC揭示板里".format(nick)))

						# 打开日期文件
						with open("record/date.txt","r+") as fpp:
							da = fpp.readlines()

							# 如果日期不存在 则向da写入日期
							if a + n not in da:
								fpp.write(a + n)
								fp.close()
								fpp.close()


			if "E-" in text and text[1] == "-":
				with open("record/back/" + nick + ".txt","w") as fp:

					# 防止bot被卡BUG
					if "/" in text:
						ws.send(sendd("包含无效的字符"))

					# 设置为空时重置
					elif text[2:] == "" and "/" not in text:
						ws.send(sendd("已重置欢迎语"))
						fp.truncate(0)

					else:
						# 把欢迎语写入带昵称的文件中
						fp.write(text[2:] + n)
						ws.send(sendd("设置成功 将在下次进入聊天室时生效"))

						# 打开昵称文件
						with open("record/join.txt","r+") as fpp:
							ck = fpp.readlines()

							# 如果昵称不存在 则向ck写入昵称
							if nick + n not in ck:
								fpp.write(nick + n)
								fp.close()
								fpp.close()


			if "IP-" in text and text[2] == "-":

				# 判断词后是否留空
				if text[3:] == "":
					ws.send(sendd("请勿留空哦"))

				else:
					# api:韩小韩API
					url = "https://api.vvhan.com/api/getIpInfo"
					data = {"ip":text[3:]}
					se = requests.get(url,data)
					res = se.json()
					a = nn + "地址：" + res["ip"] + n + "所属：" + b["lsp"]
					b = res["info"]
					if b["prov"] == "":
						ws.send(sendd(a))

					else:
						c = n + nn + "国家：" + b["country"] + n + "省份：" + b["prov"] + n + "城市：" + b["city"]
						ws.send(sendd(a + c))


			if "PING-" in text and text[4] == "-":

				# 判断词后是否留空
				if text[5:] == "":
					ws.send(sendd("请勿留空哦"))

				else:
					# api:SuixinAPI
					url = "http://api.botwl.cn/api/ping"
					data = {"url":text[5:]}
					se = requests.get(url,data)
					res = se.json()

					# 如果状态码为1 则成功
					if res["code"] == 1:
						a = nn + res["host"] + "（" + res["ip"] + "）"
						b = n + nn + "最快用时：" + res["ping_time_min"] + n + "最慢用时：" + res["ping_time_max"]
						ws.send(sendd(a + b.replace(' ','')))

					else:
						ws.send(sendd("获取失败 请检查域名"))


			if "ICP-" in text and text[3] == "-":

				# 判断词后是否留空
				if text[4:] == "":
					ws.send(sendd("请勿留空哦"))

				else:
					# api:零七生活API
					url = "https://api.oick.cn/icp/api.php"
					data = {"url":text[4:]}
					se = requests.get(url,data)
					res = se.json()

					# 如果状态码为200 则成功
					if res["code"] == 200:
						a = nn + res["site_name"] + "（" + res["site_index"] + "）"
						b = n + nn + "单位：" + res["name"] + n + "类型：" + res["nature"]
						c = n + nn + "备案信息：" + res["icp"] + n + "备案时间：" + res["site_time"]
						ws.send(sendd(a + b + c))

					# 如果状态码为201 无记录
					elif res["code"] == 201:
						ws.send(sendd("未有此域名ICP备案记录"))

					else:
						ws.send(sendd("获取失败 请检查域名"))


			if "QQ-" in text and text[2] == "-":

				# 判断词后是否留空
				if text[3:] == "":
					ws.send(sendd("请勿留空哦"))

				else:
					# api:搏天api
					url = "http://api.btstu.cn/qqxt/api.php"
					data = {"qq":text[3:]}
					se = requests.get(url,data)
					res = se.json()

					if res["code"] == 1 and res["name"] != "":
						a = nn + res["name"] + n + text[3:]
						ws.send(sendd(a))

					else:
						ws.send(sendd("查询失败 请检查QQ号"))


			if "F-" in text and text[1] == "-":

				# 判断词后是否留空
				if text[2:] == "":
					ws.send(sendd("请勿留空哦"))

				else:
					# api:网易有道翻译
					url = "http://fanyi.youdao.com/translate"
					head = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"}

					if len(text) > 102:
						ws.send(sendd("超出最大字符数100"))

					else:
						data = {"doctype":"json","type":"AUTO","i":text[2:]}
						se = requests.get(url,params = data,headers = head,timeout = 10)
						res = se.json()

						# 如果状态码为0 则成功
						if res["errorCode"] == 0:
							a = res["translateResult"][0][0]["tgt"]
							ws.send(sendd("{} said：".format(nick) + a.lower()))

						else:
							ws.send(sendd("翻译请求失败"))


			if "SOGO-" in text and text[4] == "-":

				# 判断词后是否留空
				if text[5:] == "":
					ws.send(sendd("请勿留空哦"))

				else:
					# api:木小果API
					url = "https://api.muxiaoguo.cn/api/Baike"
					data = {"type":"Sogo","word":text[5:],"api_key":"cb28182953ac4557"}
					se = requests.get(url,data)
					res = se.json()
					a = res["data"]

					# 如果状态码为200 则成功
					if res["code"] == 200:
						b = nn + "查询：" + text[5:] + n + nn + "搜狗：" + a["content"]
						c = b.replace('。','。' + n).replace('(','（').replace(')','）').replace('“','「').replace('”','」')
						ws.send(sendd(c))

					else:
						ws.send(sendd("查询失败 无此百科"))


			if "BAIDU-" in text and text[5] == "-":

				# 判断词后是否留空
				if text[6:] == "":
					ws.send(sendd("请勿留空哦"))

				else:
					# api:木小果API
					url = "https://api.muxiaoguo.cn/api/Baike"
					data = {"type":"Baidu","word":text[6:],"api_key":"cb28182953ac4557"}
					se = requests.get(url,data)
					res = se.json()
					a = res["data"]

					# 如果状态码为200 则成功
					if res["code"] == 200:
						b = nn + "查询：" + text[6:] + n + nn + "百度：" + a["content"]
						c = b.replace('。','。' + n).replace('"','').replace('(','（').replace(')','）').replace('“','「').replace('”','」')
						ws.send(sendd(c))

					else:
						ws.send(sendd("查询失败 无此百科"))


			if "CITY-" in text and text[4] == "-":

				# 判断词后是否留空
				if text[5:] == "":
					ws.send(sendd("请勿留空哦"))

				else:
					# api:木小果API
					url = "https://api.muxiaoguo.cn/api/tianqi"
					data = {"city":text[5:],"type":1,"api_key":"9410e360a940cb5e"}
					se = requests.get(url,data)
					res = se.json()
					a = res["data"]

					# 如果状态码为200 则成功
					if res["code"] == 200:
						b = nn + "城市：" + text[5:] + "（" + a["weather"] + "）"
						c = n + "温度：" + a["temp"] + "°C" + n + "湿度：" + a["SD"]
						d = n + nn + "风向：" + a["WD"] + n + "风级：" + a["WS"] + n + "风速：" + a["wse"]
						e = n + nn + "更新时间：" +  a["time"]
						ws.send(sendd(b + c + d + e))

					else:
						ws.send(sendd("查询失败 请检查城市"))


			if "ID-" in text and text[2] == "-":

				# 判断词后是否留空
				if text[3:] == "":
					ws.send(sendd("请勿留空哦"))

				else:
					# api:零七生活API
					url = "https://api.oick.cn/wyy/api.php"
					data = {"id":text[3:]}
					se = requests.get(url,data)
					res = se.url
					if "https://music.163.com/404" == res:
						ws.send(sendd("网易云id获取失败 请检查"))

					else:
						ws.send(sendd(res))


			if "N-" in text and text[1] == "-":
				if text[2:] == "":
					ws.send(sendd("请勿留空哦"))

				else:
					# api:SuixinAPI
					url = "http://api.botwl.cn/api/sjhgsd"
					data = {"sjh":text[2:]}
					se = requests.get(url,data)
					res = se.json()

					# 如果状态码为1 则成功
					if res["code"] == 1:
						a = nn + "手机号：" + res["手机号"]
						b = n + nn + "归属地：" + res["归属地"] + n + "卡类型：" + res["卡类型"]
						ws.send(sendd(a + b))

					else:
						ws.send(sendd("获取失败 请检查手机号"))


			if "L-" in text and text[1] == "-":
				if text[2:] == "":
					ws.send(sendd("请勿留空哦"))

				else:
					# api:搏天api
					url = "https://api.vvhan.com/api/la.ji"
					data = {"lj":text[2:]}
					se = requests.get(url,data)
					res = se.json()

					if res["sort"] != "俺也不知道是什么垃圾~":
						ws.send(sendd(res["sort"]))

					else:
						ws.send(sendd("所以这是什么垃圾"))


			if "http" in text and "h" in text[0]:

				# api:远昔API
				url = "https://yuanxiapi.cn/api/info/"
				data = {"url":text}
				se = requests.get(url,data)
				res = se.json()

				# 如果状态码为200 则成功
				if res["code"] == 200:
					a = res["title"] + n + text
					ws.send(sendd(nn + a))

				else:
					ws.send(sendd("无法获取网站标题信息"))


			if text == name:
				with open("record/eebot.txt","r") as fp:
					eb = fp.read()
					time.sleep(zz)
					ws.send(sendd(per + eb))


			if "@" in text[0]:
				time.sleep(ee)
				a = len(name) + 2
				url = "http://api.botwl.cn/api/aick"
				if "@" + name in text:
					if text[a:] == "":
						time.sleep(ee)
						ws.send(sendd(random.choice(["{}有事吗".format(nick),"欢迎来hc聊天","找ee去吧","好耶"])))


					elif "好" in text[a:]:
						time.sleep(ee)
						if "吧" in text[a:]:
							ws.send(sendd(random.choice(["那不就没问题了嘛（","这就对了","嗯嗯"])))

						elif "不" in text[a:]:
							ws.send(sendd(random.choice(["靠在{}身边）".format(nick),"啊哈"])))

						elif "看" in text[a:] or "康" in text[a:]:
							ws.send(sendd(random.choice([name + "觉得不错嘛","哇哦"])))

						elif "大家" in text[a:] or "你" in text[a:]:
							ws.send(sendd(random.choice(["欢迎来到hc！","你好你好"])))


					elif "绿" in text[a:] or "44FF00" in text[a:]:
						time.sleep(ee)
						ws.send(sendd(random.choice(["ww绿！","hc最棒的颜色","大自然的颜色"])))


					elif "可怕" in text[a:] or "吓人" in text[a:] or "害怕" in text[a:]:
						time.sleep(ee)
						ws.send(sendd(random.choice(["摸摸","富强民主文明和谐美丽的……hc","社会主义核心价值观"])))


					else:
						data = {"msg":text[a:].replace(' ','')}
						se = requests.get(url,data)
						res = se.json()
						l = res["msg"]
						if res["code"] == "1":
							with open("record/aick.txt","r") as fp:
								ai = fp.readlines()
								if text[a:] + n not in ai:
									with open("record/text.txt","r") as fpp:
										xt = random.choice(fpp.readlines())
										tx = xt.replace('我',name).replace('你',nick).replace('，',' ')
										if "{" in l and "}" in l:
											ws.send(sendd(tx))

										else:
											b = l.replace('随心',"bot").replace('我',name)
											b = b.replace('你',nick).replace('，',' ')
											b = Converter('zh-hans').convert(b)
											if (len(b) % 2) == 0:
												c = random.choice(["（","）","（）"])
												ws.send(sendd(b + c))

											else:
												b = b.replace('啥','什么').replace('咋','怎么')
												b = b.replace('“','「').replace('”','」')
												ws.send(sendd(b))

								else:
									ws.send(sendd(tx))

						else:
							time.sleep(zz)
							ws.send(sendd(random.choice(["诶嘿",text[a:]])))


			if len(te) == 25 or len(te) == 75:
				time.sleep(ee)
				url = "http://api.botwl.cn/api/aick"
				if len(text) < 10 and len(text) > 1:
					data = {"msg":text.replace(' ','')}
					se = requests.get(url,data)
					res = se.json()
					a = res["msg"]
					b = a.replace('随心',"bot").replace('我',name).replace('你',nick).replace('，',' ')
					b = Converter('zh-hans').convert(b)
					te.append(text)
					if "{" in a and "}" in a:
						c = random.choice(["嗨嗨","欧拉欧拉","话说bot还是比较聪明的（"])
						ws.send(sendd(c))

					else:
						if (len(b) % 2) != 0:
							c = b + random.choice(["（","）","（）"])
							ws.send(sendd(c))

						else:
							c = b.replace('啥','什么').replace('咋','怎么').replace('“','「').replace('”','」')
							ws.send(sendd(c))


			# 如果text的长度小于指定的值
			if len(text) < 10 and "-" not in text:

				# 未有游戏进行
				if len(ga) == 0:

					# 将字符数<10的话写入te
					time.sleep(zz)
					te.append(text)

					# te长度为50时bot随机输出te内容
					if len(te) == 50:
						t = random.choice(te).replace('我',name).replace('你',nick)
						ws.send(sendd(t))

					# te长度为100时bot复读一句话
					if len(te) == 100:
						ws.send(sendd(text))
						te.clear()

				# 复读或发送meme中的表情
				if text in meme:
					t = text.replace('我',name).replace('你',nick).replace('，',' ')
					ws.send(sendd(random.choice([t,meme])))


			if len(text) < 30 and len(text) > 10 and "@" not in text and name not in text:

				# 将话写入text文件
				with open("record/text.txt","r+") as fp:
					tx = fp.readlines()
					if text + n not in tx:
						fp.write(text + n)


			# 如果昵称在af列表里
			if nick in af:

				# 排除以下消息
				if text not in ["挂机","afk","挂机列表","list"]:

					# 把昵称从af中移除
					a = "welcome back {}".format(nick)
					b = "{} is back".format(nick)
					time.sleep(zz)
					ws.send(sendd(random.choice([a,b])))
					del af[af.index(nick)]

				# 不能重复挂机
				elif text in ["挂机","afk"]:
					time.sleep(zz)
					ws.send(sendd("{} is already in afk list".format(nick)))


			# 如果昵称不在af列表里
			if nick not in af:

				# 将昵称加入af
				if text in ["挂机","afk"]:
					time.sleep(zz)
					ws.send(sendd("{} is now afk".format(nick)))
					af.append(nick)

					# 退出真心话游戏
					if self.true == True and nick in by:
						time.sleep(ee)
						ws.send(sendd("{}已离开真心话游戏".format(nick)))
						a = by.index(nick)
						del by[a]
						del pl[a]


			# 查看af列表
			if text in ["挂机列表","list"]:

				# 若af的长度为0
				if len(af) == 0:
					time.sleep(zz)
					ws.send(sendd("目前无人挂机 列表为空"))

				else:
					# 输出列表
					a = nn + "afk list:" + str(af).replace('[\'','').replace('\']','').replace('\'',' ')
					time.sleep(zz)
					ws.send(sendd(a))
	

			# 如果有人提到了挂机成员
			for name in af:

				# 提示该成员在afk状态
				if "@{}".format(name) in text:
					time.sleep(zz)
					ws.send(sendd("{} is now afk".format(name)))


			# 防止多个游戏同时进行
			if text in ["真心话","飞花令","词语接龙","故事制造机"]:
				if len(ga) != 0 and text not in ga:
					with open("record/over.txt","r") as fp:
						a = fp.read().replace('——',ga[0])
						time.sleep(zz)
						ws.send(sendd(a))


			# 如果想玩的游戏已经开始了
			if text in ga:
				time.sleep(zz)
				ws.send(sendd("{}已经开始了".format(ga[0])))


			# 在有游戏进行的情况下
			if len(ga) != 0:

				# 结束游戏
				if text in ["结束游戏"]:
					time.sleep(zz)
					ws.send(sendd("{}已结束".format(ga[0])))

					# 清空所有游戏数据
					by.clear()
					pl.clear()
					ga.clear()

					# 关闭所有开关
					self.true = False
					self.word = False
					self.story = False
					self.flower = False
				
				# 重置游戏
				elif text in ["重置游戏"]:
					time.sleep(zz)
					ws.send(sendd("{}已重置".format(ga[0])))

					# 清空游戏内容
					by.clear()
					pl.clear()

					# 在真心话开关打开的情况下
					if self.flower == True:
						time.sleep(ee)
						ws.send(sendd("下句的关键词在第1个字上"))
			

			if text in ["真心话"]:

				# 如果游戏未开启
				if self.true == False and len(ga) == 0:

					# 真心话说明
					with open("record/true.txt","r") as fp:
						a = fp.read()
						ws.send(sendd(a))
						time.sleep(zz)
						ws.send(sendd("真心话游戏开始"))
						ga.append(text)

						# 真心话开关打开
						self.true = True
				

			if text in ["飞花令"]:

				# 如果游戏未开启
				if self.flower == False and len(ga) == 0:

					# 飞花令说明
					with open("record/flower.txt","r") as fp:
						a = fp.read()
						ws.send(sendd(a))
						time.sleep(zz)
						ws.send(sendd("游戏开始 下句的关键词在第1个字上"))
						ga.append(text)

						# 飞花令开关打开
						self.flower = True
				

			if text in ["词语接龙"]:

				# 如果游戏未开启
				if self.word == False and len(ga) == 0:

					# 词语接龙说明
					with open("record/word.txt","r") as fp:
						a = fp.read()
						ws.send(sendd(a))
						time.sleep(zz)
						ws.send(sendd("请{}开一个好头吧".format(nick)))
						ga.append(text)
						by.append(nick)

						# 词语接龙开关打开
						self.word = True
				

			if text in ["故事制造机"]:

				# 如果游戏未开启
				if self.story == False and len(ga) == 0:

					# 故事制造机说明
					a = nn + "游戏制作中 敬请期待"
					ws.send(sendd(a))
					ga.append(text)

					# 故事制造机开关打开
					self.story = True


		if text in ["随机数","r"]:

			# 随机1~999的数字
			r = random.randint(1,999)

			# 如果真心话开关开启
			if self.true == True:

				# 无效在by中的昵称
				if nick in by:
					ws.send(sendd("{}已经r过了".format(nick)))

				else:
					# 发送r数字并记录值和昵称
					by.append(nick)
					pl.append(int(r))
					ws.send(sendd(r))

			else:
				# 如果真心话开关关闭
				ws.send(sendd(r))


		if text in ["结算"]:

			# 如果真心话开关开启
			if self.true == True:

				# 游戏成员<2人
				if len(by) < 2:
					time.sleep(zz)
					ws.send(sendd("人数不足 至少要有2个人"))

				else:
					# 获取pl中最大和最小的数字
					j = max(pl)
					k = min(pl)

					# 获取pl中分别对应最大和最小的成员
					v = by[pl.index(j)]
					m = by[pl.index(k)]

					# 将数字字符串化
					a = "最大：" + str(j) + "（" + v + "）"
					b = "最小：" + str(k) + "（" + m + "）"
					c = nn + "本次参与人数：" + str(len(by)) + n + nn + a + n + b

					# 发送并清空by和pl
					time.sleep(zz)
					ws.send(sendd(c))
					time.sleep(ee)
					ws.send(sendd("@" + v + " 向@" + m + " 提问"))
					by.clear()
					pl.clear()

			# 如果成语接龙开关开启
			if self.word == True:

				# 如果pl中没有数据
				if len(pl) == 0:
					time.sleep(zz)
					ws.send(sendd("不允许在游戏未开始前结束"))

				else:
					# 发送游戏数据后清空
					j = nn + str(pl).replace(',',n).replace('[\'','').replace('\']','').replace('\'',' ')
					k = n + nn + "by." + str(by).replace('[\'','').replace('\']','').replace('\'',' ')
					q = "（" + str(len(by)) + "）"
					time.sleep(zz)
					ws.send(sendd(str(j + k + q)))
					by.clear()
					pl.clear()
	

		# 如果成语接龙开关开启
		if self.word == True:

			# 获取特定位置的字
			z = len(pl)
			a = "「" + text[2:] + "」 "
			b = "下一词的开头为「" + text[-1] + "」"

			# P-存在的情况下
			if "P-" in text and str(text).count("-") == 1:

				# 如果文本长度为6
				if len(text) == 6:

					# 如果pl中没有数据
					if z == 0:
						time.sleep(zz)
						pl.append(text[2:])

						# 昵称已在by的情况下
						if nick in by:
							ws.send(sendd(a + b))

						else:
							# 昵称不在by
							ws.send(sendd("那好 就由{}开始吧".format(nick)))
							time.sleep(zz)
							ws.send(sendd(a + b))

							# 清空by中的昵称再将新昵称写入
							by.clear()
							by.append(nick)

					else:
						# pl中已有数据
						time.sleep(zz)

						# 判断文本中的第三个字是否为前成语的末尾
						if text[2] in pl[z - 1][-1]:
							ws.send(sendd(a + b))
							pl.append(text[2:])

							# 如果昵称不在by中
							if nick not in by:
								by.append(nick)

						else:
							# 成语的头尾接不上
							ws.send(sendd("请检查词语的头尾是否接上"))

				else:
					# 文本长度不是6
					time.sleep(zz)
					ws.send(sendd("请输入四字词哦"))


		# 如果飞花令开关开启
		if self.flower == True:

			# 获取特定位置的字
			z = len(pl) + 2
			v = str(pl).count("花")

			# 如果z列表的长度为9
			if z == 9:
				a = nn + str(pl).replace(',',n).replace('[\'','').replace('\']','').replace('\'',' ')
				b = n + nn + "by." + str(by).replace('[\'','').replace('\']','').replace('\'',' ')
				c = "（" + str(len(by)) + "）"
				time.sleep(ee)
				ws.send(sendd(a + b + c))
				time.sleep(ee)

				# 清空游戏数据并结束游戏
				by.clear()
				pl.clear()
				ga.clear()
				self.flower = False

				# 如果花字多于14个
				if v > 14:
					ws.send(sendd("游戏结束 天女散花x" + str(v)))

				else:
					# 直接结束
					ws.send(sendd("游戏结束 完美撒花"))
	
			# 排除bot的昵称
			elif nick + n not in bot:

				# z列表的长度不为9且P-存在的情况下
				if z != 9 and "P-" in text and str(text).count("-") == 1:

					# 如果文本长度为9
					if len(text) == 9:

						# 如果关键字在固定位置上
						if text[z] == "花":
							a = random.choice(["Perfect! ","Pretty! ","Great! ","Good! "])
							time.sleep(zz)
							pl.append(text[2:])
							time.sleep(zz)

							# 如果昵称不在by中
							if nick not in by:
								by.append(nick)

							# 如果z列表的长度不为8
							if z != 8:
								ws.send(sendd(a + "下句的关键词在第" + str(z) + "个字上"))

							# 如果z列表的长度为8
							if z == 8:
								ws.send(sendd("OK! 七句诗成功输出"))

						# 如果关键字没有在固定位置上
						elif text[z] != "花":
							time.sleep(zz)
							ws.send(sendd("关键词没在固定位置上哦"))
	
					else:
						# 文本长度不是9
						time.sleep(zz)
						ws.send(sendd("请输入七言律诗"))


	def onlineadd(self):

		# 简化和设定部分
		n = "\n"
		jo = self.join
		nick = self.data["nick"]

		a = "hello {}".format(nick)
		b = "hi {}".format(nick)
		c = "hey {}".format(nick)
		d = "hi yo {}".format(nick)
		e = "hey yo {}".format(nick)
		f = "{}!".format(nick)

		with open("record/join.txt","r") as fp:
			time.sleep(0.25)
			jn = fp.readlines()

			if nick + n in jn:
				with open("record/back/" + nick + ".txt","r") as fpp:
					ck = fpp.read()

					# 如果欢迎语被重置了
					if ck == "":
						ws.send(sendd(random.choice([d,e,f])))

					else:
						ws.send(sendd(ck))
						fp.close()
						fpp.close()

			# 如果此用户来过聊天频道
			elif nick in jo:
				ws.send(sendd(random.choice([d,e,f])))

			else:
				# 昵称是第一次出现
				ws.send(sendd(random.choice([a,b,c,f])))
				jo.append(nick)
		

	def onlineset(self):
		pass


class main:
	def __init__(self,room,name,pas):

		# 设定部分
		self.runbox = runbox(room,name,pas)
		self.room = self.runbox.room
		self.name = self.runbox.name
		self.pas = self.runbox.pas
		

	def on_message(self,ws,message):

		# 获取文本信息
		n = "\n"
		js = json.loads(message)
		self.runbox.handle(js)


		# 如果有人说话
		if js["cmd"] == "chat":
			a = n + js["nick"] + "：" + js["text"]
			print(a + n)


		# 向hack.chat自动回复消息
		if js["cmd"] == "onlineSet":
			onlineuser = "Onlineuser:"
			for e in js["nicks"]:
				if e != js["nicks"][-1]:
					onlineuser = onlineuser + e + ","

				else:
					onlineuser = onlineuser + e


	def on_error(self,ws,error):
		pass
	

	def on_close(self,ws):
		pass
	

	def on_open(self,ws):

		# 连接上服务器了则调用
		a = json.dumps({"cmd":"join","channel":str(self.room),"nick":str(self.name),"password":str(self.pas)})
		hi = random.choice(["hello","hi","hey","hi yo","hey yo"])
		ws.send(a)
		ws.send(sendd("/color ffffff"))
		time.sleep(0.25)
		ws.send(sendd(hi + " this is " + self.name))
		time.sleep(0.5)
		ws.send(sendd("想了解更多玩法 请输入「功能」 我的主人喜欢49哟"))


if __name__ == "__main__":

	# 设定频道、bot名称、bot密码
	xq = "xq102210"
	cn = "chinese"
	yc = "your-channel"
	ycl = "your-channell"
	cc ="公共聊天室"
	mm ="49yyds"

	main = main(room = cn,name = "wine_Corpsebot",pas = "49")

	# 连接聊天室
	hc = "wss://hack.chat/chat-ws"
	hl = "ws://xq.kzw.ink:6060"
	cc = "wss://ws.crosst.chat:35197"
	websocket.enableTrace(True)
	ws = websocket.WebSocketApp(hc,on_message = main.on_message,on_error = main.on_error,on_close = main.on_close)
	ws.on_open = main.on_open 
	ws.run_forever()
