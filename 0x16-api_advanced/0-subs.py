#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit. If not valid subreddit, returns 0
"""
import requests

def number_of_subscribers(subreddit):
    try:
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/39.0.2171.95 Safari/537.36',
            'accept': 'application/json'}
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        
        # Check if 'data' and 'subscribers' are in the response
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
    except KeyError:
        return 0

# Example usage
if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    print(number_of_subscribers(subreddit))
