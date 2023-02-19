from sqlalchemy import Column, Integer, String, Enum, Boolean, MetaData
from Account.Postgresql.database import Base
from sqlalchemy.orm import relationship

metadata = MetaData()
class User(Base):

    __tablename__ = 'User'
    metadata
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
    type = Column(Enum)
    experience = Column(Enum)
    audience = Column(Enum)
    is_mentor = Column(Boolean)
    first_name = Column(String)
    last_Name = Column(String)


class Profile(Base):
    __tablename__ = 'Profile'
    metadata
    id = Column(Integer, primary_key=True)
    user_id = relationship(User, backref='user')
    competence = Column(String)
    language = Column(String)
    site_url = Column(String)
    twitter_url = Column(String)
    facebook_url = Column(String)
    linkedin_url = Column(String)
    youtube_url = Column(String)
    image = Column(String)
    is_hidden = Column(Boolean)
    is_hidden_courses = Column(Boolean)
    promotions = Column(Boolean)
    mentor_ads = Column(Boolean)
    email_ads = Column(Boolean)
