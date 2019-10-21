# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:49:12 2019

@author: chaulaic
"""

import pika
import os

cpt = 0
def simple_queue_read(concurrency):
    
    def callback(ch, method, properties, body):
            #Function callback call every time the channel received a message
            #Display message
            global cpt
            
            print(" [x] Received %r" % body)
            print(" [x] Message Processed, acknowledging")
            ch.basic_ack(delivery_tag = method.delivery_tag)
            
            cpt += 1
            print("Cpt = " + str(cpt))

        
    amqp_url='amqp://vqbglcjd:lUp91qezVmYJkFh9ct5AOdHeFspespmv@dove.rmq.cloudamqp.com/vqbglcjd'
    
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='presentation')
    
    if (concurrency):
        
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='presentation',
                              on_message_callback=callback,
                              auto_ack=False)
        
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
        
    else :
        
        channel.basic_consume(queue='presentation',
                              on_message_callback=callback,
                              auto_ack=True)
        
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()