# KafkAvroTemplate

KafkAvroTemplate is a simple Kafka consumer and producer built with Python.

## 🚀 Features

- Kafka consumer and producer using the `kafka-python` library.
- Dockerized Kafka and Zookeeper services.
- Avro serialization for Kafka messages.
- Flask for handling HTTP requests.

## 🛠️ Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose

### Installation

1.  **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/kafka-ex.git
    ```

2.  **Install Python dependencies:**

    ```sh
    poetry install
    ```

3.  **Start Kafka and Zookeeper services:**

    ```sh
    docker-compose up
    ```

4.  **Run the Flask server::**
    ```sh
    python main.py
    ```
5.  **Access the application:**

        Open your web browser and navigate to `http://localhost:5000` to access the application.

## 📚 Usage

Once the application is running, you can use the following endpoints:

- `GET /record`: Produces an event to the kafka topic

To consume the events, you need to run the `consumers.py` script. You can do this by running the following command in your terminal:

```
python consumers.py
```
