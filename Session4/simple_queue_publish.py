# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:36:55 2019

@author: chaulaic
"""
import os
import pika 


amqp_url='amqp://vqbglcjd:lUp91qezVmYJkFh9ct5AOdHeFspespmv@dove.rmq.cloudamqp.com/vqbglcjd'

# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5



connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='presentation')

channel.basic_publish(exchange='',
                      routing_key='presentation',
                      body='Camille CHAULAIC')
print("[x] Sent 'Camille CHAULAIC'")
connection.close()
