#####################引用内置的库####################
import json
import requests
import os
import base64
import random
import time
import re
import protocol
import ast
import eventlet
from threading import Thread
import threading
import jieba
import datetime
import sys
####################引用自定义库####################
sys.path.append("..")
try:
    from . import permissions
except:
    import permissions
from config import web
####################机器人配置######################
########web配置##########
bot_ip=web.bot_ip #机器人ip
bot_http_port=web.bot_http_port#机器人http端口
bot_ws_port=web.bot_ws_port#机器人websocket端口
#########################
blacklist=permissions.blacklist
owner=permissions.owner
bot_http_address=bot_ip+":"+bot_http_port
bot_ws_address=bot_ip+":"+bot_ws_port
print("[*]初始化机器人websocket:",bot_ws_address)
print("[*]初始化机器人http:",bot_http_address)
###################附加函数声明#####################
text_list = []
def split_text(text, length):
    text_list.clear()
    tmp = text[:int(length)]
    # print(tmp)
    # 将固定长度的字符串添加到列表中
    text_list.append(tmp)
    # 将原串替换
    text = text.replace(tmp, '')
    if len(text) < length + 1:
        # 直接添加或者舍弃
        text_list.append(text)
    else:
        split_text(text, length)
    return text_list
def listtostr(list1):
    list2=[str(i) for i in list1]
    strlist="".join(list2)
    return strlist
def remove_upprintable_chars(s):
    """移除所有不可见字符"""
    return ''.join(x for x in s if x.isprintable())
##################API函数化配置#####################
def send_group_msg(group,msg):#发送群消息的函数
    a=requests.get("http://"+bot_http_address+"/send_group_msg?group_id="+str(group)+"&message="+str(msg))
    ans=json.loads(a.text)
    try:
        ans=ans["data"]["message_id"]
    except:
        ans="success"
    print("[*]小淇发送了消息:",msg.encode('utf-8').decode("utf-8","ignore"))
    return ans
def send_private_msg(user,msg):#发送私聊消息的函数
    a=requests.get("http://"+bot_http_address+"/send_private_msg?user_id="+str(user)+"&message="+str(msg))
    ans=json.loads(a.text)
    try:
        ans=ans["data"]["message_id"]
    except:
        ans="success"
    print("[*]小淇发送了消息:",msg.encode('utf-8').decode("utf-8","ignore"))
    return ans
def set_group_name(group_id,group_name):#设置群名的函数
    requests.get("http://"+bot_http_address+"/set_group_name?group_id="+str(group_id)+"&group_name="+str(group_name))
