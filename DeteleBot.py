import websocket
import requests
import json
import time
import random
import re
import calendar
try:
	import thread
except:
	import _thread as thread

def sendd(text):
	return json.dumps({"cmd":"chat","text":str(text)})
	
def fanyi(strr):
	data = {"doctype":"json","type":"AUTO","i":str(strr)}
	headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"}
	url = "http://fanyi.youdao.com/translate"
	try:
		r = requests.get(url,params = data,headers = headers,timeout = 10)
		if r.status_code == 200:
			result = r.json()
			resultt = result["translateResult"][0][0]["tgt"]
			return resultt

	except:
		pass
	
class runbox:
	def __init__(self,room,name):
		self.room = room
		self.name = name
		self.online_users = []
		self.afk_list = []
		self.roll_list = []
		self.tui_list = []
		self.join_list = []
		self.friend_list = []
	
	def handle(self,json_data):
		self.json_data = json_data
		if "cmd" in self.json_data:
			if self.json_data["cmd"] == "chat":
				self.chat()

			elif self.json_data["cmd"] == "onlineAdd":
				self.onlineadd()

			elif self.json_data["cmd"] == "onlineSet":
				self.onlineset()

			else:
				pass

	def chat(self):
		qq = [">3",":)",":(",":O",":o",":D","¬_¬","-_-","-.-","-︵-","—.—","—︵—","⌒-⌒","￣︶￣","￣⌒￣","￣ˇ￣","u.u","u_u","n_n","n.n"]
		pp = ["._.","。_。","。.。","°-°","°⌒°","°▽°","°O°","°︶°","°～°","°ˇ°","o.o","o︵o","O.O","OuO","O︵O","0.0","0u0","0︵0"]
		m1 = random.choice(qq)
		m2 = random.choice(pp)
		meme = random.choice([m1,m2])
		chat = time.strftime("%Y-%m-%d")
		room = self.room
		b = chat + " " + room + ".txt"
		with open(b,"a+") as fp:
			a = time.strftime("%H:%M:%S",time.localtime())
			ms = a + " " + self.json_data["nick"] + "\n" + self.json_data["text"] + "\n\n"
			fp.write(ms)

		if self.json_data["text"] in ["功能","order"]:
			a = "·\n基本：功能/order；帮助/help；涩图/acg；头像/head；壁纸/cutie；音乐/music\n"
			b = "日历/cal；农历/date；表情/meme；颜色/color；时间/time；随机/roll；挂机/afk；翻译/fan\n"
			c = "·\n其他：一言；励志；抽签；笑话；情话；古诗词；彩虹屁；毒鸡汤；今日曰\n"
			d = "舔狗日记；社会语录；历史今天；网易热评；摸鱼日历；今日世界\n"
			e = "·\n无聊专用：推荐/tui；树洞/tree；趣站/site；游戏/game；网盘/pan；聊天室/chat\n"
			f = "·\n不会使用？试试在聊天框里发送上面的命令吧"
			time.sleep(0.25)
			ws.send(sendd(a + b + c + d + e + f))

		if self.json_data["text"] in ["帮助","help"]:
			a = "·\nhc指令：https://tieba.baidu.com/p/6833224084\n"
			b = "hc百科：https://chumo.sbsbsb.sbs/wiki\n"
			c = "hc同人作品集：https://note.ms/HCworks111"
			time.sleep(0.25)
			ws.send(sendd(a + b + c))

		if self.json_data["text"] in ["翻译","fan"]:
			time.sleep(0.25)
			ws.send(sendd("·\n使用源：网易有道翻译\n使用方法：·要翻译的句子（前面有个点"))

		if self.json_data["text"] in ["重置","clear"]:
			self.roll_list.clear()
			self.tui_list.clear()
			time.sleep(0.25)
			ws.send(sendd("已清空所有记录"))

		if len(self.roll_list) == 10:
			self.roll_list.clear()
			time.sleep(0.5)
			ws.send(sendd("已自动清空推荐记录"))

		if len(self.tui_list) == 10:
			self.tui_list.clear()
			time.sleep(0.5)
			ws.send(sendd("已自动清空随机记录"))

		if self.json_data["text"] in ["推荐","tui"]:
			c1 = "「Gun Gale Online」\n类型：日本动漫 轻小说 日本漫画\n标签：游戏 战斗 反差萌"
			c2 = "「间谍教室」\n类型：轻小说 日本漫画\n标签：推理 欢乐向 斗智斗勇"
			c3 = "「不知我的死亡Flag将于何处停止」\n类型：日本漫画\n标签：转生 拆旗 事业流"
			c4 = "「杀戮天使」\n类型：游戏 日本动漫 轻小说 日本漫画\n标签：悬疑 治愈 靠谱"
			c5 = "「尸体派对」\n类型：游戏 日本动漫 日本漫画\n标签：恐怖 猎奇 前方高能"
			c6 = "「舞铲幼女与魔眼王」\n类型：轻小说 日本漫画\n标签：萝莉 冒险 携手战斗"
			c7 = "「绯红魔导书」\n类型：日本漫画\n标签：百合 战斗 黑暗风"
			c8 = "「幸色的一居室」\n类型：日剧 日本漫画\n标签：诱拐犯 爱情 治愈"
			c9 = "「来自深渊」\n类型：日本动漫 日本漫画\n标签：冒险 毛茸茸 黑暗风"
			c10 = "「最终休止符 -无止境的螺旋物语-」\n类型：游戏 日本动漫\n标签：冒险 萌系 欢乐向"
			c11 = "「婚约者恋上我的妹妹」\n类型：轻小说 日本漫画\n标签：致郁 轮回 爱而不得"
			c12 = "「老师温柔的杀人方法」\n类型：日本漫画\n标签：爱情 悬疑 杀人推理"
			c13 = "「最弱的驯养师开启的捡垃圾的旅途」\n类型：轻小说 日本漫画\n标签：萝莉 冒险 治愈"
			c14 = "「童话大逃杀」\n类型：日本漫画\n标签：冒险 童话风 黑暗风"
			c15 = "「大海原与大海原」\n类型：日本漫画\n标签：冒险 治愈"
			c15 = "「神不在的星期天」\n类型：日本动漫 轻小说 日本漫画\n标签：成长 冒险 治愈"
			c16 = "「纳尼亚传奇：魔法师的外甥」\n类型：名著 日本漫画\n标签：穿越 冒险 经典作品"
			c17 = "「中之人基因组」\n类型：日本动漫 日本漫画\n标签：冒险 多主角 实况中"
			c18 = "「喜欢的不是女儿，而是我吗！？」\n类型：轻小说 日本漫画\n标签：日常 年龄差 恋爱喜剧"
			c19 = "「从零开始的魔法书」\n类型：日本动漫 轻小说 日本漫画\n标签：兽人 冒险 美少女"
			c20 = "「落后的驯兽师慢生活」\n类型：轻小说 日本漫画\n标签：正太 游戏 种田"
			c21 = "「厄里斯的圣杯」\n类型：轻小说 日本漫画\n标签：推理 恶役 种田"
			c22 = "「葬送的芙莉莲」\n类型：日本漫画\n标签：冒险 魔法 感人泪下"
			c23 = "「转生成蜘蛛又怎样！」\n类型：日本动漫 轻小说 日本漫画\n标签：转生 蜘蛛子 双主线"
			c24 = "「最近，妹妹的样子有点怪？」\n类型：日剧 日本动漫 日本漫画\n标签：骨科 日常 恋爱喜剧"
			c25 = "「无能的奈奈」\n类型：日本动漫 日本漫画\n标签：悬疑 校园 斗智斗勇"
			c26 = "「灾祸的真理」\n类型：游戏 日本动漫 日本漫画\n标签：悬疑 战斗 剧情紧凑"
			c27 = "「LOST SONG」\n类型：日本动漫\n标签：治愈 冷门向 音乐作"
			c28 = "「败犬女主也太多了！」\n类型：轻小说\n标签：脑洞 败犬故事 恋爱喜剧"
			c29 = "「因为太怕痛就全点防御力了」\n类型：日本动漫 轻小说 日本漫画\n标签：游戏 冒险 凤傲天"
			c30 = "「罪恶王冠」\n类型：日本动漫\n标签：悬疑 战斗 幻想"
			c31 = "「来自多彩世界的明天」\n类型：日本动漫\n标签：成长 治愈 感人泪下"
			c32 = "「关于我转生变成史莱姆这档事」\n类型：游戏 日本动漫 轻小说\n标签：冒险 史莱姆 欢乐向"
			c33 = "「社会我鸡哥，人狠话不多」\n类型：日本漫画\n标签：战斗 主角鸡 核氢核锂"
			c34 = "「犬与屑」\n类型：日本漫画\n标签：悬疑 伦理 黑暗风"
			c35 = "「学园孤岛」\n类型：日本动漫 日本漫画\n标签：悬疑 治愈 擦眼泪"
			c36 = "「凹凸魔女的母女故事」\n类型：日本漫画\n标签：百合 日常 欢乐向"
			c37 = "「猪肝热热吃」\n类型：轻小说 日本漫画\n标签：主角猪 美少女 冒险"
			c38 = "「即使世界毁灭每一天依然快乐」\n类型：日本漫画\n标签：末世 治愈 毛茸茸"
			c39 = "「转生魔女宣告灭亡」\n类型：日本漫画\n标签：少女 爱情 魔法"
			c40 = "「骨龙的宝贝」\n类型：日本漫画\n标签：冒险 颜艺 养女儿"
			c41 = "「雾雨飘散之森」\n类型：游戏 日本漫画\n标签：悬疑 冒险 解谜游戏"
			c42 = "「女王陛下的异世界战略」\n类型：轻小说 日本漫画\n标签：虫族 战斗 猎奇"
			c43 = "「魔女之家：艾莲日记」\n类型：游戏 轻小说 日本漫画\n标签：恐怖 致郁 解谜游戏"
			c44 = "「恶魔的谜语」\n类型：日本动漫 日本漫画\n标签：百合 战斗 暗杀"
			c45 = "「魔女的心脏」\n类型：日本漫画\n标签：少女 治愈 旅行途中"
			c46 = "「魔法少女site」\n类型：日本动漫 日本漫画\n标签：百合 黑暗风 魔法少女"
			c47 = "「我推的孩子」\n类型：日本漫画\n标签：偶像 转生 误会系"
			c48 = "「转生成为魔剑」\n类型：轻小说 日本漫画\n标签：主角剑 养女儿 战斗"
			c49 = "「沉默的魔女」\n类型：轻小说\n标签：少女 推理 魔法"
			c50 = "「BNA」\n类型：日本动漫 轻小说\n标签：冒险 治愈 视觉系"
			c51 = "「约定的梦幻岛」\n类型：日本动漫 轻小说 日本漫画\n标签：悬疑 致郁 逃生"
			c52 = "「在魔王城说晚安」\n类型：日本动漫 日本漫画\n标签：治愈 萌系 欢乐向"
			c53 = "「奇诺之旅」\n类型：日本动漫 轻小说 日本漫画\n标签：旅行 冒险 引人深思"
			c54 = "「烧开水勇者的复仇记」\n类型：日本漫画\n标签：百合 复仇 携手战斗"
			c55 = "「恶魔战线」\n类型：日本动漫 日本漫画\n标签：爱情 悬疑 吸血鬼"
			c56 = "「该死的告白日」\n类型：韩国漫画\n标签：悬疑 感人 前方高能"
			c57 = "「开局一条鲲」\n类型：中国漫画\n标签：玄幻 冒险 双女主"
			c58 = "「花非花」\n类型：中国漫画\n标签：帝王 养成 古风"
			c59 = "「血族Bloodline」\n类型：游戏 中国漫画\n标签：年代 战斗 吸血鬼"
			c60 = "「血族维他命」\n类型：中国漫画\n标签：年代 恋爱 吸血鬼"
			w1 = "「宿命回响」\n类型：游戏 日本动漫\n标签：剧情 音乐 奇幻\n地址：https://movie.douban.com/subject/35417875"
			w2 = "「我要成为双马尾」\n类型：日本动漫 轻小说\n标签：剧情 性转 美少女\n地址：https://movie.douban.com/subject/25793397"
			w3 = "「巨龙山谷」\n剧情：意识流\n建模：堪称「极致美学」\n备注：千万别看，你会猝死。啊啊啊，我要犭"
			w4 = "「刺客信条：王朝」\n类型：游戏 中国漫画\n标签：冒险 历史 武侠\n推荐：L"
			j1 = "\n地址：https://movie.douban.com/subject/35296324"
			j2 = "\n·\n你看看，我看看\n大家一起去阴间\n白内障，脑血栓\n全都给我得一遍\n草起来了，蚌埠住了\n你来看，我来看\n阴间的路会变短"
			j3 = "\n编曲：蜜雪冰城\n推荐/填词：ww"
			aa = random.choice([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20])
			bb = random.choice([c21,c22,c23,c24,c25,c26,c27,c28,c29,c30,c31,c32,c33,c34,c35,c36,c37,c38,c39,c40])
			cc = random.choice([c41,c42,c43,c44,c45,c46,c47,c48,c49,c50,c51,c52,c53,c54,c55,c56,c57,c58,c59,c60])
			c = "·\n" + random.choice([aa,bb,cc]) + "\n推荐：ee"
			w = "·\n" + random.choice([w1+"\n推荐：ww",w2+"\n推荐：ww",w3+j1+j2+j3,w4])
			wuhu = random.choice([c,w])

			if c in self.roll_list and w in self.roll_list:
				time.sleep(0.25)
				ws.send(sendd("诶诶诶 {}中奖了 再试一次吧".format(self.json_data["nick"])))

			elif c in self.roll_list:
				time.sleep(0.25)
				ws.send(sendd(w))
				self.roll_list.append(w)

			elif w in self.roll_list:
				time.sleep(0.25)
				ws.send(sendd(c))
				self.roll_list.append(c)

			else:
				time.sleep(0.55)
				ws.send(sendd(wuhu))
				self.roll_list.append(wuhu)

		if self.json_data["text"] in ["树洞","tree"]:
			f0 = random.choice(["13和ee的轻小说屋 old\nhttps://lidualhistory.mysxl.cn","JSH的主页\nhttps://jshang.cf"])
			f1 = random.choice(["flaugh的个人博客\nhttps://xsdboke.mysxl.cn","Sprinkle博客\nhttps://pntang.github.io"])
			f2 = random.choice(["Detele的GitHub\nhttps://github.com/Detele-Detele/Detele","贤者13的树洞\nhttps://sage-thirteen.mysxl.cn"])
			f3 = random.choice(["Bird's Page\nhttps://fuckbird.sbsbsb.sbs","Beluga's YouTube\nhttps://youtube.com/c/Beluga1"])
			f4 = random.choice(["MuRongPIG's GitHub\nhttps://github.com/MuRongPIG","朽木自雕\nhttp://blog.noxx.cn"])
			f5 = random.choice(["纸片君ee的个人主页\nhttps://paperee.tk","13和ee的小说屋 new\nhttps://novelhouse.mysxl.cn"])
			f = "·\n" + random.choice([f0,f1,f2,f3,f4,f5])
			if f in self.tui_list:
				time.sleep(0.25)
				ws.send(sendd("嘿嘿～eebot偷懒了"))
				
			else:
				time.sleep(0.25)
				ws.send(sendd(f))
				self.tui_list.append(f)

		if self.json_data["text"] in ["趣站","site"]:
			s0 = random.choice(["ISS Docking Simulator\nhttps://iss-sim.spacex.com","STROBE\nhttps://strobe.cool"])
			s1 = random.choice(["Form Follows Function\nhttp://fff.cmiscm.com","In Pieces\nhttp://species-in-pieces.com"])
			s2 = random.choice(["Chrome Music Lab\nhttps://musiclab.chromeexperiments.com/Song-Maker","Calm\nhttps://calm.ovh"])
			s3 = random.choice(["Staggering Beauty\nhttp://www.staggeringbeauty.com","Mikutap\nhttps://aidn.jp/mikutap"])
			s4 = random.choice(["Koalas to the Max dot Com\nhttp://koalastothemax.com","OREOOO\nhttp://ljl.li/oreooo"])
			s5 = random.choice(["即刻到账\nhttps://saythemoney.github.io","Microsculpture\nhttp://microsculpture.net"])
			s6 = random.choice(["我爱工作\nhttps://ilove.works","卡巴斯基网络威胁实时地图\nhttps://cybermap.kaspersky.com/cn"])
			s7 = random.choice(["Yoichi Kobayashi\nhttps://www.tplh.net","跳跃的小球\nhttp://guozhivip.com/fun"])
			s8 = random.choice(["今天吃啥呀\nhttp://guozhivip.com/eat","便携小空调\nhttps://ac.yunyoujun.cn"])
			s9 = random.choice(["The Zen Zone\nhttps://thezen.zone","网页小游戏列表\nhttps://xingye.me/game"])
			s10 = random.choice(["Bruno Simon\nhttps://bruno-simon.com","Coding Cat\nhttps://hostrider.com"])
			s11 = random.choice(["架子鼓\nhttp://guozhivip.com/jzg","Nomadic Tribe\nhttps://2019.makemepulse.com"])
			s12 = random.choice(["The Blocks\nhttps://blocks.ovh","Sequencer64\nhttps://www.sequencer64.com"])
			s13 = random.choice(["Bubble wrap pop\nhttps://bubblespop.netlify.app","Sharkle\nhttps://sharkle.com"])
			s14 = random.choice(["Kick Ass\nhttps://kickassapp.com","Patatap\nhttps://www.patatap.com"])
			s15 = random.choice(["星弈小游戏平台\nhttp://other.noxx.cn/play","全景故宫\nhttps://pano.dpm.org.cn"])
			s = "·\n" + random.choice([s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15])
			if s in self.tui_list:
				time.sleep(0.25)
				ws.send(sendd("不给不给 就是不给{}".format(self.json_data["nick"])))

			else:
				time.sleep(0.25)
				ws.send(sendd(s))
				self.tui_list.append(s)

		if self.json_data["text"] in ["游戏","game"]:
			g0 = random.choice(["Phigros\nhttps://pgr.han-han.xyz/tapToStart","defly\nhttps://defly.io"])
			g1 = random.choice(["和焦虑一起冒险\nhttps://z-lyen.github.io/anxiety","RICHUP\nhttps://richup.io"])
			g2 = random.choice(["Red Carpet Rampage\nhttps://rcr.heheda.top","Raaaaft\nhttps://raaaaft.io"])
			g3 = random.choice(["名字竞技场\nhttp://namerena.github.io","Nazo Game\nhttps://nazo.one-story.cn"])
			g4 = random.choice(["HTML5 杯\nhttp://html5cup.kayac.com","株式会社 闇\nhttps://death.co.jp/ja/pc"])
			g5 = random.choice(["Line Rider\nhttps://www.linerider.com","Dino Swords\nhttps://dinoswords.gg"])
			g6 = random.choice(["信任的进化\nhttps://dccxi.com/trust","2020 Game\nhttps://2020game.io"])
			g7 = random.choice(["Minecraft Classic\nhttps://classic.minecraft.net","Gartic\nhttps://gartic.io"])
			g8 = random.choice(["YORG\nhttps://yorg.io","我们变成了我们所看到的\nhttps://claycoffee.github.io/wbwwb"])
			g9 = random.choice(["西游梗传\nhttp://littlegame.tomato123.cn/xiyou","太鼓ウェブ\nhttps://taiko.bui.pm"])
			g10 = random.choice(["florr\nhttps://florr.io","人生重开模拟器\nhttp://liferestart.syaro.io/public"])
			g11 = random.choice(["Taming\nhttps://taming.io","ふぁんしーあいらんど\nhttp://lomando.com/main.html"])
			g12 = random.choice(["Manyland\nhttp://manyland.com","Undercards\nhttps://undercards.net/Quests"])
			g13 = random.choice(["Minecraft 网页版\nhttps://craft.spr233.eu.org/"])
			g = "·\n" + random.choice([g0,g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12,g13])
			if g in self.tui_list:
				time.sleep(0.25)
				ws.send(sendd("哼 不给 不可以贪心哦～"))

			else:
				time.sleep(0.25)
				ws.send(sendd(g))
				self.tui_list.append(g)

		if self.json_data["text"] in ["网盘","pan"]:
			p0 = random.choice(["勿待炬火网盘\nhttps://pan.weunite.top","樱忆云盘\nhttps://drive.loili.com"])
			p1 = random.choice(["雨滴云盘\nhttp://pan.handanxiaochipeixun.top:5212","AcgngameCloud\nhttps://acgngame.cloud"])
			p2 = random.choice(["Cloudreve\nhttps://cloudreve.zjh336.cn","爱丽丝的记事本\nhttps://drive.noire.cc"])
			p3 = random.choice(["小太阳云存储\nhttps://cncncloud.com","比邻云盘\nhttps://pan.bilnn.cn"])
			p4 = random.choice(["萌云\nhttps://moecloud.cn","AnonFiles\nhttps://anonfiles.com"])
			p5 = random.choice(["文叔叔\nhttps://www.wenshushu.cn","TMP.link\nhttps://app.tmp.link"])
			p = "·\n" + random.choice([p0,p1,p2,p3,p4,p5])
			if p in self.tui_list:
				time.sleep(0.25)
				ws.send(sendd("eebot企图让{}再试一次".format(self.json_data["nick"])))

			else:
				time.sleep(0.25)
				ws.send(sendd(p))
				self.tui_list.append(p)

		if self.json_data["text"] in ["聊天室","chat"]:
			h0 = random.choice(["hack.chat\nhttps://hack.chat","小蝌蚪互动聊天室\nhttp://zzzgd.info/kedou"])
			h1 = random.choice(["BBBUG 聊天室\nhttp://chat.zzzgd.info","星弈微聊\nhttps://im.noxx.cn"])
			h2 = random.choice(["蔷薇花园\nhttps://iirose.com","爱聊友\nhttps://im.ailyoo.com"])
			h3 = random.choice(["网页聊天\nhttps://wylt.com/r/XianLiao","十字街\nhttps://crosst.chat"])
			h4 = random.choice(["DOLLARS 聊天室\nhttps://drrr.com","hichat\nhttp://hichat.herokuapp.com"])
			h5 = random.choice(["BBBUG 音乐聊天室\nhttps://bbbug.com","多人听歌网\nhttps://chat.zhuolin.wang"])
			h6 = random.choice(["在线聊天\nhttps://chat.anonshacker.com/Mars","聊乎\nhttps://www.randomchat.cn"])
			h7 = random.choice(["匿名聊天室\nhttps://easonchiang7178.github.io/f2e-anonymous-chatroom","TALK2\nhttps://talk2.fun"])
			h8 = random.choice(["啊噗聊天\nhttps://www.uplt.com","fiora\nhttps://fiora.suisuijiang.com"])
			h9 = random.choice(["叔叔不约\nhttp://www.shushubuyue.com","Deskry\nhttp://v6.nm1v1.cn"])
			h10 = random.choice(["Liveany\nhttps://www.liveany.com/web.html","CamSurf\nhttps://camsurf.com"])
			h11 = random.choice(["WooTalk\nhttps://wootalk.today","陌路人\nhttp://www.moluren.net"])
			h12 = random.choice(["Anonymous\nhttps://chat42.online","MeeTunnel\nhttps://www.meetunnel.com/chat"])
			h = "·\n" + random.choice([h0,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12])
			if h in self.tui_list:
				time.sleep(0.25)
				ws.send(sendd("耶 eebot不告诉{}".format(self.json_data["nick"])))

			else:
				time.sleep(0.25)
				ws.send(sendd(h))
				self.tui_list.append(h)

		if self.json_data["text"] in ["一言"]:
			api = "https://v1.hitokoto.cn"
			response = requests.get(api)
			res = response.json()
			word = res["from"] + " " + res["creator"] + "\n「" + res["hitokoto"] + "」"
			apii = "https://api.muxiaoguo.cn/api/yiyan"
			responsee = requests.get(apii)
			ress = responsee.json()
			a = ress["data"]
			wordd = "「" + a["content"] + "」"
			apiii = "https://api.vvhan.com/api/ian"
			responseee = requests.get(apiii)
			resss = "「" + responseee.text + "」"
			time.sleep(0.25)
			ws.send(sendd(random.choice([word,wordd,resss])))

		if self.json_data["text"] in ["励志"]:
			api = "http://api.botwl.cn/api/yhyl"
			response = requests.get(api)
			res = "「" + response.text + "」"
			time.sleep(0.25)
			ws.send(sendd(res))

		if self.json_data["text"] in ["抽签"]:
			api = "http://api.botwl.cn/api/qiuqian"
			response = requests.get(api)
			res = response.text.replace('[\\n]','\n')
			time.sleep(0.25)
			ws.send(sendd(res))

		if self.json_data["text"] in ["笑话"]:
			api = "https://api.muxiaoguo.cn/api/xiaohua"
			response = requests.get(api)
			res = response.json()
			a = res["data"]
			word = a["title"] + "\n" + a["content"]
			apii = "https://api.vvhan.com/api/xh"
			responsee = requests.get(apii)
			ress = responsee.text
			time.sleep(0.25)
			ws.send(sendd(random.choice([word,ress])))

		if self.json_data["text"] in ["情话"]:
			api = "https://api.lovelive.tools/api/SweetNothings/count/Serialization/serializationType"
			response = requests.get(api)
			res = response.json()
			word = res["returnObj"]
			a = "「" + random.choice(word) + "」"
			apii = "https://api.vvhan.com/api/sao"
			responsee = requests.get(apii)
			ress = "「" + responsee.text + "」"
			apiii = "https://api.vvhan.com/api/love"
			responseee = requests.get(apiii)
			resss = "「" + responseee.text + "」"
			time.sleep(0.25)
			ws.send(sendd(random.choice([a,ress,resss])))

		if self.json_data["text"] in ["古诗词"]:
			api = "https://api.muxiaoguo.cn/api/Gushici"
			response = requests.get(api)
			res = response.json()
			a = res["data"]
			word = a["title"] + " " + a["author"] + "\n「" + a["min_content"] + "」"
			time.sleep(0.25)
			ws.send(sendd(word))

		if self.json_data["text"] in ["彩虹屁"]:
			api = "https://api.muxiaoguo.cn/api/caihongpi"
			response = requests.get(api)
			res = response.json()
			a = res["data"]
			word = "「" + a["comment"] + "」"
			time.sleep(0.25)
			ws.send(sendd(word))

		if self.json_data["text"] in ["毒鸡汤"]:
			api = "https://api.muxiaoguo.cn/api/dujitang"
			response = requests.get(api)
			res = response.json()
			a = res["data"]
			word = "「" + a["comment"] + "」"
			apii = "http://api.btstu.cn/yan/api.php"
			responsee = requests.get(apii)
			ress = "「" + responsee.text + "」"
			time.sleep(0.25)
			ws.send(sendd(random.choice([word,ress])))

		if self.json_data["text"] in ["今日曰"]:
			api = "https://api.vvhan.com/api/en"
			response = requests.get(api)
			res = response.json()
			a = res["data"]
			b = "Today Is " + a["month"] + " " + a["day"]
			word = b + "\n「" + a["zh"] + "」" + "\n「" + a["en"] + "」"
			time.sleep(0.25)
			ws.send(sendd(word))

		if self.json_data["text"] in ["舔狗日记"]:
			api = "https://api.ixiaowai.cn/tgrj/index.php"
			response = requests.get(api)
			res = "「" + response.text + "」"
			apii = "https://api.muxiaoguo.cn/api/tiangourj"
			responsee = requests.get(apii)
			ress = responsee.json()
			a = ress["data"]
			word = "「" + a["comment"] + "」"
			time.sleep(0.25)
			ws.send(sendd(random.choice([res,word])))

		if self.json_data["text"] in ["社会语录"]:
			api = "https://api.oick.cn/yulu/api.php"
			response = requests.get(api)
			res = response.text.replace('\"','')
			word = "「" + res + "」"
			time.sleep(0.25)
			ws.send(sendd(word))

		if self.json_data["text"] in ["历史今天"]:
			api = "https://qqlykm.cn/api/lishi/index.php"
			response = requests.get(api)
			res = "「" + response.text + "」"
			time.sleep(0.25)
			ws.send(sendd(res))

		if self.json_data["text"] in ["网易热评"]:
			api = "https://api.muxiaoguo.cn/api/163reping"
			response = requests.get(api)
			res = response.json()
			a = res["data"]
			word = "来自 " + a["nickname"] + a["songName"] + "：\n「" + a["content"] + "」"
			time.sleep(0.25)
			ws.send(sendd(word))

		if self.json_data["text"] in ["摸鱼日历"]:
			api = "https://api.vvhan.com/api/moyu"
			response = requests.get(api)
			res = response.url
			time.sleep(0.25)
			ws.send(sendd(res))

		if self.json_data["text"] in ["今日世界"]:
			time.sleep(0.25)
			ws.send(sendd("https://api.vvhan.com/api/60s"))

		if self.json_data["text"] in ["涩图","acg"]:
			api = "http://api.btstu.cn/sjbz/api.php?lx=dongman&format=images"
			response = requests.get(api)
			res = response.url
			apii = "http://api.btstu.cn/sjbz/api.php?method=mobile&lx=dongman&format=images"
			responsee = requests.get(apii)
			ress = responsee.url
			apiii = "https://api.ixiaowai.cn/mcapi/mcapi.php"
			responseee = requests.get(apiii)
			resss = responseee.url
			time.sleep(0.25)
			ws.send(sendd(random.choice([res,ress,resss])))

		if self.json_data["text"] in ["头像","head"]:
			api = "http://api.btstu.cn/sjtx/api.php"
			response = requests.get(api)
			res = response.url
			apii = "https://api.muxiaoguo.cn/api/sjtx?method=pc"
			responsee = requests.get(apii)
			ress = responsee.json()
			a = ress["data"]
			word = a["imgurl"]
			time.sleep(0.25)
			ws.send(sendd(random.choice([res,word])))

		if self.json_data["text"] in ["壁纸","cutie"]:
			api = "https://cdn.seovx.com/ha/?mom=302"
			response = requests.get(api)
			res = response.url
			apii = "https://cdn.seovx.com/?mom=302"
			responsee = requests.get(apii)
			ress = responsee.url
			time.sleep(0.25)
			ws.send(sendd(random.choice([res,ress])))

		if self.json_data["text"] in ["音乐","music"]:
			api = "https://api.paugram.com/acgm"
			response = requests.get(api)
			res = response.json()
			word = res["title"] + " " + res["artist"] + " " + str(res["id"]) + "\n" + res["link"]
			time.sleep(0.25)
			ws.send(sendd(word))

		if self.json_data["text"] in ["日历","cal"]:
			a = time.strftime("%Y")
			b = time.strftime("%m")
			cal = calendar.month(int(a), int(b)).replace(' ','⠀').replace('⠀⠀',' ⠀')
			time.sleep(0.25)
			ws.send(sendd("⠀" + cal))

		if self.json_data["text"] in ["农历","date"]:
			api = "https://api.muxiaoguo.cn/api/yinlongli"
			response = requests.get(api)
			res = response.json()
			a = res["data"]
			word = a["lunar"] + " " + a["yearZodiac"] + " " + a["lunarYearName"] + " " + a["solarTerms"]
			apii = "http://api.botwl.cn/api/nl"
			responsee = requests.get(apii)
			ress = responsee.text.replace('\n',' ').replace('今天是','').replace('节气：','')
			time.sleep(0.25)
			ws.send(sendd(random.choice([word,ress])))

		if self.json_data["text"] in ["表情","meme"]:
			time.sleep(0.25)
			ws.send(sendd(meme))

		if self.json_data["text"] in ["颜色","color"]:
			# https://api.vvhan.com/api/color
			api = "http://api.botwl.cn/api/sjys"
			response = requests.get(api)
			a = "/color " + response.text
			time.sleep(0.25)
			ws.send(sendd(a))
			ws.send(sendd(response.text))
			ws.send(sendd("/color 44FF00"))

		if self.json_data["text"] in ["时间","time"]:
			a = time.strftime("TIME %Y-%m-%d %H:%M:%S %a %b",time.localtime())
			time.sleep(0.25)
			ws.send(sendd(a))

		if self.json_data["text"] in ["随机","roll"]:
			time.sleep(0.25)
			ws.send(sendd(random.randint(1,999)))

		if self.json_data["nick"] in self.afk_list and self.json_data["text"] not in ["挂机","afk","挂机列表","list"]:
			a = "welcome back {}".format(self.json_data["nick"])
			b = "{} is back".format(self.json_data["nick"])
			time.sleep(0.25)
			ws.send(sendd(random.choice([a,b])))
			del self.afk_list[self.afk_list.index(self.json_data["nick"])]

		if self.json_data["nick"] in self.afk_list and self.json_data["text"] in ["挂机","afk"]:
			time.sleep(0.25)
			ws.send(sendd("{} is already in afk list".format(self.json_data["nick"])))
			
		if self.json_data["nick"] not in self.afk_list and self.json_data["text"] in ["挂机","afk"]:
			time.sleep(0.25)
			ws.send(sendd("{} is now afk".format(self.json_data["nick"])))
			self.afk_list.append(self.json_data["nick"])
			
		if self.json_data["text"] in ["挂机列表","list"]:
			if len(self.afk_list) == 0:
				time.sleep(0.25)
				ws.send(sendd("目前无人挂机 列表为空"))

			else:
				time.sleep(0.25)
				ws.send(sendd(self.afk_list).replace('[\'','').replace('\']','').replace('\'',' '))
			
		if re.findall(r"·.+$",self.json_data["text"]) != []:
			time.sleep(0.25)
			ws.send(sendd("{} said: ".format(self.json_data["nick"]) + fanyi(re.findall(r"·(.+)$",self.json_data["text"])[0])))

		if self.json_data["nick"] not in ["eebot","eeebot","eeeebot"]:
			a1 = "eebot！耶！"
			a2 = "好像听到了有人callme呢"
			a3 = "诶？{}有事吗？".format(self.json_data["nick"])
			a4 = "{}去找主人ee玩吧".format(self.json_data["nick"])
			a = random.choice([a1,a2,a3,a4])
			b1 = "/me 摸了摸{}的头".format(self.json_data["nick"])
			b2 = "/me 哇的一声扑向{}".format(self.json_data["nick"])
			b3 = "/me 戳了戳{}".format(self.json_data["nick"])
			b4 = "/me 拉着{}的衣角".format(self.json_data["nick"])
			b5 = "/me 靠在{}身边".format(self.json_data["nick"])
			b6 = "/me 歪着头看{}".format(self.json_data["nick"])
			b7 = "/me 呆呆望着{}".format(self.json_data["nick"])
			b8 = "/me 将{}加入了好友名单".format(self.json_data["nick"])
			b9 = "/me 拖住了{}".format(self.json_data["nick"])
			b10 = "/me 偷偷盯着{}".format(self.json_data["nick"])
			b11 = "/me 向{}要抱抱".format(self.json_data["nick"])
			b12 = "/me 向{}要举高高".format(self.json_data["nick"])
			b = random.choice([b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12])
			c1 = "/me 高调经过"
			c2 = "/me 低调路过"
			c3 = "/me bilibili"
			c4 = "/me 打个招呼"
			c5 = "/me 柠檬酸了"
			c6 = "/me orzorzorz"
			c7 = "/me azazazaz"
			c8 = "/me wuhuwuhuh"
			c = random.choice([c1,c2,c3,c4])
			d1 = "/me ！？"
			d2 = "/me 窥屏中"
			d3 = "/me 躺平中"
			d4 = "/me 瞪大了双眼"
			d5 = "/me 默默竖起大拇指"
			d6 = "/me 死死盯着屏幕"
			d7 = "/me 突发恶疾"
			d8 = "/me 将作业撕了"
			d9 = "/me 蹲厕所中"
			d = random.choice([d1,d2,d3,d4,d5,d6,d7,d8,d9])
			e1 = "不说话便是最好的回答"
			e2 = "寒冷的空气 瑟瑟发抖"
			e3 = "该说点什么好呢"
			e4 = "来捧场了！"
			e5 = "死亡凝视！"
			e6 = "猎杀时刻！"
			e = random.choice([e1,e2,e3,e4,e5,e6])
			f1 = "eebot才不是复读机呢"
			f2 = "对了 eebot复读的概率在1/2到1/3间"
			f3 = "果然 人类的本质都是复读机"
			f4 = "eebot会复读特定的字段"
			f = random.choice([f1,f2,f3,f4])
			x = ""
			if "eebot" in self.json_data["text"]:
				time.sleep(0.5)
				ws.send(sendd(random.choice([a,c,x])))

			if "（" in self.json_data["text"] or "）" in self.json_data["text"]:
				time.sleep(0.5)
				ws.send(sendd(random.choice([b,d,x])))

			if "《" in self.json_data["text"] and "》" in self.json_data["text"]:
				time.sleep(0.25)
				ws.send(sendd(random.choice([self.json_data["text"],x])))

			if ":" * 1 in self.json_data["text"] or "：" * 1 in self.json_data["text"]:
				if "http" in self.json_data["text"]:
					time.sleep(0.5)
					ws.send(sendd(random.choice([self.json_data["text"],x])))

				else:
					time.sleep(0.5)
				ws.send(sendd(random.choice([b,c,x])))

			if "！" * 1 in self.json_data["text"] or "？" * 1 in self.json_data["text"]:
				time.sleep(0.5)
				ws.send(sendd(random.choice([b,d,x])))

			if "em" * 1 in self.json_data["text"] or "hm" * 1 in self.json_data["text"]:
				time.sleep(0.25)
				ws.send(sendd(random.choice([self.json_data["text"],x])))

			if "复读机" in self.json_data["text"] or "学舌" in self.json_data["text"]:
				time.sleep(0.75)
				self.ws.send(sendd(random.choice([e,f,x])))

			if self.json_data["text"] in ["…","……","。","。。","。。。"]:
				time.sleep(0.5)
				ws.send(sendd(random.choice([e,x])))

			if self.json_data["text"] in qq or self.json_data["text"] in pp:
				time.sleep(0.25)
				ws.send(sendd(random.choice([meme,x])))
	
	def onlineadd(self):
		a = "hi {}".format(self.json_data["nick"])
		b = "hello {}".format(self.json_data["nick"])
		c = "hey {}".format(self.json_data["nick"])
		d = "welcome back {}".format(self.json_data["nick"])
		e = "{} is back".format(self.json_data["nick"])
		if self.json_data["nick"] in self.join_list:
			time.sleep(0.25)
			ws.send(sendd(random.choice([d,e])))

		else:
			time.sleep(0.25)
			ws.send(sendd(random.choice([a,b,c])))
			self.join_list.append(self.json_data["nick"])
		
	def onlineset(self):
		pass
			
