# Adapter/适配器  
## 介绍  
适配器是FaliceQBot与聊天平台(QQ)通信的桥梁，其三个主要功能对应三个子类：  
1. Formatter - 格式化消息，完成文本与协议格式之间的相互转译。  
2. API - Falice主动与聊天平台进行通信，完成消息发送或信息的获取。  
3. Listener - Falice被动监听平台推送的消息，完成消息的接收。  

## 属性  
属性|类型|描述
:-|:-|:-
config|Config|配置文件
authorization|Authorization|鉴权信息
platform|str|平台名称  
Formatter|Formatter|用于格式化消息
API|API|用于与平台进行通信
Listener|Listener|用于监听平台推送