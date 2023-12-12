import json
import time

import requests
from github_issue_listener import listen_for_github_issue_events
from sweep_issue_creator import create_sweep_issue


def sync_assignees():
    while True:
        try:
            # Make a GET request to the GitHub API endpoint for retrieving issue events
            response = requests.get('https://api.github.com/issues/events')
            response.raise_for_status()
            issue_events = json.loads(response.text)

            # Process each issue event
            for issue_event in issue_events:
                listen_for_github_issue_events(issue_event)

            # Delay between each iteration of the loop
            time.sleep(60)  # Adjust the delay as needed

        except Exception as e:
            # Handle exceptions and manual overrides
            # Add specific conditions or configurations to apply the necessary actions
            pass

if __name__ == '__main__':
    sync_assignees()
