from prometheus_client import start_http_server, Summary, Counter
import logging


'''

MetricsCollector Class: Uses Prometheus to collect system metrics.
REQUEST_TIME and ERROR_COUNT: Track request processing time and the number of errors encountered.
record_request_time Method: Measures and records the time taken by any given function.

'''
# Metrics to track request processing time and error counts
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
ERROR_COUNT = Counter('error_count', 'Number of errors encountered')

class MetricsCollector:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        start_http_server(8000)  # Prometheus server running on port 8000

    @REQUEST_TIME.time()
    def record_request_time(self, func, *args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            ERROR_COUNT.inc()
            logging.error(f"Error occurred: {e}")
            raise


