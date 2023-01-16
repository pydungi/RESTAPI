import unittest
from sqlalchemy import create_engine
from datetime import datetime

class TestWeatherDb(unittest.TestCase):

    def test_weather_data(self):
        """
        Test 2 random records in weatherdb
        """
        data = [['USC00110072', '1990-12-04', -39, -89, 0], ['USC00112140', '1986-04-14', None, 89, 157]]
        engine = create_engine('mysql+pymysql://root:root@127.0.0.1/weatherdb')
        conn = engine.connect()
        temp = conn.execute(
        "select * from weather_data where station_id='USC00110072' and date='1990-12-04'").fetchall()[0]
        result = list(temp)
        result[1] = result[1].strftime("%Y-%m-%d")

        self.assertEqual(result, data[0])
        temp = conn.execute(
        "select * from weather_data where station_id = 'USC00112140' and date = '1986-04-14'").fetchall()[0]

        result = list(temp)
        result[1] = result[1].strftime("%Y-%m-%d")

        self.assertEqual(result, data[1])

if __name__ == '__main__':
    unittest.main()

