import os
from dotenv import load_dotenv
import pika
load_dotenv()

params = pika.URLParameters(os.getenv("AMPQ"))
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    channel.basic_publish(exchange='', routing_key='admin', body='hello' )