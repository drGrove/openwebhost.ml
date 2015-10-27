#!/usr/bin/env python
from flask import Flask, request, url_for, render_template
from json import loads
import os
import MySQLdb

with open('data.json', 'r') as datafile:
    settings = loads(datafile.read())

mysqlenv = lambda name: os.getenv('MYSQL_ENV_MYSQL_' + name)

env = {
    "host": os.getenv('MYSQL_PORT_3306_TCP_ADDR'),
    "user": mysqlenv('USER') or 'root',
    "passwd": (mysqlenv('PASSWORD')
        if mysqlenv('USER')
        else mysqlenv('ROOT_PASSWORD')),
    "db": mysqlenv('DATABASE')
}
connection = MySQLdb.connect(**env)
cursor = connection.cursor()

app = Flask(__name__)
app.jinja_env.autoescape = False
@app.route('/')
def main():
    posts = []
    cursor.execute("SELECT * FROM posts ORDER BY id DESC LIMIT 5;")
    for item in cursor.fetchall():
        posts.append({"title": item[1], "content": item[2], "date": item[3]})
    return render_template('index.html', settings=settings, posts=posts)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8888,
        #port=4443,
        #ssl_context=('certs/openwebhost.ml.crt', 'certs/openwebhost.ml.key'),
        debug=True
    )
