from pika import ConnectionParameters, BlockingConnection


connection_params = ConnectionParameters(
    host='localhost',
    port=5672
)

def procces_message(ch, method, properties, body):
    print(f"Received message: {body.decode()}")

    ch.basic_ack(delivery_tag=method.delivery_tag)
    
def main():
    with BlockingConnection(connection_params) as conn:
        with conn.channel() as ch:
            ch.queue_declare(queue='messages')
            ch.basic_consume(
                queue='messages',
                on_message_callback=procces_message,
                #auto_ack=True
            )

            ch.start_consuming()

if __name__ == '__main__':
    main()
