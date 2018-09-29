#!/usr/bin/env python
import pika

rabbitHost='oci-apps.us.oracle.com'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitHost))

channel = connection.channel()

channel.queue_declare(queue='spring-boot')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback, queue='spring-boot', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
