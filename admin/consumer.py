import os
from dotenv import load_dotenv
load_dotenv()
import pika

url = os.getenv("AMQPS_KEY")
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    pass

channel.basic_consume(queue, on_message_callback)