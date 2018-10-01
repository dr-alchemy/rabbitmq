#!/usr/bin/env python

import pika

msgBody = 'Hello World!'

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello-queue')

channel.basic_publish(exchange='', routing_key='hello-queue', body=msgBody)

print(" [x] Sent " + msgBody)

connection.close()
