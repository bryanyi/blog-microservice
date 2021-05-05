import os
from dotenv import load_dotenv
load_dotenv()
import pika

url = os.getenv("AMQS_KEY")
params = pika.URLParameters(url)