import pika
import json


def send_message_queue(user):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        channel = connection.channel()

        channel.queue_declare(queue="fila_alunos", durable=True)

        mensagem = json.dumps(
            {
                "id": str(user.user_id),
                "name": user.username,
                "photo": user.photo.url,
            }
        )
        channel.basic_publish(exchange="", routing_key="fila_alunos", body=mensagem)

        print(f"Mensagem enviada para a fila: {mensagem}")
        connection.close()
    except Exception as e:
        print(f"Erro ao enviar mensagem para a fila: {e}")
