#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
  """Print the titles of the 10 hottest posts on a given subreddit."""
  url = "https://www.reddit.get/r/{}/hot/.json".format(subreddit)  # Fixed typo in URL
  headers = {
      "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
  }
  params = {
      "limit": 10
  }
  response = requests.get(url, headers=headers, params=params, allow_redirects=False)

  # Check for successful response (status code 200)
  if response.status_code == 200:
    # Uncomment the following line to print the full JSON response for debugging
    # print(response.text)

    try:
      results = response.json()  # Assuming successful JSON parsing
      # Extract post titles from children list
      for post in results.get("data", {}).get("children", []):
        title = post.get("data", {}).get("title")
        if title:
          print(title)  # Print only titles with valid data
    except (KeyError, JSONDecodeError):
      print("Error parsing JSON response.")
  else:
    print(f"Error: {response.status_code}")  # Print specific error code

# Example usage
top_ten("learnpython")
