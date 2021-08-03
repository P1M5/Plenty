import json
import requests


def get_access_token():
    headers = {
        "accept": "text/html",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "dnt": "1",
        "pragma": "no-cache",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "sec-gpc": "1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.120 Safari/537.36"  # randomly generated user agent
    }

    # get the html page (including the access token)
    r = requests.get("https://open.spotify.com/", headers=headers)

    # extract the token from the html page
    split_front = str(r.content).split('"accessToken":"')
    split_back = split_front[1].split('","', 1)
    return split_back[0]


def search_spotify(access_token, keyword):
    # prepare the request's headers and url
    headers = {
        "authorization": "Bearer " + access_token,
    }
    url = "https://api.spotify.com/v1/search?type=album%2Cartist%2Cplaylist%2Ctrack%2Cshow_audio%2Cepisode_audio" \
          "&q=" + keyword + "&decorate_restrictions=false&best_match=true&include_external=audio&limit=10&market=US"

    # get the search results
    r = requests.get(url, headers=headers)

    # print the search results
    print(r, json.dumps(r.json()))


if __name__ == "__main__":
    search_spotify(get_access_token(), "discord")
