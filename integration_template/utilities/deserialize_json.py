import json


class DeserializeJson:
    @staticmethod
    def deserialize_json(file_path):
        try:
            with open(file_path) as file:
                data = json.load(file)
                data_str = json.dumps(data)
            return data_str
        except FileNotFoundError:
            exit()
