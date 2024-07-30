import importlib
import threading
import os, time
import traceback
from Falice import logger
from Falice.matcher import Matcher
from Falice.segments import Config, Message, Base_Adapter, Sender, Plugin, PluginList

class QBot:
    def __init__(self,
            adapter: str = 'console',
            token: str = '',
            wsbase: str = '',
            httpbase: str = '',
            prefix: str = '/',
            permission: dict = {},
            plugin_folder: str = 'plugins',
            breath: float = 0.1,
            delay: float = 0.1
        ) -> None:
        """
        Falice's main class. Easy to use.

        :param adapter: Choose the adapter you want to use, such as 'console'.
        :param token: If your adapter need a token, you should put it here.
        :param wsbase: If your adapter need a websocket connection, you should put the link here.
        :param httpbase: If your adapter need a http link to request, you should put it here.
        :param prefix: The prefix of your command.
        :param permission: The permission dictionary for plugins. Stores permissions for special users like dict[str, int] : {'<user_id>': <level>}
        :param plugin_folder: The folder where your plugins file are located.
        :param breath: Each time the bot dealed with current messages, it will sleep for a while.
        :param delay: When you respond to a message(by Message.respond), the bot will have to wait for a while before sending the message.
        """
        self.config: Config = Config(token, wsbase, httpbase, prefix, permission, delay)
        adapter_name = adapter.lower()
        self.adapter: Base_Adapter = importlib.import_module(f'Falice.adapters.{adapter_name}').Adapter(self.config)
        self.adapter.platform = adapter
        self.plugin_folder: str = plugin_folder
        self.breath: float = breath
        logger.runtime(f'Using adapter: {adapter_name}...')
        self.Formatter: Base_Adapter.Formatter = self.adapter.Formatter()
        self.API: Base_Adapter.API = self.adapter.API(self.adapter)
        self.Listener: Base_Adapter.Listener = self.adapter.Listener(self.adapter, self.Formatter, self.API)
        self.Sender: Sender = Sender(self.Formatter, self.API)
        
        self.MESSAGES: list[Message] = []
        self.PLUGINS: list[Plugin] = []

        self.STATUS: bool = True

    class BotFinishException(Exception): pass

    def run(self) -> None:
        """
        Run your bot: Start Listener, load plugins, and start responding to messages.
        """
        threading.Thread(target=self.Listener.listen, args=(self.MESSAGES,)).start()
        plugins_folder: list = os.listdir(self.plugin_folder)
        for plugin_file_name in plugins_folder:
            if plugin_file_name.endswith('.py'):
                try:
                    logger.info(f'Loading plugin {plugin_file_name}...')
                    plugin_file = importlib.import_module(f'plugins.{plugin_file_name[:-3]}')
                    plugin: Plugin = plugin_file.load()
                    self.PLUGINS.append(plugin)
                    logger.info(f'Loaded {plugin}')
                except Exception as e:
                    logger.error(f'Error loading plugin {plugin_file_name}: {e}')
                    continue

        matcher = Matcher(PluginList(self.PLUGINS))
        try:
            while self.STATUS:
                if self.MESSAGES:
                    message: Message = self.MESSAGES.pop(0)
                    message.Sender = self.Sender
                    logger.chat('{} in {} : {}'.format(message.user.id, 'Private' if message.private else message.group_id, message.content))
                    functions = matcher.match(message)
                    for function in functions:
                        threading.Thread(target=function, args=(message,)).start()
                time.sleep(self.breath)
            
        except self.BotFinishException:
            logger.info('Bot stopped, exiting...')
            self.Listener.STATUS = False
            exit(0)
        except KeyboardInterrupt:
            logger.info('Ctrl+C pressed, exiting...')
            self.Listener.STATUS = False
            exit(0)
        except Exception as e:
            logger.error('Error: {}'.format(e))
            logger.error('Error: {}'.format(traceback.format_exc()))