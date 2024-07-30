from config import Config
from Falice import QBot

config = Config()
Falice = QBot(
    config.adapter,
    config.token,
    config.wsbase,
    config.httpbase,
    config.prefix,
    config.permission,
    'plugins'
)
Falice.run()