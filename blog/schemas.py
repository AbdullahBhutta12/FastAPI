from pydantic import BaseModel, ConfigDict


class Blog(BaseModel):
    title: str
    body: str


class ShowBlog(Blog):
    title: str
    body: str
    # class Config:
    #     orm_mode = True
    model_config = ConfigDict(from_attributes=True)


class User(BaseModel):
    name: str
    email: str
    password: str
