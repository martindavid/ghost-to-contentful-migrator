import os
from ghost import GhostAPI


def migrate():
    ghost_api_key = os.getenv('GHOSTJS_API_KEY', '')
    ghost_base_url = os.getenv('GHOSTJS_BASE_URL', '')
    ghost = GhostAPI(ghost_base_url, ghost_api_key)

    posts = ghost.fetch_posts()

    print(f"Fetch {len(posts)} post from Ghostjs")


if __name__ == '__main__':
    migrate()
