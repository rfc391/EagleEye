import yaml
from kafka import KafkaProducer
import pika
import redis
import psycopg2

def test_services():
    try:
        with open("config/example-config.yaml", "r") as file:
            config = yaml.safe_load(file)

        print("Testing Kafka...")
        kafka_config = config["kafka"]
        producer = KafkaProducer(bootstrap_servers=kafka_config["bootstrap_servers"])
        print("Kafka OK")

        print("Testing RabbitMQ...")
        rabbitmq_config = config["rabbitmq"]
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_config["host"]))
        connection.close()
        print("RabbitMQ OK")

        print("Testing Redis...")
        redis_client = redis.StrictRedis(host=config["redis"]["host"], port=6379, db=0)
        redis_client.ping()
        print("Redis OK")

        print("Testing PostgreSQL...")
        pg = config["postgres"]
        conn = psycopg2.connect(host=pg["host"], dbname=pg["dbname"], user=pg["user"], password=pg["password"])
        conn.close()
        print("PostgreSQL OK")

    except Exception as e:
        print(f"Service test failed: {e}")