import requests

# GitHub API endpoint to get the contents of a repo
repo_owner = "ssss"  
repo_name = "anagha_repositry_1"  
branch = "github"  
# token = "gAAAAABnNJ3-xuc5LXaPrvr9InnaGQhLrPuRMF8xfG6AzK9-PtVt6KXzcJV27qVAhqvKtopThsVw51WsY0mIA4WtRiyEZtwJ3Q=="
token = "!!!!!!!!!!!!!!!!!!!!!!!!!"
url = f"https://api.github.com/repos/{repo_owner}/"
url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/"
params = {"ref": token}

# Make the GET request to GitHub API
response = requests.get(url, params=params)

if response.status_code == 200:
    files = response.json()
    for file in files:
        print(file['name'], file['type'])
else:
    print(f"Error: {response.status_code}")

# repo_url = "https://api.github.com/users/{}/repos".format(repo_owner)
# response = requests.get(repo_url, auth = (repo_owner, token)) 
             
# if response.status_code == 200:
#     print("Github successfully connected")
# else:
#     print("Not connected")

# import requests

# repo_owner = "ssss"
# repo_name = "anagha_repositry_1"
# branch = "github"
# token = "!!!!!!!!!!!!!!!!!!!!!!!!!"  # Use your actual token here

# repo_url = f"https://api.github.com/users/{repo_owner}/repos"
# response = requests.get(repo_url, auth=(repo_owner, token))

# if response.status_code == 200:
#     print("Github successfully connected")
# elif response.status_code == 401:
#     print("Authentication failed: Invalid username or token.")
# else:
#     print(f"Failed to connect. Status code: {response.status_code}")
