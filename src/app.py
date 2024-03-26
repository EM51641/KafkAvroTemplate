# app.py
# fun fact: This snippet was generated entirely by Copilot
from flask import Flask
from kafka import KafkaProducer  # type: ignore
from datetime import UTC, datetime
from kafka.admin import KafkaAdminClient, NewTopic  # type: ignore
from src.utils import avro_serializer

app = Flask(__name__)


producer = KafkaProducer(
    bootstrap_servers=["localhost:9093"],
    value_serializer=avro_serializer,  # json.dumps(v).encode("utf-8"),
)

# Create an admin client
admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9093",
)

# Check if the topic exists
topics = admin_client.list_topics()
if "records" not in topics:
    # If not, define the new topic
    new_topic = NewTopic(name="records", num_partitions=5, replication_factor=1)

    # Create the topic
    admin_client.create_topics(new_topics=[new_topic], validate_only=False)


@app.route("/record", methods=["GET"])
def produce_record():
    """
    Creates a record with the following information:
    - name: The name of the person.
    - age: The age of the person.
    - employer: The employer information, including company name and job title.
    - start_date: The start date of employment as a Unix timestamp.
    - skills: A list of skills.
    - metadata: Additional metadata, including location and department.

    Returns:
    - str: The status of the record creation.
    """
    record = {
        "name": "John Doe",
        "age": 30,
        "employer": {"company_name": "Acme Corp", "job_title": "Software Engineer"},
        "start_date": datetime.now(UTC),
        "skills": ["Python", "Java", "SQL"],
        "metadata": {"location": "San Francisco", "department": "Engineering"},
    }
    # clickhouse can only parse strings without milliseconds
    producer.send("records", record)
    return "ok"
