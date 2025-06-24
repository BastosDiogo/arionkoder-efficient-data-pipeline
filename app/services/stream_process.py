import ijson
from datetime import datetime
import logging
from services.sql_database import SQL
from uuid import uuid1
from services.publisher import publisher


class ProcessData():
    """Class for process and save data."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    users_database = SQL().users_database()

    def data_processing(self, data: dict):
        """Method for process data"""
        if ['first_name', 'last_name', 'age', 'document', 'web_site'] != list(data.keys()):
            logging.warning('Data incomplete.')
            return {}

        if '.' in data['document'] or '-' in data['document']:
            data['document'] = data['document'].replace('.','').replace('-','')

        if self.users_in_database(data['document']):
            logging.warning(f'Document {data['document']} already exists in databse.')
            return {}

        if data.get('age', 18) < 18:
            data['WARNING'] = 'User less than 18 years old.'

        data["created_at"] = datetime.today()
        return data


    def users_in_database(self, document:str):
        """Return a tuple with all """
        return True if document in self.users_database else False


    def create_inserts(self, item:dict):
        """Create a data structure for isert into uerser's table"""
        return f"""
            (
                '{str(uuid1())}',
                '{item['first_name']}',
                '{item['last_name']}',
                {item['age']},
                '{item['document']}',
                '{item['web_site']}',
                '{item.get('WARNING', '-')}',
                '{item['created_at']}'
            ),"""


    def message_broker(self, item:dict):
        """Method to use message broker service."""
        try:
            publisher(item)

        except Exception as error:
            logging.error(f'Message broker ERROr: {error}')


    def process_stream(self, body: bytes):
        """Method for streaming data"""
        inserts = ''
        for item in ijson.items(body, "item"):
            item = self.data_processing(item)

            if not item:
                continue

            inserts += self.create_inserts(item)
            self.message_broker(item)

        if inserts:
            logging.info('Begining insert data...')
            SQL().insert_database(inserts)

        logging.info('Finishing process.')


    def find_all(self):
        """Return all users."""
        return {'data': SQL().users_database(only_documents=False)}


    def clean_database(self):
        """Clean up database."""
        SQL().delete_all_users()