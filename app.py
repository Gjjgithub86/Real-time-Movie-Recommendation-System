from flask import Flask, request, jsonify
from hybrid_recommendation import HybridRecommendation
import logging


'''

Flask Application: Creates a REST API to get recommendations for users.
recommend Endpoint: Receives user IDs as a query parameter and returns personalized recommendations.
Error Handling: Ensures proper error reporting if user ID is missing or if recommendation generation fails.

'''






app = Flask(__name__)
try:
    recommendation_engine = HybridRecommendation(user_item_matrix={}, item_profiles={})  # Example: Use real data structures
except Exception as e:
    logging.error(f"Error initializing recommendation engine: {e}")
    raise

logging.basicConfig(level=logging.INFO)

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400
    try:
        recommendations = recommendation_engine.recommend(user_id)
        logging.info(f"Personalized recommendations provided for user {user_id}")
        return jsonify(recommendations)
    except Exception as e:
        logging.error(f"Error generating recommendations for user {user_id}: {e}")
        return jsonify({"error": "Unable to generate recommendations"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