####################功能初始化#######################
def Group_message_processing(group,user,message_id,message):#群消息可用功能
        ####打印获取的内容####
    print("====群聊消息====")
    print("[*]群号:",group,"\n[*]发送者QQ号:",user,"\n[*]消息ID:",message_id,"\n[*]消息内容:",message)
    print("================")
    if str(user) in blacklist:
        pass
    else:
        

        #######功能实现#######
        if message=="菜单":
            print("[*]QQ:"+str(user)+"请求菜单操作")
            txt='''
    ==========
    |||||||菜单||||||||
    ==========
    |1.随机听歌        
    |2.一言            
    |3.精神语录        
    |4.爱情语录     
    |5.翻译            
    |6.计算
    |7.搜搜古诗
    |8.搜搜漫画
    |9.搜搜小说
    |10.编码\解码
    |11.百度百科
    |12.手机号归属地查询
    |13.查查天气
    |14.举牌牌
    |15.点歌
    |16.随机微视
    ==========
    '''
            send_group_msg(group,txt)
            print("[*]成功发送了回复")
    #############################
        if message=="随机听歌":
            print("[*]QQ:"+str(user)+"请求随机听歌操作")
            req = requests.get("https://api.kit9.cn/api/neteasecloudmusic/")
            print("[*]读取成功:",req)
            ans=json.loads(req.text)
            songname=ans["data"]["songname"]
            print("[*]解析成功:",songname)
            author=ans["data"]["author"]
            print("[*]解析成功:",author)
            address=ans["data"]["musicaddress"]
            print("[*]解析成功:",address)
            pic=ans["data"]["pic"]
            print("[*]解析成功:",pic)
            send_group_msg(group,"曲名:"+str(songname)+"\n用户昵称:"+str(author)+"\n音乐链接:"+str(address)+"[CQ:image,file="+str(pic)+"]")
            print("[*]成功发送了回复")
    #############################        
        if message=="一言":
            print("[*]QQ:"+str(user)+"请求一言操作")
            req = requests.get("https://api.iyk0.com/yi/")
            print("[*]解析成功",req)
            send_group_msg(group,req.text)
            print("[*]成功发送了回复")
    #############################        
        if message=="随机微视":
            print("[*]QQ:"+str(user)+"请求随机微视操作")
            req = requests.get("http://ovooa.com/API/weishi/api.php")
            print("[*]解析成功",req)
            ans=json.loads(req.text)
            print("[*]解析成功",ans)
            ans=ans["data"]
            print("[*]解析成功",ans)
            name=ans["name"]
            print("[*]解析成功",name)
            author=ans["author"]
            img=ans["img"]
            url=ans["url"]
            send_group_msg(group,"标题:"+str(name)+"\n作者:"+str(author))
            send_group_msg(group,"视频链接:"+str(url.replace('&','&amp')))
            
            print("[*]成功发送了回复")
    #############################
        if message=="精神语录":
            print("[*]QQ:"+str(user)+"请求精神语录操作")
            req = requests.get("https://api.iyk0.com/jsyl/")
            print("[*]解析成功",req)
            send_group_msg(group,req.text)
            print("[*]成功发送了回复")
    #############################
        if message=="爱情语录":
            print("[*]QQ:"+str(user)+"请求爱情语录操作")
            req = requests.get("https://api.iyk0.com/aiqing/")
            print("[*]解析成功",req.text)
            send_group_msg(group,req.text)
            print("[*]成功发送了回复")
    #############################
        if message=="来个头像框":
            print("[*]QQ:"+str(user)+"请求来个头相框操作")
            send_group_msg(group,"[CQ:image,cache=0,file=http://ovooa.com/API/head/?QQ="+str(user)+"]")
            print("[*]成功发送了回复")
    #############################
        if message.startswith("编码"):
            print("[*]QQ:"+str(user)+"请求base64操作")
            text=message[2:]
            print("[*]编码："+str(text))
            send_group_msg(group,base64.b64encode(text.encode()).decode())
        if message.startswith("解码"):
            print("[*]QQ:"+str(user)+"请求base64操作")
            text=message[2:]
            print("[*]解码："+str(text))
            out=base64.b64decode(text.encode()).decode()
            send_group_msg(group,out)
            print("[*]成功发送了回复")
    #############################
        if message.startswith("翻译"):
            print("[*]QQ:"+str(user)+"请求翻译操作")
            text=message[2:]
            api="http://fanyi.youdao.com/translate?i="
            res=json.loads(requests.get(api+text+"&type=AUTO&doctype=json").content.decode())
            out=""
            for y in res['translateResult']:
                for x in y:
                    out=out+x['tgt']+'\n'
            ret="翻译结果:\n原文:"+text+"\n译文:"+out
            if "2317220879" in message:
                ret="翻译结果:\n原文:"+text+"\n译文:"+"氷ۖ໌氷ۖ໌࿚໊ᔉ⚝"
            send_group_msg(group,ret)
            print("[*]成功发送了回复")
    #############################
        if message.startswith("计算"):
            print("[*]QQ:"+str(user)+"请求计算操作")
            if len(str(message[2:]))<=10:
                text=re.sub(u"([a-zA-Z]+)","",str(message[2:]))
                try:
                    ans=eval(text)
                    send_group_msg(group,str(text)+str("=")+str(ans))
                    print("[*]成功发送了回复")
                except:
                        send_group_msg(group,"这也没法算啊(QAQ)")
            else:
                    send_group_msg(group,"你是不是要害我(QAQ)")
    #############################
        if message.startswith("查查天气"):
            try:
                print("[*]QQ:"+str(user)+"请求搜搜古诗操作")
                text=re.sub("[0-9]+", '',message[4:])
                print("[*]正则表达式文本提取:",text)
                try:
                    num = re.findall("\d+",message[4:])
                    print("[*]正则表达式数字提取:",num[0])
                    req = requests.get("http://hm.suol.cc/API/tq.php?msg="+str(text)+"&n="+str(num[0]))
                except:
                    req = requests.get("http://hm.suol.cc/API/tq.php?msg="+str(text))
                print("[*]读取成功:",req.text)
                ans=str(req.text)
                try:
                    send_group_msg(group,ans)
                except:
                    send_group_msg(group,ans)
            except Exception as e:
                print("[*]发送错误:",e)
    #############################
        if message.startswith("搜搜古诗"):
            print("[*]QQ:"+str(user)+"请求搜搜古诗操作")
            try:
                text=re.sub("[0-9]+", '',message[4:])
                print("[*]正则表达式文本提取:",text)
                num = re.findall("\d+",message[4:])
                print("[*]正则表达式数字提取:",num[0])
                req = requests.get("https://api.iyk0.com/sc/?msg="+str(text)+"&b="+str(num[0]))
                print("[*]读取成功:",req)
                ans=json.loads(req.text)
                print("[*]解析成功:",ans)
                try:
                    name=ans["name"]
                    print("[*]解析成功:",name)
                    autor=ans["autor"]
                    print("[*]解析成功:",autor)
                    content=ans["content"]
                    print("[*]解析成功:",content)
                    time=ans["time"]
                    print("[*]读取时间:",time)
                    send_group_msg(group,"题目:"+str(name)+"\n作者:"+str(autor))
                    send_group_msg(group,"原文和释义:")
                    send_group_msg(group,content)
                except:
                    send_group_msg(group,"没搜到啊qwq")
                print("[*]成功发送了回复")
            except:
                send_group_msg(group,"你输入的不对吧qwq")
    #############################
        if message.startswith("搜搜漫画"):
            try:
                print("[*]QQ:"+str(user)+"请求搜搜古诗操作")
                text=re.sub("[0-9]+", '',message[4:])
                print("[*]正则表达式文本提取:",text)
                num = re.findall("\d+",message[4:])
                print("[*]正则表达式数字提取:",num[0])
                req = requests.get("https://api.iyk0.com/txmh/?msg="+str(text)+"&n="+str(num[0]))
                print("[*]读取成功:",req)
                ans=json.loads(req.text)
                print("[*]解析成功:",ans)
                print(ans)
                try:
                    title=ans["title"]
                    print("[*]解析成功:",title)
                    img=ans["img"]
                    print("[*]解析成功:",img)
                    collection=ans["collection"]
                    print("[*]解析成功:",collection)
                    author=ans["author"]
                    print("[*]解析成功:",author)
                    time=ans["time"]
                    print("[*]解析成功:",time)
                    tip=ans["type"]
                    print("[*]解析成功:",tip)
                    introduce=ans["introduce"]
                    print("[*]解析成功:",introduce)
                    url=ans["url"]
                    print("[*]解析成功:",url)
                    send_group_msg(group,"标题："+str(title)+"\n收藏人数："+str(collection)+"\n作者："+str(author)+"\n更新时间："+str(time)+"\n类型："+str(tip)+"\n介绍："+str(introduce)+"\n点这里在线看："+str(url)+"[CQ:image,file="+str(img)+"]")
                except:
                    send_group_msg(group,"没搜到啊qwq")
                print("[*]成功发送了回复")
            except:
                send_group_msg(group,"你输入的不对吧qwq")
    #############################
        if message.startswith("搜搜小说"):
            try:
                print("[*]QQ:"+str(user)+"请求搜搜古诗操作")
                text=re.sub("[0-9]+", '',message[4:])
                print("[*]正则表达式文本提取:",text)
                num = re.findall("\d+",message[4:])
                print("[*]正则表达式数字提取:",num[0])
                req = requests.get("https://api.iyk0.com/sgxs/?msg="+str(text)+"&b="+str(num[0]))
                print("[*]读取成功:",req)
                ans=json.loads(req.text)
                print(ans)
                try:
                    title=ans["name"]
                    print("[*]解析成功:",title)
                    img=ans["img"]
                    print("[*]解析成功:",img)
                    autor=ans["autor"]
                    print("[*]解析成功:",autor)
                    tip=ans["type"]
                    print("[*]解析成功:",tip)
                    content=ans["content"]
                    print("[*]解析成功:",content)
                    url=ans["url"]
                    print("[*]解析成功:",url)
                    send_group_msg(group,"书名："+str(title)+"\n简介："+str(content)+"\n作者："+str(autor)+"\n类型："+str(tip)+"\n点这里在线看："+str(url)+"[CQ:image,file="+str(img)+"]")
                    print("[*]成功发送了回复")
                except:
                    send_group_msg(group,"没搜到啊qwq")
            except:
                send_group_msg(group,"你输入的不对吧qwq")
    #############################
        if message.startswith("查询手机号"):
            print("[*]QQ:"+str(user)+"请求查询手机号操作")
            text=message[5:]
            try:
                req = requests.get("https://api.iyk0.com/tel/?tel="+str(text))
                print("[*]读取成功:",req)
                ans=json.loads(req.text)
                print("[*]解析成功",ans)
                tel=ans["tel"]
                local=ans["local"]
                duan=ans["duan"]
                tip=ans["type"]
                yys=ans["yys"]
                bz=ans["bz"]
                send_group_msg(group,"手机号:"+str(tel)+"\n"+str(local)+"\n"+str(duan)+"\n"+str(tip)+"\n"+str(yys)+"\n"+str(bz)) 
                print("[*]成功发送了回复")
            except:
               send_group_msg(group,"你输入错了吧")
               
    #############################
        if message.startswith("百度百科"):
            print("[*]QQ:"+str(user)+"请求百度百科操作")
            text=message[4:]
            try:
                req = requests.post("https://api.muxiaoguo.cn/api/Baike?api_key=1faae800bb349a41&type=Baidu&word="+str(text))
                print("[*]读取成功:",req)
                ans=json.loads(req.text)
                print("[*]解析成功",ans)
                content=ans["data"]["content"]
                print("[*]解析成功",content)
                ImgUrl=ans["data"]["ImgUrl"]
                print("[*]解析成功",ImgUrl)
                send_group_msg(group,content)
                print("[*]成功发送了回复")
            except:
                if str(ans["code"])=="-4":
                   send_group_msg(group,"我没找到呀qwq")
                else:
                    send_group_msg(group,content)
    #############################
        if message.startswith("查ip"):
            print("[*]QQ:"+str(user)+"请求ip查询操作")
            text=message[3:]
            try:
                req = requests.post("https://api.kit9.cn/api/attribution/?ip="+str(text))
                print("[*]读取成功:",req)
                ans=json.loads(req.text)
                print("[*]解析成功",ans)
                ip=ans["data"]["ip"]
                print("[*]解析成功",ip)
                Digitaladdress=ans["data"]["Digitaladdress"]
                print("[*]解析成功",Digitaladdress)
                location=ans["data"]["location"]
                print("[*]解析成功",location)                
                send_group_msg(group,"==="+str(ip)+"==="+"\n"+"数字地址:"+str(Digitaladdress)+"\n"+"ip归属地:"+str(location))
                print("[*]成功发送了回复")
            except:
                    send_group_msg(group,"你输错了吧qwq")
    #############################
        if message.startswith("点歌"):
            print("[*]QQ:"+str(user)+"请求点歌操作")
            text=message[2:]
            req = requests.get("http://ovooa.com/API/kwdg/api.php?msg="+str(text)+"&n=1&p=1&sc=1&type=json")
            req = req.text
            req = req[5:]
            print("[*]读取成功:",req)
            ans=json.loads(req)
            ans=ans["meta"]["music"]
            print("[*]解析成功",ans)
            title=ans["title"]
            desc=ans["desc"]#作者
            musicUrl=ans["jumpUrl"]#音乐链接
            preview=ans["preview"]#封面图片
            send_group_msg(group,"乐曲名:"+str(title)+"\n作者:"+str(desc)+"\n音乐链接:"+str(musicUrl)+"\n[CQ:image,cache=0,file="+str(preview)+"]")    #############################
        if message.startswith("说"):
            print("[*]QQ:"+str(user)+"请求复述操作")
            text=message[1:]
            print("[*]复述:"+str(text))
            send_group_msg(group,"[CQ:tts,text="+str(text)+"]")
    #############################
        if message == "微博热搜":
            req=requests.get("https://api.kit9.cn/api/weibohotsearch/")
            ans=json.loads(req.text)
            ans=ans["data"]
            print(ans)
            end=[]
            for data in ans:
                time.sleep
                tmp="\n标题:"+str(data["title"])+"\n热度:"+str(data["heat"])+"\n链接:"+str(data["link"])
                end.append(tmp)
            ansstr=listtostr(end)
            ansend=split_text(ansstr,1000)
            for outdata in ansend:
                time.sleep(3)
                send_group_msg(group,outdata)
    #############################
        if message.startswith("举牌牌"):
            print("[*]QQ:"+str(user)+"请求举牌牌操作")
            text=message[3:]
            text=remove_upprintable_chars(text)
            text=re.sub('\s[\]\[]+','',text)
            print(text)
            print("[*]举牌:"+str(text))
            send_group_msg(group,"[CQ:image,cache=0,file=http://ovooa.com/API/pai/?msg="+str(text)+"]")
