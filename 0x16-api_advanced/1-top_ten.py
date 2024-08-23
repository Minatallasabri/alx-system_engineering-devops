#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
  """Print the titles of the 10 hottest posts on a given subreddit."""
  url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)   

  headers = {
      "User-Agent": "linux:reddit_api:v1.0.0   
 (by /u/your_username)"  # Replace with your username
  }
  params = {
      "limit": 10
  }
  response = requests.get(url, headers=headers, params=params, allow_redirects=False)

  # Check for successful response (status code 200)
  if response.status_code == 200:
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
    print("None")  # Print None for invalid subreddits or errors