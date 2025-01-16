
import pytest
from kafka import KafkaProducer
import pika
import redis
import psycopg2

def test_kafka_connection():
    try:
        producer = KafkaProducer(bootstrap_servers="localhost:9092")
        assert producer.bootstrap_connected()
    except Exception as e:
        pytest.fail(f"Kafka connection failed: {e}")

def test_rabbitmq_connection():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        assert connection.is_open
    except Exception as e:
        pytest.fail(f"RabbitMQ connection failed: {e}")

def test_redis_connection():
    try:
        redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)
        assert redis_client.ping()
    except Exception as e:
        pytest.fail(f"Redis connection failed: {e}")

def test_postgresql_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="eagleeye_db",
            user="eagleeye_user",
            password="secure_password"
        )
        assert conn.status == psycopg2.extensions.STATUS_READY
    except Exception as e:
        pytest.fail(f"PostgreSQL connection failed: {e}")
