from kafka import KafkaConsumer
from hybrid_recommendation import HybridRecommendation
import json
import logging


'''

StreamProcessor Class: Consumes user interaction data from Kafka and processes it to provide recommendations.
Initialization: Sets up a Kafka consumer and initializes the hybrid recommendation engine.
process_stream Method: Iterates through messages in the Kafka topic, extracts user IDs, and generates personalized recommendations.

'''
class StreamProcessor:
    def __init__(self, kafka_topic, kafka_server, user_item_matrix, item_profiles):
        try:
            self.consumer = KafkaConsumer(
                kafka_topic,
                bootstrap_servers=kafka_server,
                value_deserializer=lambda m: json.loads(m.decode('utf-8'))
            )
            self.recommendation_engine = HybridRecommendation(user_item_matrix, item_profiles)
        except Exception as e:
            logging.error(f"Error initializing StreamProcessor: {e}")
            raise
        logging.basicConfig(level=logging.INFO)

    def process_stream(self):
        for message in self.consumer:
            try:
                user_id = message.value.get('user_id')
                if user_id:
                    recommendations = self.recommendation_engine.recommend(user_id)
                    logging.info(f"Personalized real-time recommendations for user {user_id}: {recommendations}")
            except Exception as e:
                logging.error(f"Error processing stream message: {e}")


