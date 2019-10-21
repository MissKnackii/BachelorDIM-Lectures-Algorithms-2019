# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:55:21 2019

@author: chaulaic
"""




import argparse
import simple_queue_publish as publish
import simple_queue_read as read

parser = argparse.ArgumentParser()

parser.add_argument("--read", action="store_true",
                    help="Launch reading script")
parser.add_argument("--publish", action="store_true",
                    help="Launch publish script")
parser.add_argument("--concurrency", action="store_true",
                    help="Activate persitent messages")

args = parser.parse_args()

if(args.read):
    read.simple_queue_read(args.concurrency)
elif(args.publish):
    publish.simple_queue_publish(args.concurrency)
else:
    print("Please specify -r to read or -p to publish")
