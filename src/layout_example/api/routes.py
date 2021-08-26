from flask import Flask, render_template, request, redirect, url_for,Blueprint
from flask_sqlalchemy import SQLAlchemy
from layout_example.db.models.blog import Blogpost
from layout_example.db.db import db
from datetime import datetime
from layout_example.api.resources.queries import *

app= Blueprint('route', __name__, url_prefix='/route')

@app.route('/')
def index():
    posts = returnall_q()
    return render_template('index.html',posts=posts)

#adding a blog to db
@app.route('/add')
def add():
    return render_template('addpost.html')

@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['stitle']
    author = request.form['author']
    content = request.form['content']

    post = addpost_q(title,subtitle,author,content)

    db.session.add(post)
    db.session.commit()

    posts = returnall_q()
    return render_template('index.html',posts=posts)


#deleting a blog from db
@app.route('/delete')
def delete():
    return render_template('deletepost.html')


@app.route('/deletepost', methods=['POST'])
def deletepost():
    i_d = request.form['id']
    deletepost_q(i_d)
    db.session.commit()

    posts = returnall_q()
    return render_template('index.html',posts=posts)


#view a single blog from db
@app.route('/view')
def view():
    return render_template('viewpost.html')

@app.route('/viewpost', methods=['POST'])
def viewpost():
    i_d = request.form['id']
    post = returnone_q(i_d)
    
    return render_template('post.html', post = post)

#edit a blog
@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/editblog', methods=['POST'])
def editblog():
    i_d = request.form['id']
    post = returnone_q(i_d)

    return render_template('editblog.html',post=post)

@app.route('/saveedit', methods=['POST'])
def saveedit():
    i_d=request.form['id']
    edit = returnone_q(i_d)
    edit.title = request.form['title']
    edit.subtitle = request.form['stitle']
    edit.author = request.form['author']
    edit.content = request.form['content']
    db.session.commit()

    posts = returnall_q()
    return render_template('index.html',posts=posts)