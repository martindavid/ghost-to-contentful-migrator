from typing import List
from pydantic import BaseModel
from datetime import datetime


class Tag(BaseModel):
    id: str
    slug: str
    name: str
    description: str = None
    feature_image: str = None
    visibility: str
    meta_title: str = None
    meta_description: str = None


class Author(BaseModel):
    id: str
    slug: str
    name: str
    profile_image: str = None
    cover_image: str = None
    bio: str = None
    website: str = None
    location: str = None
    facebook: str = None
    twitter: str = None
    meta_title: str = None
    meta_description: str = None


class Post(BaseModel):
    id: str
    title: str
    slug: str
    html: str
    feature_image: str
    created_at: datetime
    published_at: datetime
    custom_excerpt: str = None
    primary_author: Author = None
    authors: List[Author] = None
    primary_tag: Tag = None
    tags: List[Tag] = None
    excerpt: str
    meta_title: str = None
    meta_description: str = None
    og_image: str = None
    og_title: str = None
    og_description: str = None
    twitter_image: str = None
    twitter_title: str = None
    twitter_description: str = None
    images: List[str] = None
