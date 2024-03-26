# consumer.py
from kafka import KafkaConsumer  # type: ignore
from src.utils import avro_deserializer


consumer = KafkaConsumer(
    "records",
    bootstrap_servers=["localhost:9093"],
    value_deserializer=avro_deserializer,
)
# note that this for loop will block forever to wait for the next message
for message in consumer:
    print(message.value)
