# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:55:21 2019

@author: chaulaic
"""
import os
import pika 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--read", help="Launch reading script",
                    action="store_true")

args = parser.parse_args()

cpt = 0 #Counter to know the num of message received

if args.read == True :
    
    print('Reading')
    
    def callback(ch, method, properties, body):
        #Function callback call every time the channel received a message
        #Display message
        print(" [x] Received %r" % body)
        global cpt
        cpt += 1
        print(str(cpt) + ' message(s) reçu(s)')

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
    print('coucou')
    
else:
    print('Publishing')
    
    amqp_url='amqp://vqbglcjd:lUp91qezVmYJkFh9ct5AOdHeFspespmv@dove.rmq.cloudamqp.com/vqbglcjd'
    
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