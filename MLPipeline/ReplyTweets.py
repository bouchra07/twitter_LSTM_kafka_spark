import tweepy
from tweepy import OAuthHandler
import json
from flask import Flask, request
import random
from .Config import Config

class ReplyTweet(Config):

    def __init__(self):

        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)

    def sendReply(self, tweetId, user, text):
        try:
            text = "@" + user + " " + text
            print(text)
            self.api.update_status(text, int(tweetId))
            return True
        except Exception as e:
            print(e)
            return False

    def getReplyText(self, complain_type, ticketId):
        reply_txt = "Appologies for the inconvience caused. We are taking this via ticket id " + str(
            ticketId) + " it will be resolved asap."
        return reply_txt

    def reply_toTweet(self, tweetId, complain, complain_type, user):
        if bool(complain):
            ticketId = int(random.random() * 100000)
            txt = self.getReplyText(complain_type, ticketId)
            replied = self.sendReply(tweetId, user, txt)
        else:
            ticketId = ""
            replied = False
        return json.dumps({"replied": replied, "ticketId": ticketId})