####################管理功能########################           
        if message.startswith("改群名") and str(user) in owner:
            text=message[3:]
            print("successful")
            set_group_name(group,text)
        ###权限管理###
        if message.startswith("加入黑名单") and str(user) in owner:
            text=message[5:]
            permissions.blacklist_add(str(text))
            send_group_msg(group,"已将"+str(text)+"加入黑名单")
        if message.startswith("移除黑名单") and str(user) in owner:
            text=message[5:]
            permissions.blacklist_del(str(text))
            send_group_msg(group,"已将"+str(text)+"从黑名单移除")
        if message.startswith("加入管理权限") and str(user) in owner:
            text=message[6:]
            permissions.owner_add(str(text))
            send_group_msg(group,"已将"+str(text)+"设置为小淇管理")
        if message.startswith("移除管理权限") and str(user) in owner:
            text=message[6:]
            permissions.owner_del(str(text))
            send_group_msg(group,"已取消"+str(text)+"小淇管理权限")
#####################语言区#########################
        if message=="你好":
            send_group_msg(group,"你好")
            print("发送你好")
        if message=="对吧":
            send_group_msg(group,"啊对对对")
            print("发送啊对对对")
        if message=="小淇你的爱好是什么":
            send_group_msg(group,"唱,跳,rap,篮球")
            print("发送唱,跳,rap,篮球")
        if message=="小淇卖个萌":
            send_group_msg(group,"[CQ:image,cache=0,file=http://sjq131313.gitee.io/cqrobot/img/a.png]")
            print("小淇卖萌")
        if message=="小淇在吗":
            send_group_msg(group,"￣ω￣=在呢！")
        if message=="诶嘿":
            send_group_msg(group,"ヾ(●´∀｀●) ")
        if message=="az"or message=="啊这":
            send_group_msg(group,"(◕ᴗ◕✿) az？？")
        if message.startswith("哈哈"):
            send_group_msg(group,"ヽ(￣▽￣)ﾉ哈哈哈哈哈哈哈哈哈")
        if message=="qwq" or message=="qaq" or message=="QAQ" or message=="QwQ" or message=="QWQ":
            send_group_msg(group,"qwq")
        if message=="owo":
            send_group_msg(group,"[CQ:face,id=21]可爱~~")
def Private_message_processing(user,message_id,message):#私聊消息可用功能
    ####打印获取的内容####
    print("====私聊消息====")
    print("[*]发送者QQ号:",user,"\n[*]消息ID:",message_id,"\n[*]消息内容:",message)
    print("================")
    #######功能实现#######
    if message=="test":
        send_private_msg(user,"test")
    else:
        try:
            message=message.text.replace('小淇','菲菲')
            response = requests.get("https://api.iyk0.com/liaotian/?msg="+str(message))
            ans=response.text.replace('菲菲','小淇')
            send_private_msg(user,str(ans))
        except:
            pass
def Join_the_group(group,user):#新人入群
    ####打印获取的内容####
    print("====加群通知====")
    print("[*]",user,"加入",group)
    print("================")
    #######功能实现#######
    send_group_msg(group,"嘻嘻，欢迎欢迎~"+"[CQ:at,qq="+str(user)+"]")
