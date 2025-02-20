from integration_template.database.mysql_database import MySQLDatabase
from integration_template.utilities.get_random_data import GetRandomData
from integration_template.configurations.testing_data_configuration import TestDataConfiguration


class GetTestsForCloning:

    @staticmethod
    def get_test_id_for_cloning():
        random_num = GetRandomData().generate_random_number(
            TestDataConfiguration().get_test_data().digit_quant_in_range)
        condition = int(str(random_num)+str(random_num))
        id_for_cloning = MySQLDatabase().read_record_by_condition("test", condition,
                                                                  TestDataConfiguration().get_test_data().limit)
        return id_for_cloning
