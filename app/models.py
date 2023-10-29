from sqlalchemy import Column, Integer,String,Boolean,ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship


class User(Base):    
    __tablename__= "users"
    id= Column(Integer,primary_key=True,nullable=False)
    email=Column(String,unique=True,nullable=False)
    password= Column(String,nullable=False)
    created_at= Column(TIMESTAMP(timezone=True), nullable=False,server_default=text('now()'))
    @hybrid_property
    def fullemail(self):
        return self.email



class Post(Base):
    __tablename__= "posts"
    id= Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    content= Column(String,nullable=False)
    published= Column(Boolean,server_default="TRUE")
    created_at= Column(TIMESTAMP(timezone=True), nullable=False,server_default=text('now()'))
    owner_id= Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    owner= relationship("User")
    @hybrid_property
    def fullid(self):
        return self.id
    @hybrid_property
    def fulltitle(self):
        return self.title
    @hybrid_property
    def fullownerid(self):
        return self.owner_id
    @hybrid_property
    def fullowner(self):
        return self.owner
    

class Vote(Base):
    __tablename__= "votes"
    user_id= Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)  
    
