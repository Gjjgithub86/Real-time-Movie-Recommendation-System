# scaler.py
import subprocess
import logging


class Scaler:
    def __init__(self, initial_instances=1, max_instances=5):
        """
        Initialize the Scaler with the initial number of instances.

        :param initial_instances: Number of instances to start initially.
        :param max_instances: Maximum number of instances allowed.
        """
        self.current_instances = initial_instances
        self.max_instances = max_instances
        logging.basicConfig(level=logging.INFO)

    def scale_up(self):
        """
        Scale up by adding a new instance, if max_instances is not exceeded.
        """
        if self.current_instances < self.max_instances:
            self.current_instances += 1
            self._start_instance(self.current_instances)
            logging.info(f"Scaled up to {self.current_instances} instances.")
        else:
            logging.warning("Maximum instance limit reached. Cannot scale up further.")

    def scale_down(self):
        """
        Scale down by removing an instance, if more than one instance is running.
        """
        if self.current_instances > 1:
            self._stop_instance(self.current_instances)
            self.current_instances -= 1
            logging.info(f"Scaled down to {self.current_instances} instances.")
        else:
            logging.warning("Only one instance is running. Cannot scale down further.")

    def _start_instance(self, instance_number):
        """
        Start a new instance. For demonstration purposes, simulate instance startup.

        :param instance_number: Instance number to start.
        """
        # Here you could use Docker, Kubernetes, or another tool to start an instance.
        try:
            subprocess.run(["python", "app.py", f"--port={5000 + instance_number}"], check=True)
            logging.info(f"Started instance {instance_number} on port {5000 + instance_number}.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error starting instance {instance_number}: {e}")

    def _stop_instance(self, instance_number):
        """
        Stop an existing instance. For demonstration purposes, simulate instance shutdown.

        :param instance_number: Instance number to stop.
        """
        # Here you could use Docker, Kubernetes, or another tool to stop an instance.
        # Placeholder logic for stopping instance (no-op)
        logging.info(f"Stopped instance {instance_number}.")


# Example usage
if __name__ == "__main__":
    scaler = Scaler(initial_instances=1, max_instances=3)

    # Scale up to add more instances
    scaler.scale_up()
    scaler.scale_up()

    # Scale down to remove instances
    scaler.scale_down()