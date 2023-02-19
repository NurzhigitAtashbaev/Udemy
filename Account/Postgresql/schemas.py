from pydantic import BaseModel
from enum import Enum


class UserBase(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str


class UserCreate(UserBase):
    type: str
    experience: str
    audience: str
    is_mentor: bool


class Type(str, Enum):
    mentor = "mentor"
    user = 'user'
    super = 'super'


class Experience(str, Enum):
    junior = 'junior'
    middle = 'middle'
    senior = 'senior'


class Audience(str, Enum):
    student = "student"
    professional = "professional"


class User(UserBase):
    id: int
    type: Type
    experience: Experience
    audience: Audience
    is_mentor: bool

    class Config:
        orm_mode = True


class Profile(BaseModel):
    competence: str
    language: str
    site_url: str
    twitter_url: str
    facebook_url: str
    linkedin_url: str
    youtube_url: str
    image: str
    is_hidden: bool
    is_hidden_courses: bool
    promotions: bool
    mentor_ads: bool
    email_ads: bool

    class Config:
        orm_mode = True
