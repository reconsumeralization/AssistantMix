# run_step.py

from utilities import logger

class RunStep:
    """
    Class representing a step taken during a Run.
    """

    def __init__(self, run, action, status="initialized"):
        self.run = run
        self.action = action
        self.status = status
        logger.info(f"RunStep initialized for Run: {run.id} with action: {action}")

    def start(self):
        """
        Start the run step.
        """
        self.status = "running"
        logger.info(f"RunStep started for Run: {self.run.id} with action: {self.action}")

        # Execute the action
        self.action.execute()

    def get_status(self):
        """
        Get the current status of the run step.
        """
        return self.status

    def stop(self):
        """
        Stop the run step.
        """
        self.status = "stopped"
        logger.info(f"RunStep stopped for Run: {self.run.id} with action: {self.action}")

    def get_action(self):
        """
        Get the action of the run step.
        """
        return self.action