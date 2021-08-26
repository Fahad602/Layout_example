from flask_sqlalchemy import SQLAlchemy
from layout_example.db.models.blog import Blogpost
from datetime import datetime

def returnall_q():
    return Blogpost.query.order_by(Blogpost.date_posted.desc()).all()

def addpost_q(title,subtitle,author,content):
    return Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

def deletepost_q(i_d):
    Blogpost.query.filter_by(id=i_d).delete()

def returnone_q(i_d):
    return Blogpost.query.filter_by(id= i_d).one()