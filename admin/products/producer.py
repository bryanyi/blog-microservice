import os
from dotenv import load_dotenv
load_dotenv()
import pika

url = os.getenv("AMQPS_KEY")
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

