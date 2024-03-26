from io import BytesIO
from avro.io import DatumWriter, BinaryEncoder, DatumReader, BinaryDecoder
from avro.schema import parse

schema = parse(open("src/schema.avsc", "rb").read())  # type: ignore


def avro_serializer(data):
    """
    Serializes the given data using Avro schema.

    Args:
        data: The data to be serialized.

    Returns:
        The serialized data.

    Raises:
        Any exceptions that may occur during serialization.
    """
    writer = DatumWriter(schema)
    bytes_writer = BytesIO()
    encoder = BinaryEncoder(bytes_writer)
    writer.write(data, encoder)
    return bytes_writer.getvalue()


def avro_deserializer(data):
    """
    Deserializes the given Avro data.

    Args:
        data (bytes): The Avro data to be deserialized.

    Returns:
        Any: The deserialized Avro record.
    """

    bytes_reader = BytesIO(data)
    decoder = BinaryDecoder(bytes_reader)
    reader = DatumReader(schema)
    record = reader.read(decoder)
    return record
