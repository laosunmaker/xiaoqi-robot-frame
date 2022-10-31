#####################引用库#########################
import json
import asyncio
import websockets
import os
import time
async def send_group_msg(uri_in,message,group):#发送群消息
    async with websockets.connect(uri_in) as websocket:
        send_data={'action':'send_group_msg','params':{'message':message, 'group_id':group}}
        await websocket.send(json.dumps(send_data))
