from .Config import Config
from tweepy import OAuthHandler


class TwitterAuth(Config):
    def authenticateTwitterApp(self):
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)

        # auth = tweepy.OAuth2BearerHandler("xxxx")
        # auth = tweepy.API(auth)

        return auth