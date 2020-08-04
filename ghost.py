import requests
from typing import List
from models.ghost import Post


class GhostAPI:
    def __init__(self, base_url: str, api_key: str) -> None:
        self.base_url = base_url
        self.api_key = api_key

    def fetch_posts(self) -> List[Post]:
        params = {'key': self.api_key, 'page': 1, 'include': 'authors,tags'}
        keep_fetch = True
        posts = []
        while (keep_fetch):
            r = requests.get(f"{self.base_url}/ghost/api/v2/content/posts/",
                             params=params)

            response = r.json()

            parsed_posts = self.__parse_posts(response["posts"])

            if len(parsed_posts) > 0:
                posts = posts + parsed_posts

            next_page = response["meta"]["pagination"]["next"]

            if (next_page is None):
                keep_fetch = False
            else:
                params['page'] = next_page

        return posts

    def __parse_posts(self, json_resp: List[dict] = None) -> List[Post]:
        if len(json_resp) == 0:
            return []

        posts = []
        for post in json_resp:
            parsed_obj = Post.parse_obj(post)
            posts.append(parsed_obj)

        return posts
