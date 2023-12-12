import json

import requests
from sweep_issue_creator import create_sweep_issue


def listen_for_github_issue_events(issue_event_data):
    # Extract necessary information from the GitHub issue event data
    action = issue_event_data['action']
    issue_number = issue_event_data['issue']['number']
    # Extract any other relevant fields from the issue_event_data

    # Define a mapping dictionary for GitHub issue actions to Sweep issue status updates
    mapping = {
        'opened': 'open',
        'closed': 'closed',
        'reopened': 'reopened',
        # Add more mappings for other GitHub issue actions and corresponding Sweep issue status updates
    }

    # Map the GitHub issue action to the corresponding Sweep issue status update
    sweep_status_update = mapping.get(action)

    if sweep_status_update:
        # Update the status of the Sweep issue using the create_sweep_issue function
        create_sweep_issue(issue_number, status=sweep_status_update)
    else:
        # Handle unsupported GitHub issue actions

# Use the GitHub API or a GitHub webhook to receive the events and extract the necessary information
def receive_github_issue_events():
    # Make a GET request to the GitHub API endpoint for retrieving issue events
    response = requests.get('https://api.github.com/issues/events')

    # Handle any errors that may occur during the request
    response.raise_for_status()

    # Extract the necessary information from the response
    issue_events = json.loads(response.text)

    # Process each issue event
    for issue_event in issue_events:
        listen_for_github_issue_events(issue_event)

# Entry point of the script
if __name__ == '__main__':
    receive_github_issue_events()
