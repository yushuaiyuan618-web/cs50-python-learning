import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python itunes.py SEARCH_TERM")

response = requests.get(
    "https://itunes.apple.com/search",
    params={
        "entity": "song",
        "limit": 1,
        "term": sys.argv[1]
    },
    timeout=10
)

response.raise_for_status()

data = response.json()

for result in data["results"]:
    print(result["trackName"])