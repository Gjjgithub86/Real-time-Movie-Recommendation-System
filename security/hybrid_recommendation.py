from collaborative_filtering import CollaborativeFiltering
from content_based import ContentBasedFiltering
import logging


'''

HybridRecommendation Class: Combines collaborative filtering and content-based methods to generate recommendations.
Initialization: Instantiates both the collaborative and content-based filtering components.
recommend Method: Merges results from collaborative and content-based recommendations and sorts them based on a score attribute.

'''
class HybridRecommendation:
    def __init__(self, user_item_matrix, item_profiles):
        try:
            self.collaborative_filtering = CollaborativeFiltering(user_item_matrix)
            self.content_based_filtering = ContentBasedFiltering(item_profiles)
        except Exception as e:
            logging.error(f"Error initializing HybridRecommendation: {e}")
            raise

    def recommend(self, user_id):
        try:
            collaborative_results = self.collaborative_filtering.recommend(user_id)
            content_based_results = self.content_based_filtering.recommend(user_id)
            # Merge and rank the results
            final_recommendations = list(set(collaborative_results + content_based_results))
            return sorted(final_recommendations, key=lambda x: x.get('score', 0), reverse=True)  # Ranking based on score
        except Exception as e:
            logging.error(f"Error generating hybrid recommendations: {e}")
            return []