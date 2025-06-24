import pika
import time
import logging

from app.settings import RABBITMQ_HOST, RABBITMQ_PASS, RABBITMQ_QUEUE, RABBITMQ_USER, RABBITMQ_VHOST

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)

params = pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=5672,
        virtual_host=RABBITMQ_VHOST,
        credentials=credentials
    )
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    logging.info(f" [x] Received {body.decode()}")
    time.sleep(body.count(b'.'))
    logging.info(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback)

channel.start_consuming()
