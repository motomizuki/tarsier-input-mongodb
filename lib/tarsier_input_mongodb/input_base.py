class TarsierInputPlugin(object):
    def __init__(self, config):
        self.__config = config

    def init(self):
        self.init_plugin(**self.parse_config(self.__config))
        return self

    def init_plugin(self, **kwargs):
        print("parent")
        pass

    def parse_config(self, config: dict) -> dict:
        return config

    def load(self) -> list:
        return []
