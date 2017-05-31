import datetime

import pymongo

from input_base import TarsierInputPlugin



class TarsierInputMongodb(TarsierInputPlugin):
    def parse_config(self, config: dict) -> dict:
        if "time_condition" in config:
            condition = config["time_condition"]
            lt = datetime.datetime.now()
            gte = lt - datetime.timedelta(**condition["duration"])
            if condition["format"] == "unix_timestamp":
                between = {
                    "$gte": gte.timestamp(),
                    "$lt": lt.timestamp(),
                }
            else:
                between = {
                    "$gte": gte,
                    "$lt": lt
                }
            c = dict()
            c[condition["field"]] = between
            config["conditions"] = {**config.get("conditions", {}), **c}
            del config["time_condition"]
        return config
    
    def init_plugin(self, url: str, collection: str, conditions: dict):

        if url is None or type(url) != str:
            raise ValueError("url is required and must be string")

        if collection is None or type(collection) != str:
            raise ValueError("collection is required and must be string")

        self._client = pymongo.MongoClient(url)
        self._db = self._client.get_default_database()
        self._col = self._db.get_collection(collection)
        self._conditions = conditions or {}

    def load(self):
        return list(self._col.find(self._conditions))

