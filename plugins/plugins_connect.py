'''
这是一个插件连接器，用以注册插件应用
例：有一插件plu.py
1.将plu.py文件置于plugins文件夹下
2.在引入插件部分键入from plugins import plu
3.在使用插件部分Group_message_processing中插入await plu.main(uri_in,group,message,user)
'''
#######################引用库#########################
import asyncio
from msg import msg_send
#####################引入插件#########################
#在此引入插件
#from plugins import <plugin>
#####################使用插件#########################
async def Group_message_processing(uri_in,group,user,message_id,message):#群消息可用功能
        #await <plugin>.main(uri_in,group,message,user)
