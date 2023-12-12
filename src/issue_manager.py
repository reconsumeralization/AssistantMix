# src/issue_manager.py

from bulk_actions import (assign_issues, close_issues, label_issues,
                          move_issues, resolve_issues)


class IssueManager:
    def __init__(self):
        # Initialize the IssueManager

    def assign_issue(self, issue_id, assignee):
        # Assign the given assignee to the specified issue ID
        assign_issues([issue_id], assignee)

    def add_label(self, issue_id, label):
        # Add the given label to the specified issue ID
        label_issues([issue_id], label)

    def close_issue(self, issue_id):
        # Close the specified issue ID
        close_issues([issue_id])

    def resolve_issue(self, issue_id):
        # Mark the specified issue ID as resolved
        resolve_issues([issue_id])

    def move_issue(self, issue_id, new_project):
        # Move the specified issue ID to the new project
        move_issues([issue_id], new_project)
