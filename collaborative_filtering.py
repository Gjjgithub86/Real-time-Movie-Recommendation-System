import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import logging

'''

CollaborativeFiltering Class: Calculates similarities between users to recommend items.
Initialization: Takes a user-item interaction matrix and computes a similarity matrix using cosine similarity.
recommend Method: Finds users most similar to the given user ID and generates a list of recommended items.
Error Handling: Manages exceptions for missing user data and computation errors.

'''


class CollaborativeFiltering:
    def __init__(self, user_item_matrix):
        try:
            self.user_item_matrix = pd.DataFrame(user_item_matrix)
            self.similarity_matrix = cosine_similarity(self.user_item_matrix)
        except Exception as e:
            logging.error(f"Error initializing CollaborativeFiltering: {e}")
            raise

    def recommend(self, user_id, top_n=5):
        try:
            user_index = self.user_item_matrix.index.get_loc(user_id)
            user_similarity_scores = self.similarity_matrix[user_index]
            similar_users_indices = user_similarity_scores.argsort()[-top_n-1:-1][::-1]
            recommendations = []
            for idx in similar_users_indices:
                similar_user_id = self.user_item_matrix.index[idx]
                user_data = self.user_item_matrix.loc[similar_user_id]
                recommendations.extend(user_data[user_data > 0].index.tolist())
            return list(set(recommendations))
        except KeyError as e:
            logging.error(f"User ID not found: {e}")
            return []
        except Exception as e:
            logging.error(f"Error generating recommendations: {e}")
            return []
