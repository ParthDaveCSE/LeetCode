# 💻 My LeetCode Solutions
This repository serves as an automatically synchronized collection of my accepted LeetCode solutions. It leverages GitHub Actions to periodically fetch and commit my latest solutions from LeetCode, along with their submission history.

## ✨ Features
Automatic Synchronization: Solutions are automatically synced to this repository on a weekly schedule (every Saturday at 1:30 PM IST).
Historical Commits: Each solution is committed with its original LeetCode submission date, preserving an accurate problem-solving timeline.
Organized Structure: Solutions are stored in dedicated folders by problem name, making them easy to browse and reference.

## 🚀 How I Implemented This (A Step-by-Step Guide)
This guide walks you through setting up a similar synchronization feature for your own LeetCode solutions.

### Prerequisites
A GitHub account and an empty repository (e.g., named leetcode-solutions).
A LeetCode account with some accepted solutions.
Basic understanding of Git and GitHub.

### Step 1: Create Your GitHub Repository
First, create a new empty GitHub repository. You can name it anything you like (e.g., leetcode-solutions, my-leetcode-journey). Do not initialize it with a README, .gitignore, or license at this stage to keep it clean.

### Step 2: Obtain LeetCode csrftoken and LEETCODE_SESSION
These are crucial for the GitHub Action to authenticate with LeetCode's API and fetch your solutions. They act like temporary login credentials.
Go to leetcode.com in your web browser (Chrome, Firefox, Edge, etc.).
Log in to your LeetCode account if you aren't already.
Open Developer Tools:
Right-click anywhere on the page and select "Inspect" or "Inspect Element."
Alternatively, use keyboard shortcuts: Ctrl + Shift + I (Windows/Linux) or Cmd + Option + I (Mac).
Navigate to the "Network" tab within the Developer Tools.
Reload the LeetCode page (press F5 or click the browser's refresh button). This will populate the Network tab with requests.
Find a LeetCode Request: In the list of requests, look for one made to leetcode.com (often the main document request or any API call). Click on it.
Inspect "Request Headers": In the details panel for that request, find the "Headers" tab/section, and then locate "Request Headers."
Copy the Cookie values: Scroll down until you see the Cookie header. Inside this string, you'll find two key-value pairs you need to extract:
csrftoken=YOUR_CSRF_TOKEN_VALUE
LEETCODE_SESSION=YOUR_LEETCODE_SESSION_VALUE
Copy only the values (the long strings after the = sign).

### Step 3: Add Tokens to GitHub Secrets
For security, you should never hardcode sensitive information directly into your workflow files. GitHub Secrets provides a secure way to store them.
Go to your GitHub repository (the one you created in Step 1).
Click on "Settings" (usually near the top right of the repository page).
In the left sidebar, scroll down to the "Security" section and click on "Secrets and variables".
Click on the "Actions" tab.
Click the "New repository secret" button.
Create two separate secrets:
Name: LEETCODE_CSRF_TOKEN
Value: Paste the csrftoken value you copied from LeetCode.
Name: LEETCODE_SESSION
Value: Paste the LEETCODE_SESSION value you copied from LeetCode.
Click "Add secret" for each one.

### Step 4: Create the GitHub Actions Workflow File
This YAML file defines the automated process for syncing.
In your GitHub repository, click on the "Actions" tab.
Click on "New workflow" or "Set up a workflow yourself."
Choose to create a new file and name it sync_leetcode.yml (inside the .github/workflows/ directory).
Copy and paste the following code into the sync_leetcode.yml file:
name: Sync Leetcode

on:
  workflow_dispatch: # Allows manual triggering from GitHub Actions tab
  schedule:
    - cron: "0 8 * * 6" # Runs automatically every Saturday at 8:00 AM UTC (1:30 PM IST)

jobs:
  build:
    runs-on: ubuntu-latest # The environment where the job will run

    steps:
      # Checkout your repository so the action can access it
      - name: Checkout repository
        uses: actions/checkout@v4

      # The LeetCode sync action
      - name: Sync LeetCode Solutions
        uses: joshcai/leetcode-sync@v1.5 # Using version 1.5 of the action
        with:
          github-token: ${{ github.token }} # Built-in token for GitHub API access
          leetcode-csrf-token: ${{ secrets.LEETCODE_CSRF_TOKEN }} # Your LeetCode CSRF token
          leetcode-session: ${{ secrets.LEETCODE_SESSION }}   # Your LeetCode session token
          # No destination-folder specified, so problems will be directly in the repository root


Commit this file to your repository (e.g., with a commit message like "Add LeetCode sync workflow").

### Step 5: Configure Workflow Permissions
The github.token needs explicit permission to write to your repository.
Go to your GitHub repository "Settings".
In the left sidebar, click on "Actions" under "Code and automation."
Click on "General".
Scroll down to the "Workflow permissions" section.
Select the radio button for "Read and write permissions".
Click the "Save" button.

### Step 6: Initial Run and Verification
Go to the "Actions" tab in your repository.
On the left sidebar, click on "Sync Leetcode" (the name of your workflow).
Click the "Run workflow" button, then "Run workflow" again in the dropdown. This will manually trigger a run.
Monitor the run: Click on the running workflow to see the live logs. Expand the build job and then the Sync LeetCode Solutions step. Look for "HttpError" or "Error" messages. If it completes successfully, you should see new commits and files in your repository!

### Step 7: Adjust Folder Structure (Optional Cleanup)
If you initially ran the workflow with destination-folder: my-folder, your solutions will be nested inside my-folder/problems. To move them directly to the repository root:
Clone your repository to your local machine (if you haven't already).
Open your terminal/command prompt and navigate into your cloned repository's directory.
Move the contents:
mv my-folder/problems/* .


Remove the empty my-folder directory:
rmdir my-folder/problems
rmdir my-folder


Stage, commit, and push these changes to GitHub:
git add .
git commit -m "Moved LeetCode solutions to repository root"
git push origin main # Or 'master'


## ⚠️ Troubleshooting

### HttpError: 
Resource not accessible by integration: Double-check that your "Workflow permissions" are set to "Read and write permissions" in your repository settings (Step 5).

### Authentication errors (401 Unauthorized, Invalid session, etc.): 
Your LEETCODE_CSRF_TOKEN or LEETCODE_SESSION secrets have likely expired or are incorrect. Repeat Step 2 and Step 3 to obtain and update fresh tokens.

### Unexpected input(s) warning: 
If you see this, ensure your workflow file matches the provided YAML in Step 4, as older versions of the joshcai/leetcode-sync action might not support all input parameters.

Feel free to open an issue in this repository if you encounter any problems!
