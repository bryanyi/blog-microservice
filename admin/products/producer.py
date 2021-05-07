import os
from dotenv import load_dotenv
load_dotenv()
import pika

url = os.getenv("AMQPS_KEY")
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    channel.basic_publish(exchange='', routing_key='admin', body='hello!')