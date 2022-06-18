# 小淇机器人框架

#### 介绍
小淇机器人框架，是一个基于python websocket+cqhttp的QQ机器人框架

#### 安装教程
1.  下载项目发行版
2.  需要安装python（百度搜索即可）
3.  windows下直接运行项目根目录下的环境配置.cmd，linux请运行python -m pip install -r include.txt
4.  打开\小淇bot\cqhttp\config.yml修改
```
account: # 账号相关
  uin: 机器人的qq号 # QQ账号
  password: '机器人的qq密码' # 密码为空时使用扫码登录
  encrypt: false  # 是否开启密码加密
  status: 0      # 在线状态 请参考 https://docs.go-cqhttp.org/guide/config.html#在线状态
  relogin: # 重连设置
    delay: 3   # 首次重连延迟, 单位秒
    interval: 3   # 重连间隔
    max-times: 0  # 最大重连次数, 0为无限制
```

```
# 连接服务列表
servers:
  # 添加方式，同一连接方式可添加多个，具体配置说明请查看文档
  #- http: # http 通信
  #- ws:   # 正向 Websocket
  #- ws-reverse: # 反向 Websocket
  #- pprof: #性能分析服务器

  - http: # HTTP 通信设置
      host: 127.0.0.1 # 服务端监听地址
      port: 5700      # 服务端监听端口
      timeout: 5      # 反向 HTTP 超时时间, 单位秒，<5 时将被忽略
      long-polling:   # 长轮询拓展
        enabled: false       # 是否开启
        max-queue-size: 2000 # 消息队列大小，0 表示不限制队列大小，谨慎使用
      middlewares:
        <<: *default # 引用默认中间件
      post:           # 反向HTTP POST地址列表
      #- url: '127.0.0.1:8000'               
  - ws:
      # 正向WS服务器监听地址
      host: 127.0.0.1
      # 正向WS服务器监听端口
      port: 6700
      middlewares:
        <<: *default # 引用默认中间件
```
5.配置成功后使用\小淇bot\小淇bot.py文件启动小淇即可

#### 使用说明

1.  你可以在config文件夹下进行机器人的各种配置，比如黑白名单机制web配置
2.  plugins文件夹下提供了机器人插件python脚本，欢迎随便进行修改
##### 更多问题请询问qq：1650562331
