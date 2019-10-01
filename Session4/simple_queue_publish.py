# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:36:55 2019

@author: chaulaic
"""
import os
import pika 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--concurrency", help="Concurency mode activate",
                    action="store_true")

args = parser.parse_args()

i=0

if args.concurrency == True:
    while i < 500 :
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
                              body='Camille CHAULAIC',
                              properties=pika.BasicProperties(delivery_mode = 2))
        print("[x] Sent 'Camille CHAULAIC'")
        connection.close()
        i+=1
        
else:
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
