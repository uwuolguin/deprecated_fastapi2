from pydantic import BaseModel,conint
from pydantic.networks import EmailStr

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

class userCreate(BaseModel):
    email: EmailStr
    password :  str

class userLogin(BaseModel):
    email: EmailStr
    password :  str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

  