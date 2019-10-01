# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:49:12 2019

@author: chaulaic
"""

import pika
import os

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

amqp_url='amqp://vqbglcjd:lUp91qezVmYJkFh9ct5AOdHeFspespmv@dove.rmq.cloudamqp.com/vqbglcjd'

url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='presentation')

channel.basic_consume(queue='presentation',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()