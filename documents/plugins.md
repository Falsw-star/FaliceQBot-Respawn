# Falice - 插件  
## 介绍  
Falice提供了一个不规范但较简易的插件模式。其流程可以分为：  
1. 机器人访问插件文件夹；  
2. 机器人导入每一个.**py**文件作为一个模块；  
3. 机器人运行每个模块的**load**函数，该函数返回一个**Plugin**对象；  
4. 机器人将每个**Plugin**对象添加到**PluginList**中，并将列表传给**Matcher**，开始对每条消息匹配。  
## 编写插件
### 实例化Plugin类
若要使机器人加载你的插件，你需要在插件文件夹中新建一个.**py**文件，导入**faliceqbot.Plugin**类，并***实例化***而非继承该类：  
```
from faliceqbot import Plugin

YourPlugin = Plugin(
    name="YourPlugin", #插件名称
)
```  
### 编写函数  
插件的运作本质是函数的运行，编写一个（或多个）函数作为你的插件运行的灵魂。  
该函数接受一个[**faliceqbot.Message**](./classes/Message.md)对象作为参数，并返回**None**:  
```
from faliceqbot import Message

def your_function(msg: Message):
    msg.respond("Hello World!")
```

### 添加事件监听器（触发器）  
给插件添加一个事件监听器，监听器内为你的函数设置一个条件，当消息满足这个条件时，函数将被运行。
```
YourPlugin.onCommand(your_function, "your_command")
```
### 编写load函数  
为了让Falice从你的文件中获取到你的PLugin对象，你需要定义一个**load**函数，返回你的Plugin对象。  
```
def load():
    return YourPlugin
```  
### 恭喜！你完成了你的插件！它看起来像这样：
```
from faliceqbot import Plugin, Message

YourPlugin = Plugin("YourPlugin")

def your_function(msg: Message):
    msg.respond("Hello World!")

YourPlugin.onCommand(your_function, "your_command")

def load():
    return YourPlugin
```  
这时在群组内发送"**/your_command**"，机器人回应"**Hello World!**"，说明你成功了！给你心心哦！ :heart: