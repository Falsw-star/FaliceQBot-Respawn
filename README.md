<div align="center">
<h1>
FaliceQBot-Respawn  
</h1>
</div>


> 'Falice'是'False'与'Alice'的组合。
## 简介  
这是FaliceQBot的重制版。原项目是一个**烂到不能再烂**的项目，已经**永远地**消失了。以下简称本项目为Falice。  
Falice是一个致力于简化QQ机器人使用的Python模块，当前处于开发阶段，且**可能很长一段时间内不会再更新**。  
由于初衷是面向QQ群开发，因此开发时忽略了QQ频道（QQ频道内可以使用官方机器人），内部并无“频道”的概念。  
目前（2024.8.5）仅对Satori协议提供了适配器，参考[Chronocat](https://github.com/chrononeko/chronocat)项目以及[Satori](https://satori.js.org/)协议官方。
## 安装  
```
pip install faliceqbot
```
## 使用（以[console适配器](./faliceqbot/adapters/console.py)为例）  
### 文件目录：
```
|--Base
    |--run_bot.py #你的机器人入口文件
    |--pluginsQWQ #你的插件文件夹
        |--Echo.py
```
## run_bot.py:  
```
from faliceqbot import QBot
# from faliceqbot.bot import QBot

Falice = QBot(
    adapter="console",
    plugin_folder="pluginsQWQ"
)

Falice.run()
```
## Echo.py:
```
from faliceqbot import Plugin, Message

Echo = Plugin("Echo")
def echo(msg: Message):
    msg.respond(msg.get_args_string())
Echo.onCommand(echo, 'echo')

def load():
    return Echo
```
## 运行：  
```
python run_bot.py
```
# 更多文档：
### 编写插件，请参阅 [插件开发文档](./documents/plugins.md)