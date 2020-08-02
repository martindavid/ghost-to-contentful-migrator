from pydantic import BaseModel
from datetime import datetime


class Post(BaseModel):
    id: str
    title: str
    slug: str
    html: str
    feature_image: str
    created_at: datetime
    published_at: datetime
    custom_excerpt: str = None
    primary_author: str = None
    primary_tag: str = None
    excerpt: str
    meta_title: str = None
    meta_description: str = None
    og_image: str = None
    og_title: str = None
    og_description: str = None
    twitter_image: str = None
    twitter_title: str = None
    twitter_description: str = None
