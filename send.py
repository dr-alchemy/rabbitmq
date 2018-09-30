#!/usr/bin/env python

import argparse
import pika

# Instantiate argument parser
parser = argparse.ArgumentParser()

parser.add_argument('--msg', action='store', dest='message', help='Message')

results = parser.parse_args()

msgBody = 'Hello World!'

if results.message is not None:
    msgBody = results.message
    
connection = pika.BlockingConnection(pika.ConnectionParameters(host='my-host.com'))
#connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='spring-boot')

channel.basic_publish(exchange='', routing_key='spring-boot', body=msgBody)

print(" [x] Sent " + msgBody)

connection.close()
