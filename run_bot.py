from config import Config
from faliceqbot import QBot

config = Config()
Falice = QBot(
    config.adapter,
    config.token,
    config.wsbase,
    config.httpbase,
    config.prefix,
    config.permission,
    plugin_folder='plugins',
)
Falice.run()