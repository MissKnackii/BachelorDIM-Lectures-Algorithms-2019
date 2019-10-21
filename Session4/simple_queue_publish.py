# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:36:55 2019

@author: chaulaic
"""
import os
import pika 

def simple_queue_publish(concurrency) :

    i=0
    
    amqp_url='amqp://vqbglcjd:lUp91qezVmYJkFh9ct5AOdHeFspespmv@dove.rmq.cloudamqp.com/vqbglcjd'
    
    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    connection = pika.BlockingConnection(params) # Connect to CloudAMQP

    properties = pika.BasicProperties()
    
    channel = connection.channel()
    channel.queue_declare(queue='presentation')
    
    if (concurrency):
        while i < 500 :
            properties.delivery_mode = 2
                        
            channel.basic_publish(exchange='',
                                  routing_key='presentation',
                                  body='Camille CHAULAIC',
                                  properties=properties)
            print("[x] Sent 'Camille CHAULAIC'")
            
            i+=1
            
            
    else:       
 
        channel.basic_publish(exchange='',
                              routing_key='presentation',
                              body='Camille CHAULAIC')
        print("[x] Sent 'Camille CHAULAIC'")
        
    connection.close()
