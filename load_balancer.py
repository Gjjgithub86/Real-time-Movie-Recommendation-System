# load_balancer.py
import requests
import random
import logging

class LoadBalancer:
    def __init__(self, server_list):
        """
        Initialize the LoadBalancer with a list of servers.

        :param server_list: List of server URLs (e.g., ["http://127.0.0.1:5000", "http://127.0.0.1:5001"])
        """
        self.server_list = server_list
        if not self.server_list:
            raise ValueError("Server list cannot be empty.")
        logging.basicConfig(level=logging.INFO)

    def forward_request(self, user_id):
        """
        Forward the user request to one of the available servers.

        :param user_id: ID of the user to get recommendations for.
        :return: The response from the server that handles the request.
        """
        try:
            # Select a server from the list using a round-robin or random selection
            server = random.choice(self.server_list)
            logging.info(f"Forwarding request for user {user_id} to server {server}")

            # Send a request to the selected server
            response = requests.get(f"{server}/recommend", params={"user_id": user_id})
            response.raise_for_status()

            # Return the JSON response from the server
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error forwarding request to server {server}: {e}")
            return {"error": "Unable to get recommendations due to server error."}

# Example usage
if __name__ == "__main__":
    server_list = ["http://127.0.0.1:5000", "http://127.0.0.1:5001"]
    load_balancer = LoadBalancer(server_list)

    # Forward a request for a sample user
    user_id = "123"
    recommendations = load_balancer.forward_request(user_id)
    print(recommendations)