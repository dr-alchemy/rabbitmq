#!/usr/bin/env python

import json
import pika


rabbitHost='my-host.com'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitHost))

channel = connection.channel()

channel.queue_declare(queue='spring-boot')

def callback(ch, method, properties, body):
    parsed = json.loads(body)    
    print(" [x] Received %r" % json.dumps(parsed))

channel.basic_consume(callback, queue='spring-boot', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
