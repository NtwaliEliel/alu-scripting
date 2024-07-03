import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API for the number of subscribers of a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"  # Direct URL for subreddit info
    headers = {"User-Agent": "My Reddit API Script 0.1"}  # Custom User-Agent to avoid throttling

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)  # Don't follow redirects
        response.raise_for_status()  # Raise an exception for non-200 status codes

        data = response.json()
        if data.get('data', {}).get('subscribers'):  # Check for valid data structure
            return data['data']['subscribers']
        else:
            return 0  # Handle cases where subscriber count is not present

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching subscriber count: {e}")
        return 0