class main:
	def __init__(self,room,name):
		self.runbox = runbox(room,name)
		self.room = self.runbox.room
		self.name = self.runbox.name
		
	def on_message(self,ws,message):
		js_ms = json.loads(message)
		self.runbox.handle(js_ms)
		if js_ms["cmd"] == "onlineSet":
			onlineuser = "Onlineuser:"
			for e in js_ms["nicks"]:
				if e != js_ms["nicks"][-1]:
					onlineuser = onlineuser + e + ","
				else:
					onlineuser = onlineuser + e
		
	def on_error(self,ws,error):
		pass
		
	def on_close(self,ws):
		pass
		
	def on_open(self,ws):
		ws.send(json.dumps({"cmd": "join", "channel": str(self.room), "nick": str(self.name)}))
		ws.send(sendd("/color 44FF00"))
		time.sleep(0.25)
		ws.send(sendd("hi (o°ω°o)"))
		time.sleep(0.75)
		ws.send(sendd("想了解更多玩法 请输入：功能"))

if __name__ == "__main__":
	main = main(room="your-channel",name="detelebot#aaa")
	websocket.enableTrace(True)
	ws = websocket.WebSocketApp("wss://hack.chat/chat-ws",on_message=main.on_message,on_error=main.on_error,on_close=main.on_close)
	ws.on_open=main.on_open 
	ws.run_forever()
