#!/usr/bin/env python
from flask import Flask, request, url_for, render_template
from json import loads
import os

with open('data.json', 'r') as datafile:
    settings = loads(datafile.read())

app = Flask(__name__)
app.jinja_env.autoescape = False
@app.route('/')
def main():
    posts = []
    #files = [ f for f in os.listdir('blog') if f[0] != '.' ]
    #files.sort()
    #for blogpost in files[::-1]:
    #    with open('blog/' + blogpost) as f:
    #        posts.append(loads(f.read()))
    return render_template('index.html', settings=settings, posts=posts)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=4443,
        ssl_context=('certs/openwebhost.ml.crt', 'certs/openwebhost.ml.key'),
        debug=True
    )
