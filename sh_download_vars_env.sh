#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 5 ]; then
  echo "Usage: $0 <REPO_OWNER> <REPO_NAME> <GITHUB_TOKEN> <ENVIRONMENT> <ENV_FILE>"
  exit 1
fi

# Variables
REPO_OWNER="$1"          # GitHub owner/organization name
REPO_NAME="$2"           # GitHub repository name
GITHUB_TOKEN="$3"       # GitHub PAT (can also be set as an env var)
ENVIRONMENT="$4"        # GitHub Actions environment (e.g., production, staging)
ENV_FILE="$5"           # Path to your .env file

# GitHub API URLs
GITHUB_API="https://api.github.com"
ENV_VARS_URL="$GITHUB_API/repos/$REPO_OWNER/$REPO_NAME/environments/$ENVIRONMENT/variables"

# Function to download environment variables using GitHub API
download_env_vars() {
  # Construct the curl command to get environment variables
  CURL_CMD="curl -s -X GET \
    -H \"Authorization: token $GITHUB_TOKEN\" \
    -H \"Accept: application/vnd.github+json\" \
    \"$ENV_VARS_URL\""

  echo "Executing: $CURL_CMD"   # Print the full curl command

  # Execute the curl command and get the response
  response=$(eval "$CURL_CMD")

  # Check if the response is valid
  if [ $? -ne 0 ]; then
    echo "Failed to fetch environment variables."
    exit 1
  fi

  echo "$response" | jq -r '.variables[] | "\(.name)=\(.value)"' > "$ENV_FILE"
  echo "Downloaded environment variables to $ENV_FILE"
}

# Call the function to download environment variables
download_env_vars
