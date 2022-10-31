#####################引用库#########################
import json
import asyncio
import websockets
import os
import time
print("[*]加载插件连接器")
from plugins import plugins_connect
wslink='ws://127.0.0.1:8080'
##################websocket配置#####################

async def wssvc(uri):
    async with websockets.connect(uri) as websocket:
        print("[*]小淇已启动！")
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
                    await plugins_connect.Group_message_processing(uri,group_id,user_id,message_id,message)
while True:
    try:
        asyncio.get_event_loop().run_until_complete(wssvc(wslink))#websocket启动
    except Exception as e:#防报错
        print("[!]发生错误!")
        print("[!]错误",repr(e))
        print("[*]准备重启")
###################################################
