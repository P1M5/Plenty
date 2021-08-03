import json
import requests


def get_token():
    r = requests.get("https://open.spotify.com/")
    # print(r, r.headers)
    print(r, r.content)

    # extract div containing the token from the html
    # dom_tree = html.fromstring(token_results.content)
    # token_div = dom_tree.xpath('//*[@id="config"]/text()')


def search_spotify():
    headers = {
        "authorization": "Bearer BQC9iUwptSuLrhHIcfx_YOtvELDEKTeUSzb1_yHlAledBslOiJ52Np-eCS6-bKyCm3yCbGzFkf9TiTQzx_w",
    }

    r = requests.get("https://api.spotify.com/v1/search?type=album%2Cartist%2Cplaylist%2Ctrack%2Cshow_audio%2C"
                     "episode_audio&q=equal&decorate_restrictions=false"
                     "&best_match=true&include_external=audio&limit=10&market=US",
                     headers=headers)

    print(r, json.dumps(r.json()))


if __name__ == "__main__":
    get_token()
    # search_spotify()
