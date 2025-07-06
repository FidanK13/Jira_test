from jira import JIRA

# Jira credentials and server info
jira_server = 'https://fidankamranli1995.atlassian.net'
jira_user = 'fidan.kamranli.1995@gmail.com'
jira_api_token = 'ATATT3xFfGF00QdLwLys1A1MZD3eYLfi4ShvzNAUeeVwJa7dIdNCXBbwQp6vtaLfPKCwnmpoGKZSLNBjWhthTUjZ0KKmPITHTJrYl_QIBak5wFZZz8CwIK4_FjpIQuwLVjaGfuDpZ8Gjr780E6FxVcJz_WthdnjjEGi_tKzhYTrB6sK4-eO177g=6A58833C'

# Authenticate
jira = JIRA(
    server=jira_server,
    basic_auth=(jira_user, jira_api_token)
)

# --- 1. Create a new issue ---
issue_dict = {
    'project': {'key': 'SCRUM'},  # Replace with your project key
    'summary': 'Automated task created by script',
    'description': 'This task was created using a Python script.',
    'issuetype': {'name': 'Task'},
}
new_issue = jira.create_issue(fields=issue_dict)
print(f"Issue created: {new_issue.key}")

# --- 2. Add a comment ---
jira.add_comment(new_issue.key, 'This is an automated comment added by the script.')

# --- 3. Update the description ---
new_issue.update(fields={'description': 'Updated description with more details.'})
print(f"Issue {new_issue.key} updated.")
