#!/usr/bin/env python
import pika

def myCallbackFunction(ch, method, properties, body):
    print(" [x] Received %r" % body)

rabbitHost='localhost'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitHost))

channel = connection.channel()

channel.queue_declare(queue='hello-queue')

channel.basic_consume(myCallbackFunction, queue='hello-queue', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
