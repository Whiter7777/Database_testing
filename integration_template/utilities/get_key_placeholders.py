class GetKeyPlaceholders:
    @staticmethod
    def get_key_placeholders(dct: dict):
        keys_list = ', '.join([key for key in dct.keys()])
        placeholders = ', '.join(f'%({key})s' for key in dct.keys())
        return keys_list, placeholders
