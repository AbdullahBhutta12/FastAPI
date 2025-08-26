from pydantic import BaseModel, ConfigDict
from typing import List

class Blog(BaseModel):
    title: str
    body: str
    model_config = ConfigDict(from_attributes=True)


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]
    model_config = ConfigDict(from_attributes=True)


class ShowBlog(BaseModel):
    # title: str
    # body: str
    creator: ShowUser
    model_config = ConfigDict(from_attributes=True)