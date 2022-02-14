from tweepy import StreamListener
import json

class TweetsListener(StreamListener):

    def __init__(self,producer,topic_name):
        self.producer = producer
        self.topic_name = topic_name

    def on_data(self, data):
        try:
            msg = json.loads(data)
            print("new message")

            if "extended_tweet" in msg:
                out_data = '{ "tweet":"' + str(msg['extended_tweet']['full_text']).replace("\n",
                                                                                           "") + '","user":"' + str(
                    msg['user']['screen_name']) + '", "tweet_id":"' + str(msg['id_str']) + '" }'
                print(out_data)
                self.producer.send(self.topic_name, str.encode(out_data))
            else:
                out_data = '{ "tweet":"' + str(msg['text']).replace("\n", "") + '","user":"' + str(
                    msg['user']['screen_name']) + '", "tweet_id":"' + str(msg['id_str']) + '" }'
                print(out_data)
                self.producer.send(self.topic_name, str.encode(out_data))
            return True

        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

    def on_exception(self, exception):
        print(exception)
        return