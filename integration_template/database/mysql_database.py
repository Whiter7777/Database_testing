from mysql.connector import connect
from integration_template.database.database_connect_data import DBConnectData
from integration_template.utilities.get_key_placeholders import GetKeyPlaceholders


class MySQLDatabase:
    def __init__(self):
        self._user = DBConnectData().db_connect_data()["username"]
        self._password = DBConnectData().db_connect_data()["password"]
        self._localhost = DBConnectData().db_connect_data()["host"]
        self._database = DBConnectData().db_connect_data()["database"]
        self._connect_db = self._connecting()

    def _connecting(self):
        return connect(
            host=self._localhost,
            user=self._user,
            password=self._password,
            database=self._database
        )

    def _querying(self, query: str):
        if (not self._connect_db.is_connected()) or self._connect_db is None:
            self._connect_db = self._connecting()
        cursor = self._connect_db.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def _execute_query_dict(self, query: str, dct: dict):
        try:
            cursor = self._connect_db.cursor(dictionary=True)
            cursor.execute(query, params=dct)
        except TypeError as err:
            raise (f"An error {err} during insert operation on {self._database}")

    def _closing_connection(self):
        if self._connect_db.is_connected():
            self._connect_db.close()

    def is_field_in_table(self, table_name: str, column_name: str, name):
        read_query = f"SELECT id FROM {table_name} WHERE {column_name} = '{name}'"
        result = self._querying(read_query)
        self._closing_connection()
        if len(result) > 0:
            return True
        return False

    def create_record(self, dct: dict, table_name: str):
        keys_list, placeholders = GetKeyPlaceholders().get_key_placeholders(dct)
        insert_query = f"INSERT INTO {table_name} ({keys_list}) VALUES ({placeholders})"
        try:
            self._execute_query_dict(insert_query, dct)
        except Exception as err:
            raise f"Message: {err}"
        self._connect_db.commit()
        self._closing_connection()

    def read_record_by_condition(self, table_name: str, condition: int, limit: int):
        read_query = f"SELECT * FROM {table_name} WHERE id LIKE '%{condition}%' LIMIT {limit}"
        result = self._querying(read_query)
        self._closing_connection()
        return [record["id"] for record in result]

    def read_last_insert_record_id(self, table_name: str):
        query = f"SELECT * FROM {table_name} ORDER BY id DESC LIMIT 1"
        result = self._querying(query)
        id, = [record["id"] for record in result]
        self._closing_connection()
        return id

    def read_id_from_table_by_column_name(self, table_name: str, column_name: str, name: str):
        read_query = f"SELECT id FROM {table_name} WHERE {column_name} = '{name}'"
        result = self._querying(read_query)
        id, = [record["id"] for record in result]
        self._closing_connection()
        return id

    def update_record_by_id(self, id: int, table_name: str, column_name: str, value):
        update_query = f"UPDATE {table_name} SET {column_name} = {value} WHERE id = {id}"
        try:
            self._querying(update_query)
        except Exception as err:
            return err
        self._connect_db.commit()
        self._closing_connection()

    def copy_record_by_id(self, id, table_name: str, author, project):
        read_query = (f"INSERT INTO {table_name} (name, status_id, method_name, project_id, session_id, start_time, end_time, env, browser, author_id)"
                      f" SELECT name, status_id, method_name, {project}, session_id, start_time, end_time, env, browser, {author}"
                      f" FROM {table_name} WHERE id = {id}")
        try:
            self._querying(read_query)
        except Exception as err:
            return err
        self._connect_db.commit()
        self._closing_connection()

    def delete_record(self, table_name: str, condition: str, value):
        delete_query = f"DELETE FROM {table_name} WHERE {condition} > %s"
        self._execute_query_dict(delete_query, value)
        self._connect_db.commit()
        self._closing_connection()


