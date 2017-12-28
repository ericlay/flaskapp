#!/usr/bin/env python3

import configparser
import twitter
import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "working"

@app.route('/getInfo')
def getInfo():
    return render_template('index.html')

@app.route('/tweet')
def tweet():
    config = sonfigparser.ConfigParser()
    config.read('.tweetrc')
    checkbox = request.form['checkBox']
    handle = request.form['handle']
    message = "is the worst."
    rc = TweetRc()
    consumer_key = config.get('Tweet', consumer_key)
    consumer_secret = config.get('Tweet', consumer_secret)
    access_key = config.get('Tweet', access_key)
    access_secret = config.get('Tweet', access_secret)
    encoding = None
    api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
                      access_token_key=access_key, access_token_secret=access_secret,
                      input_encoding=encoding)

    if checkBox == True:
        status = api.PostUpdate(handle + ' ' + message)
    else:
        status = api.PostUpdate(message)


if __name__ == "__main__":
    app.run()
