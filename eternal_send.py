#!/usr/bin/env python

import argparse
import pika
import time

# Instantiate argument parser
parser = argparse.ArgumentParser()

parser.add_argument('--msg', action='store', dest='message', help='Message')

results = parser.parse_args()

msgBody = 'Hello from Python'

if results.message is not None:
    msgBody = results.message
    
connection = pika.BlockingConnection(pika.ConnectionParameters(host='my-host.com'))
#connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='spring-boot')

counter = 1

while counter>0:

    numberMsgBody = msgBody + " " + str(counter)
    
    print(" [x] Sent " + numberMsgBody)
    
    channel.basic_publish(exchange='', routing_key='spring-boot', body=numberMsgBody)
    
    counter += 1
    
    time.sleep(5)


connection.close()
