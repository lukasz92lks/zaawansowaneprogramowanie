import pika

from producer import DONE_QUEUE, WORK_QUEUE, connect


def main():
    with connect() as connection:
        channel = connection.channel()
        channel.queue_declare(queue=WORK_QUEUE, durable=True)
        channel.queue_declare(queue=DONE_QUEUE, durable=True)
        channel.confirm_delivery()

        while True:
            method, _, body = channel.basic_get(
                queue=WORK_QUEUE, auto_ack=False
            )

            if method is None:
                connection.sleep(5)
                continue

            message = body.decode("utf-8")
            print(f"{message}: in_progress")
            connection.sleep(30)

            channel.basic_publish(
                exchange="",
                routing_key=DONE_QUEUE,
                body=body,
                properties=pika.BasicProperties(delivery_mode=2),
                mandatory=True,
            )
            channel.basic_ack(delivery_tag=method.delivery_tag)
            print(f"{message}: done")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Zatrzymano consumera")