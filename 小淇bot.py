#####################引用库#########################
import json
import asyncio
import websockets
import requests
import os
import time
from plugins import bot_plugins
####################启动框架########################
os.chdir(".\cqhttp")
os.system("start go-cqhttp.exe -faststart")
print("[#]等待CQHTTP启动。。。")
time.sleep(5)
print("[#]启动小淇。。。")
##################websocket配置#####################
async def wssvc(uri):
    async with websockets.connect(uri) as websocket:
        while True:
            recv_text = await websocket.recv()
            data=json.loads(recv_text)
            #print("#############################debug#############################")
            #print("调试信息：",data)
            #print("###############################################################")
            ##########事件判断##########
            if 'message_type' in data:#消息判断
                if data['message_type']=="group":#当消息是群发送的
                    group_id=data["group_id"]#群号
                    user_id=data["user_id"]#发送者 QQ 号
                    message_id=data["message_id"]#消息 ID
                    message=data["message"]#消息本身
                    bot_plugins.Group_message_processing(group_id,user_id,message_id,message)
                if data['message_type']=="private":#当消息是私聊发送的
                    user_id=data["user_id"]
                    message_id=data["message_id"]
                    message=data["message"]
                    bot_plugins.Private_message_processing(user_id,message_id,message)
            if 'notice_type' in data:#通知判断
                if data['notice_type']=="group_increase":#新人入群
                    group_id=data['group_id']#群号
                    user_id=data['user_id']#发送者 QQ 号
                    bot_plugins.Join_the_group(group_id,user_id)
            ############################
while True:
    try:
        asyncio.get_event_loop().run_until_complete(wssvc('ws://'+bot_plugins.bot_ws_address))#websocket启动
    except Exception as e:#防报错
        print("[!]发生错误!")
        print("[!]错误",repr(e))
        print("[*]准备重启")
###################################################
