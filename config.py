import yaml

class Config:
    def __init__(self) -> None:
        self.config: dict = self._read()
        self.adapter: str = self.config['ADAPTER'].lower() if 'ADAPTER' in self.config else 'console'
        self.token: str = self.config['TOKEN'] if 'TOKEN' in self.config else None
        self.wsbase: str = self.config['WSBASE'] if 'WSBASE' in self.config else None
        self.httpbase: str = self.config['HTTPBASE'] if 'HTTPBASE' in self.config else None
        self.prefix: str = self.config['PREFIX'] if 'PREFIX' in self.config else '/'
        self.permission: dict = self.config['PERMISSION'] if 'PERMISSION' in self.config else {}

    def _read(self) ->  dict:
        with open('CONFIG.yml', 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
        return config