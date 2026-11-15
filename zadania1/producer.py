from uuid import uuid4

import pika

WORK_QUEUE = "rozmowy"
DONE_QUEUE = "rozmowy_done"


def connect():
    credentials = pika.PlainCredentials("student", "student123")
    parameters = pika.ConnectionParameters(
        host="127.0.0.1", port=5672, credentials=credentials
    )
    return pika.BlockingConnection(parameters)


def main():
    message = f"Rozmowa {uuid4()}"

    with connect() as connection:
        channel = connection.channel()
        channel.queue_declare(queue=WORK_QUEUE, durable=True)
        channel.confirm_delivery()
        channel.basic_publish(
            exchange="",
            routing_key=WORK_QUEUE,
            body=message.encode("utf-8"),
            properties=pika.BasicProperties(delivery_mode=2),
            mandatory=True,
        )

    print(f"{message}: pending")


if __name__ == "__main__":
    main()