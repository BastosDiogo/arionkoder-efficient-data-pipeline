#!/usr/bin/env python
import pika
import json
import logging
import settings

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
credentials = pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASS)

def publisher(message:dict):
    """Function for publish in RabbitMQ queue."""
    params = pika.ConnectionParameters(
        host=settings.RABBITMQ_HOST,
        port=5672,
        virtual_host=settings.RABBITMQ_VHOST,
        credentials=credentials
    )
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.queue_declare(queue=settings.RABBITMQ_QUEUE, durable=True)
    message['created_at'] = message['created_at'].strftime("%Y-%m-%d")
    message = json.dumps(message)

    channel.basic_publish(
        exchange='',
        routing_key=settings.RABBITMQ_QUEUE,
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent
        ))
    logging.info(f"Message has sent: {message}")
    connection.close()
