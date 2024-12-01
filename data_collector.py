from api_client import TMDbClient
import time
import logging
from kafka import KafkaProducer
import json

'''

DataCollector Class: Collects movie data and streams it to Kafka.
KafkaProducer Initialization: Sets up a producer to send messages to a Kafka topic, with error handling for Kafka connection issues.
collect_real_time_data Method: Collects trending movie data, adds user ID for personalization, and sends the data to Kafka.

'''



class DataCollector:
    def __init__(self, api_client, kafka_topic, kafka_server):
        self.api_client = api_client
        self.kafka_topic = kafka_topic
        try:
            self.producer = KafkaProducer(
                bootstrap_servers=kafka_server,
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
        except Exception as e:
            logging.error(f"Error connecting to Kafka server: {e}")
            raise
        logging.basicConfig(level=logging.INFO)

    def collect_real_time_data(self):
        while True:
            try:
                # Example: Collect real-time data for trending movies
                data = self.api_client.get_trending_movies()
                if data:
                    for movie in data.get("results", []):
                        movie['user_id'] = movie.get('user_id', 'default_user')  # Adding user_id for personalization
                        self.producer.send(self.kafka_topic, movie)
                        logging.info(f"Sent movie data to Kafka: {movie['title']} for user: {movie['user_id']}")
            except Exception as e:
                logging.error(f"Error during data collection: {e}")
            time.sleep(60)  # Delay to simulate real-time data collection (e.g., every 1 minute)



