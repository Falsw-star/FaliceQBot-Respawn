# Message对象  
## 介绍  
适配器接收到每条消息时都会产生一个**Message**对象用于表示这条消息。这条消息触发的插件的事件监听器的函数将以唯一的参数的形式接收到这个**Message**对象。  
## 属性
属性|类型|描述
:-|:-|:-
config|faliceqbot.Config|包含了机器人的配置信息
id|str|消息的唯一id
content|str|消息的文本内容
private|bool|是否为私聊消息
user|faliceqbot.User|发送消息的用户
tag|str|默认为None，若进行手动设置，在使用respond方法时会将tag添加到消息中  
## 方法
方法|需求参数|参数类型|返回值类型|描述
:-|:-|:-|:-|:-
respond|content|str|None|向本条消息所在的会话发送消息
reply|content|str|None|与respond方法完全相同
get_permission|None|None|int|获取本条消息发送者的权限等级
get_text|None|None|str|返回content属性的值
get_command|None|None|str|将假设消息符合指令格式，返回本条消息的指令头
get_args|None|None|list|将假设消息符合指令格式，返回本条消息的指令参数
get_args_string|None|None|str|将假设消息符合指令格式，返回本条消息指令头后的内容
get_images|None|None|list|获取本条消息中所有的图片链接
get_files|None|None|list|获取本条消息中所有的文件链接
get_ats|None|None|list|获取本条消息中所有的at所指的用户id  