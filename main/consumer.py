import os
from dotenv import load_dotenv
import pika
load_dotenv()

ampq = os.getenv("AMPQ")

params = pika.URLParameters(ampq)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch,method,properties,body):
    print("Received in main")
    print(body)

channel.basic_consume(queue='main',on_message_callback=callback)

print('Started Consuming!!!!')

channel.start_consuming()
channel.close()