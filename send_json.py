#!/usr/bin/env python

import argparse
import pika

# Instantiate argument parser
parser = argparse.ArgumentParser()

parser.add_argument('--msg', action='store', dest='message', help='Message')

results = parser.parse_args()

#msgBody = '{"data":{"recipient":"fishybones@oracle.com","subject":"Hello Cloud","body":"My Email Body"}}'

msgBody =''' {"data" : {
		"subject" : "Testing Rabbit",
		"sender" : "no_reply@oracleindustry.com",
		"body" : "Python Test body from rabbit GUI running",
		"recipient" : ["chris.bartels@oracle.com"]
	}
}'''


if results.message is not None:
    msgBody = results.message

rabbitHost='oci-apps.us.oracle.com'
    
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitHost))

channel = connection.channel()

channel.queue_declare(queue='AAAspring-boot')

#properties = pika.BasicProperties(content_type='application/json')
#properties = pika.BasicProperties(content_type='text/plain', type='example')
properties = pika.BasicProperties(content_type='text/plain')
                                          
                                          
#channel.basic_publish(exchange='', routing_key='spring-boot', body=msgBody)
channel.basic_publish('', 'AAAspring-boot', msgBody, properties)

print(" [x] Sent " + msgBody)

connection.close()
