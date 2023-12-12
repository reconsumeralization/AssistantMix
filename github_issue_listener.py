import json

import requests
from sweep_issue_creator import create_sweep_issue, update_sweep_issue_assignee


def listen_for_github_issue_events(issue_event_data):
    # Extract necessary information from the GitHub issue event data
    action = issue_event_data['action']
    issue_number = issue_event_data['issue']['number']
    assignee = issue_event_data['issue']['assignee']['login'] if 'assignee' in issue_event_data['issue'] else None
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

    assignee_before = ''  # This could be obtained from previous data or storage
    assignee_after = assignee
    if assignee_after != assignee_before:  # Check if the assignee has changed
        update_sweep_issue_assignee(issue_number, assignee_after)  # Call the update_sweep_issue_assignee function to synchronize the assignee

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
