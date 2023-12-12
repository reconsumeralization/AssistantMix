# src/bulk_actions.py

from issue_manager import IssueManager


def assign_issues(issue_ids, assignee):
    """
    Assign the given assignee to the specified list of issue IDs.

    Args:
        issue_ids (list): List of issue IDs.
        assignee (str): Assignee to be assigned to the issues.
    """
    issue_manager = IssueManager()
    for issue_id in issue_ids:
        issue_manager.assign_issue(issue_id, assignee)

def label_issues(issue_ids, label):
    """
    Add the given label to the specified list of issue IDs.

    Args:
        issue_ids (list): List of issue IDs.
        label (str): Label to be added to the issues.
    """
    issue_manager = IssueManager()
    for issue_id in issue_ids:
        issue_manager.add_label(issue_id, label)

def close_issues(issue_ids):
    """
    Close the specified list of issue IDs.

    Args:
        issue_ids (list): List of issue IDs.
    """
    issue_manager = IssueManager()
    for issue_id in issue_ids:
        issue_manager.close_issue(issue_id)

def resolve_issues(issue_ids):
    """
    Mark the specified list of issue IDs as resolved.

    Args:
        issue_ids (list): List of issue IDs.
    """
    issue_manager = IssueManager()
    for issue_id in issue_ids:
        issue_manager.resolve_issue(issue_id)

def move_issues(issue_ids, new_project):
    """
    Move the specified list of issue IDs to the new project.

    Args:
        issue_ids (list): List of issue IDs.
        new_project (str): New project to move the issues to.
    """
    issue_manager = IssueManager()
    for issue_id in issue_ids:
        issue_manager.move_issue(issue_id, new_project)

def confirm_bulk_action(issue_ids):
    """
    Prompt the user for confirmation before performing the bulk action on the specified list of issue IDs.

    Args:
        issue_ids (list): List of issue IDs.
    """
    confirmation = input("Are you sure you want to perform the bulk action? (y/n): ")
    if confirmation.lower() == "y":
        # Perform the bulk action
        pass

def undo_bulk_action(issue_ids):
    """
    Undo the last bulk action performed on the specified list of issue IDs.

    Args:
        issue_ids (list): List of issue IDs.
    """
    # Undo the last bulk action
    pass

def redo_bulk_action(issue_ids):
    """
    Redo the last undone bulk action on the specified list of issue IDs.

    Args:
        issue_ids (list): List of issue IDs.
    """
    # Redo the last undone bulk action
    pass
