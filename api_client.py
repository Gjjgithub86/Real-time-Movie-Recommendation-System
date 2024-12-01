import requests
import logging

''' APIClient Class: Handles API requests, including headers setup and API key authorization '''
class APIClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})
        logging.basicConfig(level=logging.INFO)

    ''' get_data Method: Fetches data from a given endpoint with error handling for request exceptions.
        to get movie details, search for movies, and fetch trending movies '''
    def get_data(self, endpoint, params):
        params['api_key'] = self.api_key
        try:
            response = self.session.get(f"{self.base_url}/{endpoint}", params=params)
            response.raise_for_status()
            logging.info(f"Successfully fetched data from {endpoint}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching data from {endpoint}: {e}")
            return None

''' TMDbClient Class: Extends APIClient to interact with TMDb endpoints, providing methods '''
class TMDbClient(APIClient):
    def get_movie_details(self, movie_id):
        endpoint = f"movie/{movie_id}"
        return self.get_data(endpoint, params={})

    def search_movies(self, query):
        endpoint = "search/movie"
        return self.get_data(endpoint, params={"query": query})

    def get_trending_movies(self):
        endpoint = "trending/movie/day"
        return self.get_data(endpoint, params={})




