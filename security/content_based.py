import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import logging

class ContentBasedFiltering:
    def __init__(self, item_profiles):
        try:
            # Assuming item_profiles is a DataFrame with at least a 'description' column
            self.item_profiles = pd.DataFrame(item_profiles)
            self.tfidf = TfidfVectorizer(stop_words='english')

            # Fit and transform the item descriptions into TF-IDF vectors
            if 'description' in self.item_profiles.columns:
                self.tfidf_matrix = self.tfidf.fit_transform(self.item_profiles['description'])
            else:
                raise ValueError("Item profiles must contain a 'description' field.")

            logging.info("ContentBasedFiltering initialized successfully.")
        except Exception as e:
            logging.error(f"Error initializing ContentBasedFiltering: {e}")
            raise

    def recommend(self, user_id, item_id=None, top_n=5):
        try:
            if item_id is None:
                logging.error(f"No item_id provided for user {user_id}. Cannot generate recommendations.")
                return []

            # Find the index of the item in the item_profiles DataFrame
            item_index = self.item_profiles.index[self.item_profiles['item_id'] == item_id].tolist()

            if not item_index:
                logging.error(f"Item ID {item_id} not found in item profiles.")
                return []

            item_index = item_index[0]

            # Calculate similarity between the given item and all other items
            cosine_similarities = cosine_similarity(self.tfidf_matrix[item_index], self.tfidf_matrix).flatten()

            # Get indices of the top N most similar items (excluding the given item itself)
            similar_indices = cosine_similarities.argsort()[-top_n-1:-1][::-1]

            # Get the recommended item_ids and their similarity scores
            recommendations = [
                {"item_id": self.item_profiles.iloc[idx]['item_id'], "score": cosine_similarities[idx]}
                for idx in similar_indices
            ]

            logging.info(f"Generated {len(recommendations)} content-based recommendations for user {user_id}.")
            return recommendations
        except Exception as e:
            logging.error(f"Error generating content-based recommendations for user {user_id}: {e}")
            return []