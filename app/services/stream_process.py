import ijson
from datetime import datetime


class ProcessData():
    """Class for process and save data."""


    def data_processing(self, data: str | bytes | bytearray):
        """Method for process data"""
        if data.get('document'):
            data['document'] = data['document'].replace('.','').replace('-','')

        if data.get('age', 18) < 18:
            data['WARNING'] = 'User less than 18 years old.'

        data["created_at"] = datetime.today().isoformat()
        return data


    def process_stream(self, body: bytes):
        """Method for streaming data"""
        for item in ijson.items(body, "item"):
            item = self.data_processing(item)
            print(item)

