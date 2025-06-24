from os import getenv

from dotenv import load_dotenv

load_dotenv()

RABBITMQ_HOST: str = getenv("RABBITMQ_HOST", 'localhost')
RABBITMQ_USER: str = getenv("RABBITMQ_USER", 'diogobastos')
RABBITMQ_PASS: str = getenv("RABBITMQ_PASS", 'diogobastos')
RABBITMQ_VHOST: str = getenv("RABBITMQ_VHOST", '/')
RABBITMQ_QUEUE: str = getenv("RABBITMQ_QUEUE", '')
