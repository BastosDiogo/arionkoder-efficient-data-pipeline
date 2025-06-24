from app.services.consumer import callback

def run_callback_rabbitmq():
    """Run consumer RabbitMQ callback"""
    callback()

if __name__ == '__main__':
    run_callback_rabbitmq()
